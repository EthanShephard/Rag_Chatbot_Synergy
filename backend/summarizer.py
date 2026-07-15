from backend.memory import(
    load_session,
    save_session,
    MAX_MESSAGES
)

# CHANGED: no longer using Ollama's qwen2.5:3b — summarization now runs on
# Anthropic's Haiku, the cheapest/fastest model, matching MAIN_MODEL and
# REWRITE_MODEL in chatbot.py. Kept as its own constant in case you ever
# want a different model here than the rewrite step uses.
SUMMARY_MODEL = "claude-haiku-4-5-20251001"


def summarize_if_needed(session_id: str, client):
    session = load_session(session_id)
    messages = session["messages"]
    if len(messages) <= MAX_MESSAGES:
        return
    old_messages = messages[:-6]
    recent_messages = messages[-6:]
    conversation = "\n".join(
        f"{m['role'].capitalize()}: {m['content']}"
        for m in old_messages
    )
    old_summary = session["summary"]
    prompt = f"""
Previous Summary:
{old_summary}
-------------------------
Conversation:
{conversation}
-------------------------
Update the summary.
Requirements:
- Preserve important user preferences.
- Preserve decisions.
- Preserve ongoing tasks.
- Remove greetings and filler.
- Maximum 250 words.
Return ONLY the updated summary.
"""
    try:
        # CHANGED: swapped Ollama's `client.chat(...)` call for Anthropic's
        # `client.messages.create(...)`. Anthropic takes `system` as a
        # separate top-level param rather than a "system" role message.
        response = client.messages.create(
            model=SUMMARY_MODEL,
            max_tokens=400,  # ~250 words + margin
            temperature=0,
            system="You summarize conversation for long term memory",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
    except Exception:
        # Anthropic unreachable/slow — this runs after the user's answer has
        # already been streamed back, so raising here would only surface
        # as a noisy server-side error for no benefit. Leave the full,
        # untrimmed history in place and try again on the next turn.
        return

    # CHANGED: response shape is different from Ollama's dict-based
    # response["message"]["content"] — Anthropic returns a list of content
    # blocks, so we pull text off the first block instead.
    session["summary"] = response.content[0].text.strip()
    session["messages"] = recent_messages
    save_session(session_id, session)

from backend.memory import(
    load_session,
    save_session,
    MAX_MESSAGES
)

# CHANGED: switched from Anthropic Haiku to DeepSeek's small model,
# matching MAIN_MODEL and REWRITE_MODEL in chatbot.py.
SUMMARY_MODEL = "deepseek-v4-flash"


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
        # CHANGED: DeepSeek uses the OpenAI-style API —
        # `client.chat.completions.create(...)` instead of
        # `client.messages.create(...)`, and the system instruction goes
        # inside the `messages` list as a "system" role message rather
        # than a separate top-level `system` param.
        # Thinking mode is disabled — summarization doesn't need hidden
        # chain-of-thought, and leaving it on would bill reasoning tokens
        # at the output rate for no benefit here.
        response = client.chat.completions.create(
            model=SUMMARY_MODEL,
            max_tokens=400,  # ~250 words + margin
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You summarize conversation for long term memory"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            extra_body={"thinking": {"type": "disabled"}},
        )
    except Exception:
        # DeepSeek unreachable/slow — this runs after the user's answer has
        # already been streamed back, so raising here would only surface
        # as a noisy server-side error for no benefit. Leave the full,
        # untrimmed history in place and try again on the next turn.
        return

    # CHANGED: OpenAI-style response shape —
    # `response.choices[0].message.content` instead of Anthropic's
    # `response.content[0].text`.
    session["summary"] = response.choices[0].message.content.strip()
    session["messages"] = recent_messages
    save_session(session_id, session)

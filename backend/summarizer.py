from backend.memory import(
    load_session,
    save_session,
    MAX_MESSAGES
)

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
        response = client.chat(
            model = "qwen2.5:3b",
            stream = False,
            messages = [
                {
                    "role": "system",
                    "content": "You summarize conversation for long term memory"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    except Exception:
        # Ollama unreachable/slow — this runs after the user's answer has
        # already been streamed back, so raising here would only surface
        # as a noisy server-side error for no benefit. Leave the full,
        # untrimmed history in place and try again on the next turn.
        return

    session["summary"] = response["message"]["content"].strip()
    session["messages"] = recent_messages

    save_session(session_id, session)
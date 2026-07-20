import re
import time
from pathlib import Path
import os

# CHANGED: DeepSeek exposes an OpenAI-compatible endpoint, not Anthropic's.
# Swapped the `anthropic` SDK for the `openai` SDK pointed at DeepSeek's
# base_url. (Add `openai` to requirements.txt and remove `anthropic` if
# nothing else in the project still needs it.)
from openai import OpenAI

from backend.retrieval import (
    keyword_scoped_search,
    extract_keywords,
    scrub_price_disclaimer,
    convert_bare_usd_rows,
    initialize_retrieval,
)

from backend.memory import (
    load_history,
    load_summary,
    save_turn
)
from backend.summarizer import summarize_if_needed
from backend.prompt import PROMPT


# ========================== DEEPSEEK SETUP ==========================
# CHANGED: DeepSeek client, same OpenAI-style interface, different base_url
# and a different env var for the key.
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# CHANGED: deepseek-v4-flash is DeepSeek's small/cheap model (the
# `deepseek-chat` alias is deprecated as of 2026/07/24). Used for both
# the main answer and the rewrite step — there's no separate "mini" tier
# below Flash the way Haiku sits below Sonnet on Anthropic.
MAIN_MODEL = "deepseek-v4-flash"

MAX_TOKENS = 4096
TEMPERATURE = 0.7

MAX_HISTORY_TURNS = 10

_retrieval_ready = False


def ensure_retrieval_ready():
    global _retrieval_ready
    if not _retrieval_ready:
        initialize_retrieval()
        _retrieval_ready = True


def build_messages(question, context, history, summary):
    """
    CHANGED: DeepSeek's API (OpenAI-style) takes `system` as a message
    inside the `messages` list, not as a separate top-level param like
    Anthropic. This now returns a single `messages` list with the system
    message first, instead of (system_text, messages).
    """
    system_parts = [PROMPT]

    if summary.strip():
        system_parts.append(f"Conversation Summary:\n{summary}")

    system_text = "\n\n".join(system_parts)

    messages = [{"role": "system", "content": system_text}]
    messages.extend(history[-MAX_HISTORY_TURNS:])

    messages.append(
        {
            "role": "user",
            "content": f"""Context:

{context}

Question:

{question}
"""
        }
    )

    return messages


def ask(question, session_id):
    total = time.perf_counter()

    ensure_retrieval_ready()

    # Load memory
    t = time.perf_counter()
    history = load_history(session_id)
    summary = load_summary(session_id)
    print(f"[TIME] Memory: {time.perf_counter()-t:.3f}s")

    # Retrieval — keyword-scoped search instead of an LLM rewrite step.
    # Recent conversation is pulled in directly as extra keyword context, so
    # a vague follow-up like "show me just the cables" or "what are the
    # prices" inherits the topic scope established earlier — including the
    # SPECIFIC products the assistant itself surfaced last turn, not just
    # whatever the user happened to retype. Relying on user turns alone
    # loses that: if the assistant answered with "SMB, SMC, Low PIM 7/16
    # DIN..." and the user just says "what are the prices," those specific
    # product names need to come from the assistant's last reply, since
    # the user never said them.
    t = time.perf_counter()
    last_assistant_reply = next(
        (msg["content"] for msg in reversed(history) if msg.get("role") == "assistant"),
        "",
    )
    recent_user_turns = " ".join(
        msg["content"] for msg in history[-6:] if msg.get("role") == "user"
    )
    # Order matters for the cascading filter: the current question comes
    # first (inside keyword_scoped_search itself), then the last answer's
    # established topic, then broader recent user intent.
    history_text = f"{last_assistant_reply} {recent_user_turns}"
    results = keyword_scoped_search(question, history_text=history_text, top_k=15)
    print(f"[TIME] Retrieval: {time.perf_counter()-t:.3f}s")

    # Build prompt
    t = time.perf_counter()
    context = "\n\n".join(
        f"""Product Link: {c.get('url', '')}
Page: {c.get('page', '')}

Content:
{scrub_price_disclaimer(convert_bare_usd_rows(c['text']))}"""
        for c in results
    )

    # CHANGED: build_messages now returns one combined `messages` list
    # (system message included) instead of (system_text, messages).
    messages = build_messages(
        question, context, history, summary
    )
    print(f"[TIME] Prompt Build: {time.perf_counter()-t:.3f}s")

    print("\n==============================")
    print("Question :", question)
    print("Last assistant reply (used for scope):", last_assistant_reply[:200])
    print("Actual keywords used:", extract_keywords(f"{question} {history_text}"))
    print("==============================")

    # ========================== DEEPSEEK STREAMING ==========================
    t = time.perf_counter()

    assistant_response = ""
    first = True
    print("\n========== RETRIEVED CHUNKS ==========")
    for r in results:
        score = r.get('score', r.get('rrf_score'))
        score_str = f"{score:.4f}" if score is not None else "n/a"
        print(f"[{r.get('category')}] {r.get('url')}  (score={score_str})")
        print(r["text"][:150].replace("\n", " "))
        print("---")
    print("=======================================\n")
    # CHANGED: OpenAI-style streaming instead of Anthropic's
    # `client.messages.stream(...)` context manager. Also disabled thinking
    # mode here — for a RAG answer grounded in retrieved context, you want
    # the model to answer directly rather than spend output tokens on
    # hidden chain-of-thought before it starts streaming the real answer.
    stream = client.chat.completions.create(
        model=MAIN_MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        messages=messages,
        stream=True,
        extra_body={"thinking": {"type": "disabled"}},
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            if first:
                print(f"[TIME] First Token: {time.perf_counter()-t:.3f}s")
                first = False
            assistant_response += delta
            yield delta

    print(f"[TIME] Total: {time.perf_counter()-total:.3f}s")

    # Save conversation
    save_turn(
        session_id=session_id,
        user_message=question,
        assistant_message=assistant_response,
    )

    summarize_if_needed(
        session_id=session_id,
        client=client  # DeepSeek client (OpenAI-compatible), used by summarizer if it calls the API
    )

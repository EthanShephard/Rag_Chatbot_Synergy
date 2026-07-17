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
    hybrid_search,
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
REWRITE_MODEL = "deepseek-v4-flash"

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


def rewrite_question(question, history, summary):
    if not history:
        return question

    history = history[-6:]

    conversation = "\n".join(
        f"{msg['role'].capitalize()}: {msg['content']}"
        for msg in history
    )

    prompt = f"""
You are a conversational query rewriter for a Retrieval-Augmented Generation (RAG) system.

Your ONLY task is to rewrite the latest user message into a complete standalone search query.

IMPORTANT:
If the latest user message is already a complete standalone question, return it EXACTLY as written.
Do NOT paraphrase. Do NOT improve wording. Do NOT replace product names.

Conversation Summary:
{summary}

Recent Conversation:
{conversation}

Latest User Question:
{question}
"""

    try:
        # CHANGED: OpenAI-style call — `client.chat.completions.create(...)`
        # instead of `client.messages.create(...)`. Also disabled DeepSeek's
        # "thinking" mode: it's on by default for V4 models, and thinking
        # tokens bill at the output rate even though you never see them.
        # A query rewrite is a simple, non-reasoning task, so this avoids
        # paying for hidden reasoning tokens on every follow-up question.
        response = client.chat.completions.create(
            model=REWRITE_MODEL,
            max_tokens=256,
            temperature=0,
            messages=[
                {"role": "user", "content": prompt}
            ],
            extra_body={"thinking": {"type": "disabled"}},
        )
        rewritten = response.choices[0].message.content.strip()

        print("\n========== QUERY REWRITER ==========")
        print("Original :", question)
        print("Rewritten:", rewritten)
        print("====================================\n")

        return rewritten if rewritten else question
    except Exception as e:
        print(f"[WARNING] Query rewrite failed: {e}")
        return question


PRONOUNS = {"it", "its", "it's", "they", "them", "their", "this", "that",
            "these", "those", "he", "she", "his", "her", "former", "latter",
            "previous", "above"}

FOLLOWUP_STARTERS = ("what about", "how about", "and", "also", "what if",
                     "can it", "does it", "is it", "are they", "tell me more",
                     "explain more", "continue")


def should_rewrite(question: str, history: list) -> bool:
    if not history:
        return False

    q = question.lower().strip()
    if any(q.startswith(p) for p in FOLLOWUP_STARTERS):
        return True

    words = set(re.findall(r"\w+", q))
    if words & PRONOUNS:
        return True

    return False


def ask(question, session_id):
    total = time.perf_counter()

    ensure_retrieval_ready()

    # Load memory
    t = time.perf_counter()
    history = load_history(session_id)
    summary = load_summary(session_id)
    print(f"[TIME] Memory: {time.perf_counter()-t:.3f}s")

    # Query Rewrite
    t = time.perf_counter()
    if should_rewrite(question, history):
        rewritten_question = rewrite_question(question, history, summary)
    else:
        rewritten_question = question
    print(f"[TIME] Rewrite: {time.perf_counter()-t:.3f}s")

    # Retrieval
    t = time.perf_counter()
    results = hybrid_search(rewritten_question, top_k=5)
    print(f"[TIME] Retrieval: {time.perf_counter()-t:.3f}s")

    # Build prompt
    t = time.perf_counter()
    context = "\n\n".join(
        f"""Product Link: {c.get('url', '')}
Page: {c.get('page', '')}

Content:
{c['text']}"""
        for c in results
    )

    # CHANGED: build_messages now returns one combined `messages` list
    # (system message included) instead of (system_text, messages).
    messages = build_messages(
        rewritten_question, context, history, summary
    )
    print(f"[TIME] Prompt Build: {time.perf_counter()-t:.3f}s")

    print("\n==============================")
    print("Original :", question)
    print("Search   :", rewritten_question)
    print("==============================")

    # ========================== DEEPSEEK STREAMING ==========================
    t = time.perf_counter()

    assistant_response = ""
    first = True
    print("\n========== RETRIEVED CHUNKS ==========")
    for r in results:
        print(f"[{r.get('category')}] {r.get('url')}  (rrf_score={r.get('rrf_score'):.4f})")
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

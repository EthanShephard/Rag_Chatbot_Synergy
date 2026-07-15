import re
import time
from pathlib import Path
import os
import anthropic

# CHANGED: removed `get_ollama_client` import — no longer used since we
# switched to the Anthropic API. Keeping it imported was pulling in the
# ollama client module for no benefit on a memory-constrained box.
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


# ========================== ANTHROPIC SETUP ==========================
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# CHANGED: switched from Sonnet to Haiku for the main answering model too —
# cheaper and faster, and keeps the whole pipeline lighter on a 1 CPU / 2GB box.
MAIN_MODEL = "claude-haiku-4-5-20251001"

# Small/fast model used only for rewriting follow-up questions
REWRITE_MODEL = "claude-haiku-4-5-20251001"

MAX_TOKENS = 4096
TEMPERATURE = 0.7

# CHANGED: cap on how many past turns get sent to the model. Without this,
# `history` grows unbounded over a long session, increasing per-request
# memory and token cost. Tune this number to taste.
MAX_HISTORY_TURNS = 10

# CHANGED: module-level flag so the embedding model / BM25 index is loaded
# exactly once per process, not on every single request. Previously
# `initialize_retrieval()` was called inside `ask()`, meaning it re-ran
# (and potentially reloaded bge-large into memory) on every message —
# the single worst thing you can do on 1 CPU / 2GB RAM.
_retrieval_ready = False


def ensure_retrieval_ready():
    """
    Loads the retrieval stack (embedding model, BM25 index, etc.) once.
    Safe to call on every request — it's a no-op after the first call.

    Best practice: call this once from FastAPI's startup event in app.py
    instead of relying on the first incoming request to trigger it, e.g.:

        @app.on_event("startup")
        def on_startup():
            ensure_retrieval_ready()

    That way the model loads before the server accepts traffic, rather
    than causing a multi-second latency + memory spike on some user's
    first live request.
    """
    global _retrieval_ready
    if not _retrieval_ready:
        initialize_retrieval()
        _retrieval_ready = True


def build_messages(question, context, history, summary):
    """
    Anthropic's API takes `system` as a separate top-level param,
    not as a message in the list. This returns (system_text, messages).
    """
    system_parts = [PROMPT]

    if summary.strip():
        system_parts.append(f"Conversation Summary:\n{summary}")

    system_text = "\n\n".join(system_parts)

    # CHANGED: cap history to the last MAX_HISTORY_TURNS entries instead of
    # sending the full, ever-growing conversation on every request.
    messages = list(history[-MAX_HISTORY_TURNS:])

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

    return system_text, messages


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
        response = client.messages.create(
            model=REWRITE_MODEL,
            max_tokens=256,
            temperature=0,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        rewritten = response.content[0].text.strip()

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

    # CHANGED: was `initialize_retrieval()` — now calls the guarded
    # singleton loader so the embedding model / index only load once
    # per process instead of once per request.
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

    system_text, messages = build_messages(
        rewritten_question, context, history, summary
    )
    print(f"[TIME] Prompt Build: {time.perf_counter()-t:.3f}s")

    print("\n==============================")
    print("Original :", question)
    print("Search   :", rewritten_question)
    print("==============================")

    # ========================== ANTHROPIC STREAMING ==========================
    t = time.perf_counter()

    assistant_response = ""
    first = True

    with client.messages.stream(
        model=MAIN_MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=system_text,
        messages=messages,
    ) as stream:
        for text_chunk in stream.text_stream:
            if first:
                print(f"[TIME] First Token: {time.perf_counter()-t:.3f}s")
                first = False
            assistant_response += text_chunk
            yield text_chunk

    print(f"[TIME] Total: {time.perf_counter()-total:.3f}s")

    # Save conversation
    save_turn(
        session_id=session_id,
        user_message=question,
        assistant_message=assistant_response,
    )

    summarize_if_needed(
        session_id=session_id,
        client=client  # Anthropic client, used by summarizer if it calls the API
    )

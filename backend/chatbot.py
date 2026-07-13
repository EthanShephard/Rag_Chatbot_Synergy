import re
import time
from pathlib import Path
import os
import anthropic

from backend.retrieval import (
    hybrid_search,
    initialize_retrieval,
    get_ollama_client  # Keeping for potential fallback
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

# Main model used for answering the user's question
MAIN_MODEL = "claude-sonnet-4-6"

# Small/fast model used only for rewriting follow-up questions
REWRITE_MODEL = "claude-haiku-4-5-20251001"

MAX_TOKENS = 4096
TEMPERATURE = 0.7


def build_messages(question, context, history, summary):
    """
    Anthropic's API takes `system` as a separate top-level param,
    not as a message in the list. This returns (system_text, messages).
    """
    system_parts = [PROMPT]

    if summary.strip():
        system_parts.append(f"Conversation Summary:\n{summary}")

    system_text = "\n\n".join(system_parts)

    # history is expected to be a list of {"role": "user"/"assistant", "content": "..."}
    messages = list(history)

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

    # Initialize retrieval
    initialize_retrieval()

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

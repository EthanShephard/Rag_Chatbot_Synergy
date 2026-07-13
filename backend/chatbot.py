import re
import time
from pathlib import Path
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

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


# ========================== GEMINI SETUP ==========================
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

gemini_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 8192,
        "top_p": 0.95,
        "top_k": 40,
    },
    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }
)


def build_messages(question, context, history, summary):
    messages = [
        {
            "role": "system",
            "content": PROMPT,
        }
    ]

    if summary.strip():
        messages.append(
            {
                "role": "system",
                "content": f"Conversation Summary:\n{summary}"
            }
        )

    messages.extend(history)

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
        # Using Gemini for query rewriting (fast & free)
        response = gemini_model.generate_content(prompt)
        rewritten = response.text.strip()
        
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

    messages = build_messages(
        rewritten_question, context, history, summary
    )
    print(f"[TIME] Prompt Build: {time.perf_counter()-t:.3f}s")

    print("\n==============================")
    print("Original :", question)
    print("Search   :", rewritten_question)
    print("==============================")

    # ========================== GEMINI STREAMING ==========================
    t = time.perf_counter()

    # Convert to Gemini format
    gemini_history = []
    for msg in messages:
        if msg["role"] == "system":
            continue  # System prompt already in model
        role = "user" if msg["role"] == "user" else "model"
        gemini_history.append({"role": role, "parts": [msg["content"]]})

    response = gemini_model.generate_content(gemini_history, stream=True)

    assistant_response = ""
    first = True

    for chunk in response:
        if chunk.text:
            content = chunk.text
            if first:
                print(f"[TIME] First Token: {time.perf_counter()-t:.3f}s")
                first = False
            assistant_response += content
            yield content

    print(f"[TIME] Total: {time.perf_counter()-total:.3f}s")

    # Save conversation
    save_turn(
        session_id=session_id,
        user_message=question,
        assistant_message=assistant_response,
    )

    summarize_if_needed(
        session_id=session_id,
        client=None  # Not needed for Gemini
    )
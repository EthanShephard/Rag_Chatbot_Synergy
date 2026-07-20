import json
import os
import re
from collections import defaultdict
from pathlib import Path
import torch
import numpy as np
from dotenv import load_dotenv
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

# CHANGED: Qdrant removed entirely. At ~9k chunks the full embedding matrix
# is well under 50MB, so a local cosine-similarity search over an in-memory
# numpy array is both simpler and faster than a network round-trip to
# Qdrant Cloud — no vector DB to run, pay for, or debug.
load_dotenv()

torch.set_num_threads(1)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "database"
CHUNKS = DATA_DIR / "chunks.json"
EMBEDDINGS = DATA_DIR / "chunk_embeddings.npy"
EMBEDDING_IDS = DATA_DIR / "chunk_ids.npy"

# Must match the model name used in embed_chunks.py.
MODEL_NAME = "BAAI/bge-large-en-v1.5"

# Global variables (lazy init)
chunks = None
chunk_lookup = None
bm25 = None
embedding_model = None
chunk_embeddings = None    # (N, dim) float32, L2-normalized
embedding_id_order = None  # (N,) int64 — chunk_embeddings[i] belongs to chunk id embedding_id_order[i]


def load_chunks():
    try:
        if not CHUNKS.exists():
            raise FileNotFoundError(f"chunks.json not found at: {CHUNKS}")
        with open(CHUNKS, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"[INFO] Loaded {len(data)} chunks")
            return data
    except Exception as e:
        print(f"[ERROR] Failed to load chunks: {e}")
        raise


def load_chunk_embeddings():
    if not EMBEDDINGS.exists() or not EMBEDDING_IDS.exists():
        print(f"[WARNING] Precomputed embeddings not found at {EMBEDDINGS} — "
              f"run `python -m backend.database.embed_chunks` first. "
              f"Semantic search will be disabled; falling back to BM25 only.")
        return None, None

    embeddings = np.load(EMBEDDINGS)
    ids = np.load(EMBEDDING_IDS)
    return embeddings, ids


def initialize_retrieval():
    global chunks, chunk_lookup, bm25, embedding_model, chunk_embeddings, embedding_id_order

    if chunks is not None:
        return

    print("[INFO] Initializing Retrieval System...")

    chunks = load_chunks()

    # FIXED: this was previously keyed on chunk["chunk_id"], which is only
    # a PER-DOCUMENT local index (0, 1, 2, ... resets for every source page
    # / PDF) — 2,285 of 9,184 chunks share chunk_id=0 alone. That collapsed
    # this dict down to ~1,300 entries (later chunks silently overwrote
    # earlier ones with the same chunk_id) and, worse, meant hybrid_search's
    # RRF fusion below was merging scores across completely unrelated
    # chunks that happened to share a chunk_id, and the final lookup could
    # hand back a different chunk than the one actually retrieved.
    # "id" is globally unique across all 9,184 chunks — use that instead.
    chunk_lookup = {chunk["id"]: chunk for chunk in chunks}

    # BM25
    def tokenize(text):
        return re.findall(r"[A-Za-z0-9._-]+", text.lower())

    corpus = [tokenize(chunk["text"]) for chunk in chunks]
    bm25 = BM25Okapi(corpus)

    # Embedding Model — still needed to encode incoming queries at search time.
    device = "cuda" if hasattr(torch, 'cuda') and torch.cuda.is_available() else "cpu"
    print(f"[INFO] Loading embedding model on {device}")
    embedding_model = SentenceTransformer(MODEL_NAME, device=device)

    # CHANGED: load the precomputed chunk-embedding matrix instead of
    # connecting to Qdrant.
    chunk_embeddings, embedding_id_order = load_chunk_embeddings()

    if chunk_embeddings is None:
        print("[WARNING] Retrieval system initialized WITHOUT semantic search — "
              "chat will run on BM25 keyword search only until embeddings are generated.")
    else:
        print(f"[INFO] Loaded {chunk_embeddings.shape[0]} chunk embeddings "
              f"(dim={chunk_embeddings.shape[1]}).")
        print("[INFO] Retrieval system initialized successfully.")


def semantic_search(query, top_k=20):
    if embedding_model is None:
        initialize_retrieval()

    if chunk_embeddings is None:
        print("[WARNING] No chunk embeddings loaded — skipping semantic search, using BM25 only")
        return []

    query_embedding = embedding_model.encode(query, normalize_embeddings=True).astype("float32")

    # CHANGED: cosine similarity via dot product against the local matrix.
    # Both sides are L2-normalized (normalize_embeddings=True on both the
    # query here and the chunks in embed_chunks.py), so dot product is
    # exactly equivalent to cosine similarity — this replaces the old
    # `qdrant.query_points(...)` call.
    scores = chunk_embeddings @ query_embedding  # shape (N,)

    k = min(top_k, len(scores))
    top_indices = np.argpartition(-scores, k - 1)[:k]
    top_indices = top_indices[np.argsort(-scores[top_indices])]

    results = []
    for idx in top_indices:
        chunk_id = int(embedding_id_order[idx])
        chunk = chunk_lookup.get(chunk_id)
        if chunk is None:
            continue
        results.append({"score": float(scores[idx]), **chunk})

    return results


def bm25_search(query, top_k=20):
    if bm25 is None:
        initialize_retrieval()

    def tokenize(text):
        return re.findall(r"[A-Za-z0-9._-]+", text.lower())

    scores = bm25.get_scores(tokenize(query))
    indices = np.argsort(scores)[::-1][:top_k]

    return [
        {"score": float(scores[idx]), **chunks[int(idx)]}
        for idx in indices
    ]


# ==================================================
# Cascading keyword-scoped search
#
# Replaces the LLM-based query-rewrite step for follow-up questions.
# Instead of asking a model to guess a standalone query, this pulls
# keywords straight from the current message + recent conversation
# turns and applies them as a progressive AND-filter over chunks.json
# BEFORE ranking — so a vague follow-up like "show me just the cables"
# inherits the topic scope ("RF", "coaxial") established earlier in the
# conversation, instead of matching "cable" against the whole catalogue
# (including unrelated things like Solar Cables).
# ==================================================

STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "have", "has", "had", "i", "you", "we", "they",
    "it", "he", "she", "this", "that", "these", "those", "and", "or",
    "but", "if", "of", "at", "by", "for", "with", "about", "to", "from",
    "in", "on", "just", "only", "please", "show", "me", "give", "tell",
    "want", "need", "looking", "for", "your", "our", "my", "what", "which",
    "who", "how", "any", "some", "sell", "offer", "offers", "have",
    "available", "product", "products", "list", "please", "can", "could",
}

# Technical spec patterns (e.g. "50 ohm", "6 ghz", "12 mm") are the most
# discriminating tokens a person can give — pull them out as their own
# keyword phrases so they don't get shredded by generic tokenization.
TECH_PATTERN = re.compile(
    r"\b\d+(?:\.\d+)?\s?"
    r"(?:ghz|mhz|khz|hz|ohm|ohms|db|dbi|dbm|mm|cm|inch|in|kg|w|watt|watts|"
    r"v|volt|volts|amp|amps|a)\b",
    re.IGNORECASE,
)


def extract_keywords(text):
    """Pull ordered, deduped keyword candidates out of free text — technical
    spec phrases first (most discriminating), then remaining content words,
    with stopwords and short filler words removed."""
    text_l = text.lower()

    tech_terms = [m.group().strip() for m in TECH_PATTERN.finditer(text_l)]
    remaining = TECH_PATTERN.sub(" ", text_l)

    words = re.findall(r"[a-z0-9][a-z0-9\-]*", remaining)
    content_words = [w for w in words if w not in STOPWORDS and len(w) > 2]

    seen = set()
    ordered = []
    for w in tech_terms + content_words:
        if w not in seen:
            seen.add(w)
            ordered.append(w)
    return ordered


def cascading_keyword_filter(keywords, min_results=6):
    """Progressively AND-filter chunks by keyword. If applying the next
    keyword would narrow the candidate set below min_results, that keyword
    is skipped (treated as over-specific / not present) rather than
    zeroing out the results."""
    if chunks is None:
        initialize_retrieval()

    candidate_idx = list(range(len(chunks)))

    for kw in keywords:
        filtered = [i for i in candidate_idx if kw in chunks[i]["text"].lower()]

        if len(filtered) == 0:
            continue  # keyword not present anywhere in current scope — skip it

        if len(filtered) < min_results and len(candidate_idx) >= min_results:
            continue  # would over-narrow — keep current broader scope instead

        candidate_idx = filtered

    return candidate_idx


def keyword_scoped_search(query, history_text="", top_k=15, min_results=6):
    """Main entry point: scope by cascading keywords (current message +
    recent history), then rank the narrowed candidate set by BM25
    relevance. Falls back to the full hybrid_search if no usable keywords
    are found or nothing in the catalogue matches any of them at all."""
    if chunks is None:
        initialize_retrieval()

    combined_text = f"{query} {history_text}".strip()
    keywords = extract_keywords(combined_text)

    if not keywords:
        return hybrid_search(query, top_k=top_k)

    candidate_idx = cascading_keyword_filter(keywords, min_results=min_results)

    if not candidate_idx:
        return hybrid_search(query, top_k=top_k)

    def tokenize(text):
        return re.findall(r"[A-Za-z0-9._-]+", text.lower())

    scores = bm25.get_scores(tokenize(query))
    ranked = sorted(candidate_idx, key=lambda i: -scores[i])[:top_k]

    return [{"score": float(scores[i]), **chunks[i]} for i in ranked]


def hybrid_search(query, top_k=20, semantic_k=20, bm25_k=20, rrf_k=60):
    if chunks is None:
        initialize_retrieval()

    semantic_results = semantic_search(query, semantic_k)
    bm25_results = bm25_search(query, bm25_k)

    fused_scores = defaultdict(float)

    # FIXED: fuse on "id" (globally unique) instead of "chunk_id" — see the
    # note in initialize_retrieval() for why "chunk_id" collides across
    # documents and corrupts this fusion step.
    for rank, result in enumerate(semantic_results):
        fused_scores[result["id"]] += 1 / (rrf_k + rank + 1)

    for rank, result in enumerate(bm25_results):
        fused_scores[result["id"]] += 1 / (rrf_k + rank + 1)

    ranked = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]

    final_results = []
    for chunk_id, score in ranked:
        chunk = chunk_lookup.get(chunk_id)
        if chunk is None:
            continue
        final_results.append({"rrf_score": score, **chunk})

    return final_results

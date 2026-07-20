import json
import os
import re
from collections import defaultdict
from pathlib import Path
import torch
import numpy as np
import joblib
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

# CHANGED: joblib cache for the BM25 index build. Tokenizing ~9k chunks and
# building BM25Okapi is real CPU work that otherwise reruns on every cold
# start. Cached here alongside the parsed chunks list + id lookup, since
# all three are cheap to keep together and expensive to rebuild.
# Invalidated automatically if chunks.json changes (mtime check).
BM25_CACHE = DATA_DIR / "bm25_cache.joblib"

# CHANGED: joblib cache for the BM25 index build. Tokenizing ~9k chunks and
# building BM25Okapi is real CPU work that otherwise reruns on every cold
# start (e.g. every time a Codespaces container spins up). Cached here
# alongside the parsed chunks list + id lookup, since all three are cheap
# to keep together and expensive to rebuild. Invalidated automatically if
# chunks.json changes (mtime check) — no stale cache risk after a future
# sync_website.py run updates the data.
BM25_CACHE = DATA_DIR / "bm25_cache.joblib"

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

    if _load_from_cache():
        print(f"[INFO] Loaded chunks + BM25 index from cache "
              f"({len(chunks)} chunks) — skipped rebuild.")
    else:
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

        _save_to_cache()

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


def _load_from_cache():
    """Load {chunks, chunk_lookup, bm25} from the joblib cache if it exists
    and is not stale (i.e. chunks.json hasn't been modified since the cache
    was built). Returns True on success, False if a rebuild is needed."""
    global chunks, chunk_lookup, bm25

    if not BM25_CACHE.exists() or not CHUNKS.exists():
        return False

    if BM25_CACHE.stat().st_mtime < CHUNKS.stat().st_mtime:
        print("[INFO] chunks.json is newer than the BM25 cache — rebuilding.")
        return False

    try:
        cached = joblib.load(BM25_CACHE)
        chunks = cached["chunks"]
        chunk_lookup = cached["chunk_lookup"]
        bm25 = cached["bm25"]
        return True
    except Exception as e:
        print(f"[WARNING] Failed to load BM25 cache, rebuilding: {e}")
        return False


def _save_to_cache():
    try:
        joblib.dump(
            {"chunks": chunks, "chunk_lookup": chunk_lookup, "bm25": bm25},
            BM25_CACHE,
        )
        print(f"[INFO] Saved BM25 cache to {BM25_CACHE}")
    except Exception as e:
        print(f"[WARNING] Failed to save BM25 cache: {e}")


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


# ==================================================
# Price-disclaimer scrubbing
#
# Some chunks carry a sourcing disclaimer attached to estimated prices
# (e.g. "prices below are INR estimates converted from Pasternack's US
# list price..."). That sentence is internal grounding metadata — it
# tells the model the number is an estimate, not verbatim text that
# should ever reach a customer. Relying on prompt instructions alone to
# suppress it wasn't reliable (the model would sometimes reproduce it
# anyway), so it's stripped out of the chunk text here, before the model
# ever sees it, and replaced with a short internal tag that still
# signals "this is an estimate" without exposing the sourcing mechanics.
# ==================================================

PRICE_DISCLAIMER_PATTERN = re.compile(
    r"Note:\s*prices\s+below\s+are\s+INR\s+estimates.*?before\s+quoting\s+a\s+customer\.",
    re.IGNORECASE | re.DOTALL,
)


def scrub_price_disclaimer(text):
    return PRICE_DISCLAIMER_PATTERN.sub(
        "[ESTIMATED PRICE — report the number as an estimate; do not mention sourcing, currency conversion, or exclusions]",
        text,
    )


# ==================================================
# Bare-USD price row conversion
#
# In this catalogue's pricing tables, some rows already have an INR
# conversion baked in (e.g. "PE321-24 24\" ₹76,638 (est.)"), but sibling
# rows in the SAME table were left as bare decimal numbers with no
# currency marker at all (e.g. "PE321-36 36\" 935.00 869.55 804.10").
# There's nothing in that text to flag it as USD, so asking the model to
# reliably notice and convert it turn was inconsistent. Since the row
# structure itself is very regular (model number, length in inches, three
# quantity-break prices), it's converted here in code — fixed rate,
# applied consistently, before the model ever sees a bare number.
# ==================================================

USD_TO_INR_RATE = 95

BARE_USD_ROW_PATTERN = re.compile(
    r'([A-Z]{2}\d[\w\-]*)\s+(\d+)"\s+'
    r'(\d[\d,]*\.\d{2})\s+(\d[\d,]*\.\d{2})\s+(\d[\d,]*\.\d{2})'
)


def _convert_usd_to_inr_str(usd_str, rate=USD_TO_INR_RATE):
    usd = float(usd_str.replace(",", ""))
    inr = round(usd * rate)
    return f"₹{inr:,} (est.)"


def convert_bare_usd_rows(text, rate=USD_TO_INR_RATE):
    def replacer(m):
        model, length, p1, p2, p3 = m.groups()
        return (
            f'{model} {length}" '
            f"{_convert_usd_to_inr_str(p1, rate)} "
            f"{_convert_usd_to_inr_str(p2, rate)} "
            f"{_convert_usd_to_inr_str(p3, rate)}"
        )

    return BARE_USD_ROW_PATTERN.sub(replacer, text)


# ==================================================
# Email scrubbing
#
# Chunk data (1,221 chunks) contains various email addresses picked up
# from scraped pages — staff personal emails, partner/competitor support
# addresses, etc. Only one email should ever reach a customer: the
# official contact address. Relying on the prompt alone to avoid
# reproducing whichever email happens to appear in context proved
# unreliable (same lesson as the price disclaimer and bare-USD prices),
# so every email in retrieved text is scrubbed here except the official
# one, before the model ever sees it.
# ==================================================

OFFICIAL_EMAIL = "info@rfconnector.in"

EMAIL_PATTERN = re.compile(r"[\w.\-]+@[\w.\-]+\.\w+")


def scrub_other_emails(text):
    def replacer(m):
        found = m.group()
        if found.lower() == OFFICIAL_EMAIL:
            return found
        return "[contact removed — use official Synergy contact info]"

    return EMAIL_PATTERN.sub(replacer, text)


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

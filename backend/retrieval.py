import json
import os
import re
from collections import defaultdict
from pathlib import Path
import torch
import numpy as np
from dotenv import load_dotenv
from ollama import Client
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, QueryResponse  # Added
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from backend.config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME, VECTOR_NAME, OLLAMA_HOST
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "database"
CHUNKS = DATA_DIR / "chunks.json"

# Global variables (lazy init)
chunks = None
chunk_lookup = None
bm25 = None
embedding_model = None
qdrant = None
ollama_client = None


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


def initialize_retrieval():
    global chunks, chunk_lookup, bm25, embedding_model, qdrant, ollama_client

    if chunks is not None:
        return

    print("[INFO] Initializing Retrieval System...")

    chunks = load_chunks()
    chunk_lookup = {chunk["chunk_id"]: chunk for chunk in chunks}

    # BM25
    def tokenize(text):
        return re.findall(r"[A-Za-z0-9._-]+", text.lower())

    corpus = [tokenize(chunk["text"]) for chunk in chunks]
    bm25 = BM25Okapi(corpus)

    # Embedding Model
    device = "cuda" if hasattr(torch, 'cuda') and torch.cuda.is_available() else "cpu"  # Note: torch needs import
    print(f"[INFO] Loading embedding model on {device}")
    embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5", device=device)

    # Qdrant
    try:
        qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, timeout=120)
        print(f"[INFO] Connected to Qdrant: {COLLECTION_NAME}")
    except Exception as e:
        print(f"[WARNING] Qdrant connection failed: {e}")
        qdrant = None

    ollama_client = Client(host=OLLAMA_HOST)

    if qdrant is None:
        print("[WARNING] Retrieval system initialized WITHOUT Qdrant — "
              "semantic search is disabled, chat will run on BM25 keyword "
              "search only until Qdrant is reachable.")
    else:
        print("[INFO] Retrieval system initialized successfully.")


def get_ollama_client():
    global ollama_client
    if ollama_client is None:
        initialize_retrieval()
    return ollama_client


def semantic_search(query, top_k=20):
    if embedding_model is None:
        initialize_retrieval()

    if qdrant is None:
        # Qdrant failed to connect during initialize_retrieval() (bad
        # QDRANT_URL/QDRANT_API_KEY, network issue, etc). Don't crash the
        # whole chat turn over it — skip the embedding call (no point
        # encoding a query with nowhere to send it) and let hybrid_search()
        # fall back to BM25-only results. This was previously silent: the
        # connection failure was logged once at startup/first-init and then
        # every subsequent call blew up with AttributeError on
        # `qdrant.query_points`. Now every degraded call logs so it's
        # obvious in the server logs, not just discovered via a stack trace.
        print("[WARNING] Qdrant is unavailable — skipping semantic search, using BM25 only")
        return []

    query_embedding = embedding_model.encode(query, normalize_embeddings=True).tolist()

    # FIXED: Modern way to query with named vector
    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,                    # Pass raw vector instead of NamedVector
        using=VECTOR_NAME,                        # Specify vector name with 'using'
        limit=top_k,
        with_payload=True,
    ).points

    return [
        {
            "score": point.score,
            **point.payload,
        }
        for point in results
    ]


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


def hybrid_search(query, top_k=20, semantic_k=20, bm25_k=20, rrf_k=60):
    if chunks is None:
        initialize_retrieval()

    semantic_results = semantic_search(query, semantic_k)
    bm25_results = bm25_search(query, bm25_k)

    fused_scores = defaultdict(float)

    for rank, result in enumerate(semantic_results):
        fused_scores[result["chunk_id"]] += 1 / (rrf_k + rank + 1)

    for rank, result in enumerate(bm25_results):
        fused_scores[result["chunk_id"]] += 1 / (rrf_k + rank + 1)

    ranked = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]

    final_results = []
    for chunk_id, score in ranked:
        chunk = chunk_lookup.get(chunk_id)
        if chunk is None:
            continue
        final_results.append({"rrf_score": score, **chunk})

    return final_results
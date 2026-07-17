"""
Precompute embeddings for every chunk in chunks.json, using the same
SentenceTransformer model retrieval.py uses to encode queries.

This replaces the old "upload to Qdrant" step. Run it once, and again any
time chunks.json changes (re-crawl, re-categorization, edits, etc).

Usage (from the project root, so the `backend` package resolves):
    python -m backend.database.embed_chunks

Output (written next to chunks.json):
    chunk_embeddings.npy  — float32 array, shape (N, dim), L2-normalized
    chunk_ids.npy         — int64 array, shape (N,)
                            chunk_embeddings[i] belongs to the chunk whose
                            "id" field equals chunk_ids[i]
"""

import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent
CHUNKS_PATH = BASE_DIR / "chunks.json"
EMBEDDINGS_PATH = BASE_DIR / "chunk_embeddings.npy"
IDS_PATH = BASE_DIR / "chunk_ids.npy"

# Must match the model name used for query encoding in retrieval.py.
MODEL_NAME = "BAAI/bge-large-en-v1.5"


def main():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    print(f"[INFO] Loaded {len(chunks)} chunks from {CHUNKS_PATH}")

    ids = [c["id"] for c in chunks]
    texts = [c["text"] for c in chunks]

    if len(set(ids)) != len(ids):
        raise ValueError(
            "Duplicate values found in the 'id' field — 'id' must be "
            "globally unique across chunks.json for this to work "
            "(this is the field retrieval.py now uses as its lookup key)."
        )

    print(f"[INFO] Loading embedding model: {MODEL_NAME} (GPU)")
    model = SentenceTransformer(MODEL_NAME, device="cuda")

    print(f"[INFO] Encoding {len(texts)} chunks — this can take a while on CPU...")
    embeddings = model.encode(
        texts,
        normalize_embeddings=True,  # so cosine similarity == plain dot product later
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True,
    ).astype("float32")

    np.save(EMBEDDINGS_PATH, embeddings)
    np.save(IDS_PATH, np.array(ids, dtype="int64"))

    print(
        f"[INFO] Saved {EMBEDDINGS_PATH.name}  shape={embeddings.shape}  "
        f"({EMBEDDINGS_PATH.stat().st_size / 1024 / 1024:.1f} MB)"
    )
    print(f"[INFO] Saved {IDS_PATH.name}")


if __name__ == "__main__":
    main()

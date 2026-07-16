import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# CHANGED: Qdrant settings (QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME,
# VECTOR_NAME) removed — retrieval.py now does local cosine similarity
# against a precomputed embeddings file instead of a Qdrant collection.
# You can also remove those four keys from your .env file; they're no
# longer read anywhere.
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

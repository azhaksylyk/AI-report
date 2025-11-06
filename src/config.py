import os
from dotenv import load_dotenv

load_dotenv()

LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "/path/to/ggml-model.bin")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
FAISS_INDEX_DIR = os.getenv("FAISS_INDEX_DIR", "src/models/faiss_index")

# ingest settings
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from utils import load_docx_files
import config

def build_or_update_faiss(docs, index_dir=config.FAISS_INDEX_DIR):
    # create embeddings object
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)

    # If index exists, load and add; otherwise create
    if os.path.exists(index_dir):
        print("Loading existing FAISS index...")
        db = FAISS.load_local(index_dir, embeddings)
        # filter out documents already present by source_file metadata (simple dedupe)
        existing_sources = {m.get("source_file") for m in db._collection._documents.values()} if hasattr(db, "_collection") else set()
        to_add = [d for d in docs if d.metadata.get("source_file") not in existing_sources]
        if not to_add:
            print("No new documents to add.")
            return db
        print(f"Adding {len(to_add)} new docs")
        db.add_documents(to_add)
    else:
        print("Creating new FAISS index...")
        splitter = RecursiveCharacterTextSplitter(chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
        chunks = []
        for d in docs:
            chunks.extend(splitter.split_documents([d]))
        embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
        db = FAISS.from_documents(chunks, embeddings)
    # save
    db.save_local(index_dir)
    print(f"FAISS index saved to {index_dir}")
    return db

def main():
    data_dir = "data"
    docs = load_docx_files(data_dir)
    print(f"Loaded {len(docs)} documents (before chunking).")
    db = build_or_update_faiss(docs)
    print("Done.")

if __name__ == "__main__":
    main()
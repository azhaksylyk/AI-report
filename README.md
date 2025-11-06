# 🧠 AI Report — Retrieval-Augmented Generation (RAG) System for Daily Operational Reports

This project implements a **local Retrieval-Augmented Generation (RAG)** system that can read, index, and analyze **daily operational reports** (e.g., `.docx` files from company operations).  
It allows natural-language queries like:

> 🗣️ *“How many accidents happened in April 2023?”*  
> 🗣️ *“How long was the UAZ 914 ВС 12 under repair?”*  
> 🗣️ *“Which mobile groups had GPS issues last week?”*

All processing and reasoning are done **locally** — no external APIs required.

---

## ⚙️ Features

- 🗂 **Document ingestion:** Automatically loads `.docx` daily reports (e.g., `01.04.23г.docx`)
- 🔍 **Embeddings:** Local text embeddings via `sentence-transformers/all-MiniLM-L6-v2`
- 🧮 **Vector database:** FAISS index for fast semantic search
- 🦙 **Local LLM inference:** Offline question-answering using `llama-cpp-python`
- ♻️ **Incremental updates:** Add new reports daily without rebuilding the index
- 💬 **Natural-language Q&A:** Ask any question about incidents, repairs, vehicles, etc.
- 🧱 **Modular design:** Clean structure for easy extension and experimentation

---

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/azhaksylyk/AI-report.git
   cd AI-report

2. **Create a virtual environment and install dependencies**
    python -m venv .venv
    source .venv/bin/activate   # on Linux/Mac
    .venv\Scripts\activate      # on Windows
    pip install -r requirements.txt

3. **Prepare environment variables**
    LLAMA_MODEL_PATH=/path/to/ggml-model.bin
    EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
    FAISS_INDEX_DIR=src/models/faiss_index


## 📦 Future Improvements
	•	🧾 Parse structured data (e.g., incidents, repairs) into a SQLite database
	•	🧠 Add reasoning modules for temporal queries (e.g., “in the last 30 days”)
	•	🌍 Add multilingual support (Kazakh/Russian/English)
	•	📊 Build a simple Streamlit dashboard for interactive analysis

⸻

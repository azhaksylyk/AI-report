import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import LlamaCpp
import config

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
    db = FAISS.load_local(config.FAISS_INDEX_DIR, embeddings)
    return db

def make_qa_chain():
    # LlamaCPP settings - requires you to have a ggml model binary and llama-cpp-python installed
    llm = LlamaCpp(model_path=config.LLAMA_MODEL_PATH, n_ctx=2048, n_threads=4, temperature=0.1)
    db = load_vectorstore()
    retriever = db.as_retriever(search_kwargs={"k": 6})
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    return qa

def ask(question):
    qa = make_qa_chain()
    result = qa(question)
    answer = result["result"] if isinstance(result, dict) and "result" in result else result
    sources = result.get("source_documents", []) if isinstance(result, dict) else []
    return answer, sources

if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Ask: ")
    ans, docs = ask(q)
    print("\n=== ANSWER ===\n")
    print(ans)
    print("\n=== SOURCES ===\n")
    for d in docs:
        print(d.metadata.get("source_file"), "---", d.metadata.get("report_date", "no-date"))
import os
from langchain.docstore.document import Document
from langchain.document_loaders import Docx2txtLoader
from datetime import datetime

def load_docx_files(data_dir="data"):
    docs = []
    for fname in sorted(os.listdir(data_dir)):
        if fname.lower().endswith(".docx"):
            path = os.path.join(data_dir, fname)
            loader = Docx2txtLoader(path)
            loaded = loader.load()
            # Add simple metadata: filename, inferred date if present
            meta_date = None
            try:
                # try to infer date from filename like 01.04.23г.docx or 2023-04-01.docx
                only = os.path.splitext(fname)[0]
                # naive attempts:
                for fmt in ("%d.%m.%Y", "%d.%m.%y", "%Y-%m-%d"):
                    try:
                        dt = datetime.strptime(only.replace("г","").strip(), fmt)
                        meta_date = dt.date().isoformat()
                        break
                    except Exception:
                        pass
            except Exception:
                meta_date = None

            for d in loaded:
                md = d.metadata.copy() if hasattr(d, "metadata") else {}
                if meta_date:
                    md["report_date"] = meta_date
                md["source_file"] = fname
                docs.append(Document(page_content=d.page_content, metadata=md))
    return docs
import os, pickle, faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

EMBED = SentenceTransformer("all-MiniLM-L6-v2")
VECTOR_PATH = "app/rag/vector_store"

def ingest_docs(folder="app/knowledge_base"):
    texts = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            from langchain_community.document_loaders import PyPDFLoader
            loader = PyPDFLoader(path)
            texts += loader.load()

        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())

    if not texts:
        print("No documents found.")
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents(texts)

    embeddings = EMBED.encode([c.page_content for c in chunks])

    index = faiss.IndexFlatL2(384)
    index.add(embeddings)

    os.makedirs(VECTOR_PATH, exist_ok=True)
    faiss.write_index(index, f"{VECTOR_PATH}/faiss.index")
    pickle.dump(chunks, open(f"{VECTOR_PATH}/docs.pkl","wb"))

    print("RAG knowledge base built successfully.")

if __name__ == "__main__":
    ingest_docs()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss, os, pickle

EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
VECTOR_PATH = "app/rag/vector_store"

def ingest_pdfs(folder="rag_docs"):
    texts = []
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder, file))
            texts += loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(texts)

    embeddings = EMBEDDING_MODEL.encode([c.page_content for c in chunks])

    index = faiss.IndexFlatL2(384)
    index.add(embeddings)

    os.makedirs(VECTOR_PATH, exist_ok=True)
    faiss.write_index(index, f"{VECTOR_PATH}/faiss.index")
    pickle.dump(chunks, open(f"{VECTOR_PATH}/docs.pkl","wb"))

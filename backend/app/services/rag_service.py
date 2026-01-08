import pickle, faiss, os
from langchain_groq import ChatGroq
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
llm = ChatGroq(model_name="llama3-70b-8192")

VECTOR_PATH = "app/rag/vector_store"

index = faiss.read_index(os.path.join(VECTOR_PATH, "faiss.index"))
docs = pickle.load(open(os.path.join(VECTOR_PATH, "docs.pkl"), "rb"))

def ask_copilot(question: str):
    query_vec = model.encode([question])
    _, I = index.search(query_vec, 3)

    context = "\n".join([docs[i].page_content for i in I[0]])
    prompt = f"Answer strictly based on this policy:\n{context}\n\nQuestion: {question}"

    return llm.invoke(prompt).content

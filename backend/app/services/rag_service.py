import pickle, faiss, os
from langchain_groq import ChatGroq
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize LLM only if API key is available
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = None
if GROQ_API_KEY:
    try:
        llm = ChatGroq(model_name="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
    except Exception as e:
        print(f"Warning: Could not initialize ChatGroq: {e}")

VECTOR_PATH = "app/rag/vector_store"

index = faiss.read_index(os.path.join(VECTOR_PATH, "faiss.index"))
docs = pickle.load(open(os.path.join(VECTOR_PATH, "docs.pkl"), "rb"))

def ask_copilot(question: str):
    if not llm:
        return "Copilot service is not available. Please set GROQ_API_KEY environment variable."
    
    query_vec = model.encode([question])
    _, I = index.search(query_vec, 3)

    context = "\n".join([docs[i].page_content for i in I[0]])
    prompt = f"Answer strictly based on this policy:\n{context}\n\nQuestion: {question}"

    return llm.invoke(prompt).content

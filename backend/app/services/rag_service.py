import faiss, pickle
from sentence_transformers import SentenceTransformer
from langchain_openai import ChatOpenAI

MODEL = SentenceTransformer("all-MiniLM-L6-v2")
llm = ChatOpenAI(model="gpt-4o-mini")

index = faiss.read_index("app/rag/vector_store/faiss.index")
docs = pickle.load(open("app/rag/vector_store/docs.pkl","rb"))

def ask_copilot(question):
    q_vec = MODEL.encode([question])
    D, I = index.search(q_vec, k=3)

    context = "\n".join([docs[i].page_content for i in I[0]])

    prompt = f"""
    You are FedEx Recovery Copilot.
    Answer strictly based on this SOP context:

    {context}

    Question: {question}
    """

    return llm.invoke(prompt).content

import faiss, pickle, os
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
EMBED = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("backend/app/rag/vector_store/faiss.index")
docs = pickle.load(open("backend/app/rag/vector_store/docs.pkl","rb"))

def ask_copilot(question: str):
    q = EMBED.encode([question])
    _, I = index.search(q, k=3)
    context = "\n".join([docs[i].page_content for i in I[0]])

    prompt = f"""
You are FedEx Recovery Copilot.
Answer strictly using this SOP context:

{context}

Question: {question}
"""

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role":"user","content":prompt}]
    )

    return completion.choices[0].message.content

from fastapi import APIRouter
from app.services.rag_service import ask_copilot

router = APIRouter()

@router.post("/copilot")
def copilot(question: str):
    return {"answer": ask_copilot(question)}

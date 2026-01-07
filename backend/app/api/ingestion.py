from fastapi import APIRouter
from app.core.database import SessionLocal
from app.models.case import OverdueCase

router = APIRouter()

@router.post("/ingest")
def ingest(case: dict):
    db = SessionLocal()
    obj = OverdueCase(**case)
    db.add(obj)
    db.commit()
    return {"status":"inserted"}

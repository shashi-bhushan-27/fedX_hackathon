from fastapi import APIRouter
from app.core.database import SessionLocal, engine
from app.models.case import OverdueCase

router = APIRouter()

@router.post("/ingest")
def ingest(case: dict):
    print("USING DB:", engine.url)      # <---- ADD THIS
    db = SessionLocal()
    obj = OverdueCase(**case)
    db.add(obj)
    db.commit()
    db.close()
    return {"status":"inserted"}

from fastapi import APIRouter
from uuid import uuid4
from app.core.database import SessionLocal, engine
from app.models.case import OverdueCase

router = APIRouter()

@router.post("/ingest")
def ingest(case: dict):
    print("USING DB:", engine.url)
    db = SessionLocal()
    try:
        obj = OverdueCase(
            case_id=case.get("case_id") or str(uuid4())[:8],
            customer_name=case.get("customer_name", "Unknown"),
            amount=float(case.get("amount", 0) or 0),
            status=case.get("status", "OPEN"),
            region=case.get("region", ""),
            assigned_dca=case.get("assigned_dca"),
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return {"status": "inserted", "id": obj.id, "case_id": obj.case_id}
    finally:
        db.close()

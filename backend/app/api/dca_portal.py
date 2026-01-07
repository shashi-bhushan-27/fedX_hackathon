from fastapi import APIRouter
from app.core.database import SessionLocal
from app.models.case import OverdueCase

router = APIRouter()

@router.get("/dca_portal/{dca_id}")
def get_cases(dca_id:str):
    db = SessionLocal()
    return db.query(OverdueCase).filter(OverdueCase.assigned_dca==dca_id).all()

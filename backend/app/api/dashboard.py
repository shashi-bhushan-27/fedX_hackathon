from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.case import OverdueCase
from app.models.assignment import CaseAssignment

router = APIRouter()

@router.get("/metrics")
def metrics():
    db: Session = SessionLocal()
    total_cases = db.query(OverdueCase).count()
    recovered = db.query(OverdueCase).filter(OverdueCase.status=="CLOSED").count()
    open_cases = total_cases - recovered
    return {
        "total_cases": total_cases,
        "recovered": recovered,
        "open_cases": open_cases
    }

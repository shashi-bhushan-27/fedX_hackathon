from fastapi import APIRouter
from app.services.allocation_service import auto_assign

router = APIRouter()

@router.post("/allocate")
def allocate(case: dict):
    return auto_assign(case)

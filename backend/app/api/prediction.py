from fastapi import APIRouter
from app.services.ml_service import predict_case

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    return predict_case(data)

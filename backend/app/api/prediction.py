from fastapi import APIRouter
from app.services.ml_service import predict_case

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    prob, risk = predict_case(list(data.values()))
    return {"recovery_probability":prob, "aging_risk":risk}

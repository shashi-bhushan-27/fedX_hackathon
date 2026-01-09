import joblib
import pandas as pd

FEATURE_ORDER = [
    "amount",
    "due_days",
    "invoice_count",
    "credit_score",
    "previous_collections",
    "historical_default_rate",
    "region",
    "specialization",
    "debt_to_credit_ratio",
    "invoice_intensity"
]

recovery = joblib.load("/workspaces/fedX_hackathon/backend/app/ml/recovery_model.pkl")
aging = joblib.load("/workspaces/fedX_hackathon/backend/app/ml/aging_model.pkl")
speed = joblib.load("/workspaces/fedX_hackathon/backend/app/ml/speed_model.pkl")

def predict_case(payload):
    if isinstance(payload, list):
        payload = dict(zip(FEATURE_ORDER, payload))

    X = pd.DataFrame([[payload[f] for f in FEATURE_ORDER]], columns=FEATURE_ORDER)

    return {
        "recovery_probability": float(recovery.predict_proba(X)[0][1]),
        "aging_risk": int(aging.predict_proba(X)[0][1] > 0.5),
        "closure_speed_days": int(speed.predict(X)[0])
    }

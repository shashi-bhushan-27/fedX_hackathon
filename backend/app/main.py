from fastapi import FastAPI

from app.api import ingestion, prediction, allocation, dashboard, dca_portal, copilot

app = FastAPI(title="FLEX-DCA AI Platform")
from dotenv import load_dotenv
load_dotenv()

app.include_router(ingestion.router, prefix="/api")
app.include_router(prediction.router, prefix="/api")
app.include_router(allocation.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")
app.include_router(dca_portal.router, prefix="/api")
app.include_router(copilot.router, prefix="/api")

@app.get("/")
def root():
    return {"status":"FLEX-DCA backend is running"}

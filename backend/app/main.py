from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api import ingestion, prediction, allocation, dashboard, dca_portal, copilot
from app.core.database import Base, engine
# Register models so SQLAlchemy knows about them before create_all
from app.models import case, assignment, customer, dca, history  # noqa: F401

app = FastAPI(title="FLEX-DCA AI Platform")
load_dotenv()

# Allow frontend dev server to call the API from a different origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://supreme-happiness-5g4pv6976x6v2vppq-5173.app.github.dev",
        "https://supreme-happiness-5g4pv6976x6v2vppq-5174.app.github.dev",
        "http://supreme-happiness-5g4pv6976x6v2vppq-5173.app.github.dev",
        "http://supreme-happiness-5g4pv6976x6v2vppq-5174.app.github.dev",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Ensure tables exist for local development without requiring a migration step
Base.metadata.create_all(bind=engine)

app.include_router(ingestion.router, prefix="/api")
app.include_router(prediction.router, prefix="/api")
app.include_router(allocation.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")
app.include_router(dca_portal.router, prefix="/api")
app.include_router(copilot.router, prefix="/api")

@app.get("/")
def root():
    return {"status":"FLEX-DCA backend is running"}

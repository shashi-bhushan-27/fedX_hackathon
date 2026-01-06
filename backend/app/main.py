from app.api import copilot
app.include_router(copilot.router, prefix="/api")

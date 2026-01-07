from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class CaseAssignment(Base):
    __tablename__ = "case_assignments"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(String)
    dca_id = Column(String)
    score = Column(Float)

from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class OverdueCase(Base):
    __tablename__ = "overdue_cases"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(String, unique=True, index=True)
    customer_name = Column(String)
    amount = Column(Float)
    status = Column(String)   # OPEN / CLOSED
    region = Column(String)
    assigned_dca = Column(String)

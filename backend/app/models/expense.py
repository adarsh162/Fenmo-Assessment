import uuid
from datetime import datetime
from sqlalchemy import Column, String, Numeric, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    category = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    expense_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Idempotency key: prevents duplicate entries if client retries
    request_id = Column(String, unique=True, nullable=False, index=True)
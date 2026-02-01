from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.expense import ExpenseResponse
from app.services.expense import expense_service

router = APIRouter()

@router.get("/", response_model=List[ExpenseResponse])
def get_expenses(
    category: Optional[str] = Query(None),
    sort: str = Query("date_desc"),
    db: Session = Depends(get_db)
):
    return expense_service.list_expenses(db, category=category, sort=sort)

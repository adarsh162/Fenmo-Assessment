from fastapi import APIRouter, Depends, Query, Response
from typing import List, Optional
from sqlalchemy.orm import Session
from starlette import status

from app.api.deps import get_db
from app.schemas.expense import ExpenseResponse, ExpenseCreate
from app.services.expense import expense_service

router = APIRouter()

@router.get("/", response_model=List[ExpenseResponse])
def get_expenses(
    category: Optional[str] = Query(None),
    sort: str = Query("date_desc"),
    db: Session = Depends(get_db)
):
    return expense_service.list_expenses(db, category=category, sort=sort)

@router.post("/", response_model=ExpenseResponse, status_code=201)
def create_expense(
    expense_in: ExpenseCreate,
    response: Response,
    db: Session = Depends(get_db)
):
    result, created = expense_service.create_new_expense(db, expense_in)
    if not created:
        response.status_code = status.HTTP_200_OK
    return result

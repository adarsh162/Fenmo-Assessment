from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.crud import crud_expense
from app.schemas.expense import ExpenseCreate

class ExpenseService:
    def create_new_expense(self, db: Session, expense_in: ExpenseCreate):
        # Check if already exists (Idempotency check before trying insert)
        existing = crud_expense.get_by_request_id(db, expense_in.request_id)
        if existing:
            return existing, False

        try:
            return crud_expense.create_expense(db, expense_in), True
        except IntegrityError:
            db.rollback()
            return crud_expense.get_by_request_id(db, expense_in.request_id)

    def list_expenses(self, db: Session, category: str = None, sort: str = "date_desc"):
        sort_desc = True if sort == "date_desc" else False
        return crud_expense.get_expenses(db, category=category, sort_desc=sort_desc)

expense_service = ExpenseService()
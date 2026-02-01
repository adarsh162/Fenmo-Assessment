from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate

def get_expenses(db: Session, category: str = None, sort_desc: bool = True):
    query = db.query(Expense)
    if category:
        query = query.filter(Expense.category == category)

    order = Expense.expense_date.desc() if sort_desc else Expense.expense_date.asc()
    return query.order_by(order).all()

def create_expense(db: Session, obj_in: ExpenseCreate):
    db_obj = Expense(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_by_request_id(db: Session, request_id: str):
    return db.query(Expense).filter(Expense.request_id == request_id).first()

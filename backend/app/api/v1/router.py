from app.api.v1 import expense
from fastapi import APIRouter

router = APIRouter()
router.include_router(expense.router, prefix="/expenses", tags=["expenses"])

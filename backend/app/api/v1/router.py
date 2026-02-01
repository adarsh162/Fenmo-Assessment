from app.api.v1 import items, expense
from fastapi import APIRouter

router = APIRouter()
router.include_router(items.router, prefix="", tags=["items"])
router.include_router(expense.router, prefix="/expenses", tags=["expenses"])

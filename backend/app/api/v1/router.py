from app.api.v1 import items, expenses
from fastapi import APIRouter

router = APIRouter()
router.include_router(items.router, prefix="", tags=["items"])
router.include_router(expenses.router, prefix="/expenses", tags=["expenses"])

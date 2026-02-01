from app.api.v1 import items
from fastapi import APIRouter

router = APIRouter()
router.include_router(items.router, prefix="", tags=["items"])

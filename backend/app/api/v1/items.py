from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.items import ItemResponse, ItemCreate
from app.services.items import ItemService

router = APIRouter()

@router.get("/items", response_model=list[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    service = ItemService(db)
    items = service.get_items()
    return items
@router.post("/items", response_model=ItemResponse)
def create_item(item_in: ItemCreate, db: Session = Depends(get_db)):
    service = ItemService(db)
    item = service.create_item(item_in)
    return item

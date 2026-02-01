from app.crud.crud_item import item as crud_item
from sqlalchemy.orm import Session
from app.schemas.items import ItemCreate
from app.models.items import Item
class ItemService:
    def __init__(self, db: Session):
        self.db = db

    def get_items(self) -> list[Item]:
        return crud_item.get(self.db)

    def create_item(self, item_in: ItemCreate) -> Item:
        return crud_item.create(self.db, obj_in=item_in)

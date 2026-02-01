from app.crud.base import CRUDBase
from app.models.items import Item
from app.schemas.items import ItemCreate

class CRUDItem(CRUDBase[Item, ItemCreate]):
    # You can add table-specific methods here
    # Example: Filter items by user_id
    pass

item = CRUDItem(Item)

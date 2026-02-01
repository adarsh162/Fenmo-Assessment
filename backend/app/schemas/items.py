from pydantic import BaseModel, ConfigDict
from typing import Optional

# The Shared Fields
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    title: str
    description: Optional[str]

    # This allows Pydantic to read SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)

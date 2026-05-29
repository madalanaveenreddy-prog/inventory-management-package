
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)

class ItemResponse(ItemBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)

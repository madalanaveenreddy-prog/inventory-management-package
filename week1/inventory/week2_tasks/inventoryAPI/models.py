from pydantic import BaseModel, Field
from typing import Literal

# Schema for creating a product
class ProductCreateSchema(BaseModel):
    id: int = Field(..., description="Unique ID for the product")
    name: str = Field(..., min_length=2, description="Name of the product")
    base_price: float = Field(..., gt=0, description="Price must be greater than 0")
    product_type: Literal["physical", "digital"] = Field(..., description="Type of product")
class ProductUpdateSchema(BaseModel):
    name: str = Field(..., min_length=2, description="Updated name of the product")
    base_price: float = Field(..., gt=0, description="Updated price must be greater than 0")
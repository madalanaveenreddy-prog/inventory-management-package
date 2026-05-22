from pydantic import BaseModel, field_validator

class ItemModel(BaseModel):
    item_name: str
    price: float
    quantity: int

    @field_validator("price", "quantity")
    @classmethod
    def check_positive(cls, value):
        if value < 0:
            raise ValueError("Value cannot be negative!")
        return value

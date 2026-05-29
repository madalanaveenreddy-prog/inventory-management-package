
from sqlalchemy import Column, Integer, String, Float
from database import Base

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)


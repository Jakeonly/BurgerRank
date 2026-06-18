from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str
    description: str
    year: int

class ProductCreate(ProductBase):
    restaurant_id: UUID

class ProductResponse(ProductBase):
    id: UUID
    restaurant_id: UUID
    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None
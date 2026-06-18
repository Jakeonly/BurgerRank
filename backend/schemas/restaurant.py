from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class RestaurantBase(BaseModel):
    name: str
    description: Optional[str] = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantResponse(RestaurantBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None





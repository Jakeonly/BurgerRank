
from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    user_id: UUID
    product_id: UUID

class ReviewResponse(ReviewBase):
    id: UUID
    user_id: UUID
    product_id: UUID
    creation_date: datetime
    model_config = ConfigDict(from_attributes=True)

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None
from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class ImageBase(BaseModel):
    link: str

class ImageCreate(ImageBase):
    pass

class ImageResponse(ImageBase):
    id: UUID
    creation_date: datetime
    model_config = ConfigDict(from_attributes=True)

class ImageUpdate(BaseModel):
    link: Optional[str] = None
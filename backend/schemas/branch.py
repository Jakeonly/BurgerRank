from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class BranchBase(BaseModel):
    address: str
    
class BranchCreate(BranchBase):
    restaurant_id: UUID

class BranchResponse(BranchBase):
    id: UUID
    restaurant_id: UUID
    model_config = ConfigDict(from_attributes=True)

class BranchUpdate(BaseModel):
    address: Optional[str] = None



    
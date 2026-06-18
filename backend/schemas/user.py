from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
	username: str
	name: str
	email: EmailStr

class UserCreate(UserBase):
	password: str


class UserResponse(UserBase):
	id: UUID
	is_active: bool
	is_admin: bool

	model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
	username: Optional[str] = None
	name: Optional[str] = None
	email: Optional[EmailStr] = None
	password: Optional[str] = None



from models.review import Review
from typing import List
from sqlalchemy import Uuid, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid

from db.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password_hash: Mapped[str] = mapped_column(String(300), nullable=False)
    is_active: Mapped[bool]
    is_admin: Mapped[bool]
    #Relationship with Reviews: User 1:N Reviews
    reviews: Mapped[List["Review"]] = relationship(back_populates="user")











    

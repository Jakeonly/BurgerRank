from typing import List
import uuid
from sqlalchemy import Uuid, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base
from models.product import Product
from models.branch import Branch

class Restaurant(Base):
    __tablename__ = "restaurants"
    #Attributes
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    #ORM
    #Relationship with Product: Restaurant 1:N Product
    products: Mapped[List["Product"]] = relationship(back_populates="restaurant", cascade="all, delete-orphan")
    #Relationship with Branch: Restaurant 1:N Branch
    branches: Mapped[List["Branch"]] = relationship(back_populates="restaurant", cascade="all, delete-orphan")
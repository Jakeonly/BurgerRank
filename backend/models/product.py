from typing import List
from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Uuid, String, Integer, ForeignKey
import uuid
from models.review import Review

class Product(Base):
    __tablename__ = "products"
    #Attributes
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    year: Mapped[int] = mapped_column(Integer(), nullable=False)
    #ORM
    #Foreign Key to Restaurant
    restaurant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False)
    #Relationships
    reviews: Mapped[List["Review"]] = relationship()
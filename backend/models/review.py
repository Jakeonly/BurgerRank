import uuid
from datetime import datetime
from db.database import Base
from sqlalchemy import Uuid, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.product import Product
from models.user import User

class Review(Base):
    __tablename__ = "reviews"
    #Attributes
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    rating: Mapped[int] = mapped_column(nullable=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False ,server_default=func.now())
    comment: Mapped[str] = mapped_column(String(500), nullable=True)
    #ORM
    #Relationship with User: Reviews N:1 User 
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="reviews")
    #Relationship with Product: Reviews N:1 Product
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="reviews")

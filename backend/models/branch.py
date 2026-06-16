import uuid
from sqlalchemy import Uuid, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base
from models.restaurant import Restaurant

class Branch(Base):
    __tablename__ = "branches"
    #Attributes
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    address: Mapped[str] = mapped_column(String(80), nullable=False)
    #ORM
    #Relationship with Restaurant: Branch N:1 Restaurant
    restaurant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False)
    restaurant: Mapped["Restaurant"] = relationship(back_populates="branches")
from sqlalchemy import Uuid, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base
from datetime import datetime
import uuid

class Image(Base):
    __tablename__ = "images"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    link: Mapped[str] = mapped_column(String(1000), nullable=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False ,server_default=func.now())
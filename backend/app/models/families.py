import uuid
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User

class Family(Base):
    __tablename__ = "families"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String, nullable=False)
    invite_code: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    
    users: Mapped[list["User"]] = relationship("User", back_populates="family", cascade="all, delete-orphan")

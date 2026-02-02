import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User
    from .families import Family

class Event(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    start_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    # Relationships
    family_id: Mapped[str] = mapped_column(String, ForeignKey("families.id"), nullable=False, index=True)
    creator_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)

    # Back Reference (we usually add these so we can say event.family.name)
    family: Mapped["Family"] = relationship("Family")
    creator: Mapped["User"] = relationship("User")


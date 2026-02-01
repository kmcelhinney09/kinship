import uuid
from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .families import Family

class User(Base):
    __tablename__ = "users"
    
    # UUID is used for the primary key
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Email is used for login and is unique
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    
    # Hashed password is used for login
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    
    # Role is used to determine the user's role
    role: Mapped[str] = mapped_column(String, nullable=False, default="member")

    # Links to the Family model
    family_id: Mapped[str] = mapped_column(String, ForeignKey("families.id"), nullable=False, index=True)

    # Token balance for chore gamification
    current_token: Mapped[int] = mapped_column(Integer, default=0)

    # Relationship to Family
    family: Mapped["Family"] = relationship("Family", back_populates="users")
import uuid
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    # UUID is used for the primary key and lambda is used to generate a new UUID for each new user
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    # Email is used for login and is unique so not two users can have the same email and nullable=False means that the email cannot be empty
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # Hashed password is used for login and is nullable=False means that the password cannot be empty
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    # Role is used to determine the user's role and is nullable=False means that the role cannot be empty
    role: Mapped[str] = mapped_column(String, nullable=False)

    # Links to the Family model
    family_id: Mapped[str] = mapped_column(String, ForeignKey("families.id"), nullable=False, index=True)

    # Token balance for chore gamification
    current_token: Mapped[int] = mapped_column(Integer, default=0)

    # We use quotes "Family" so Python doesn't need to import the Family class yet
    family: Mapped["Family"] = relationship("Family", back_populates="users")
    
    
import uuid
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    # UUID is used for the primary key and lambda is used to generate a new UUID for each new user
    id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    # Links to the Family model
    family_id = Column(String, ForeignKey("families.id"), nullable=False)

    # Token balance for chore gamification
    current_token = Column(Integer, default=0)

    # We use quotes "Family" so Python doesn't need to import the Family class yet
    family = relationship("Family", back_populates="users")
    
    
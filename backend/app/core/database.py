from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import Base here so other files can just import from database if they want, 
# or strictly usage models.base. But typically database.py constructs engine/session.
# We don't necessarily need to import Base here unless we want to bind it, 
# but Base is bound to metadata.
# We will just setup the engine and session here.

SQLALCHEMY_DATABASE_URL = "sqlite:///./kinship.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

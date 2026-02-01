from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core import security
from app.core.database import get_db
from app.models.users import User
from app.schemas.user import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    try:
        payload = jwt.decode(
            token, security.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenData(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    # Payload has 'sub' which is the subject (email in our case, or id)
    # The security.create_access_token uses `str(subject)` as sub.
    # We should define what we use as subject. Let's use email for now or ID.
    # Ideally ID is more stable.
    # Let's assume we store email as sub in token for simplicity or ID.
    # In auth.py we will decide.
    
    # Adjusting TokenData schema or decoding here:
    # payload: {'sub': 'user_email', 'exp': ...}
    
    user_identifier = payload.get("sub")
    if not user_identifier:
        raise HTTPException(status_code=403, detail="Invalid token subject")
        
    user = db.query(User).filter(User.email == user_identifier).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return user

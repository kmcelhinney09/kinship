from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.core import security
from app.core.database import get_db
from app.models.users import User
from app.models.families import Family
from app.schemas.user import UserCreate, User as UserSchema, Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = security.create_access_token(subject=user.email)
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

@router.post("/register", response_model=UserSchema)
def register_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
) -> Any:
    """
    Create new user and family (or join existing)
    """
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this user name already exists in the system",
        )
        
    family = None
    if user_in.invite_code:
        family = db.query(Family).filter(Family.invite_code == user_in.invite_code).first()
        if not family:
            raise HTTPException(status_code=404, detail="Family not found with this invite code")
    elif user_in.family_name:
        # Create new family
        # Simple invite code generation (in real app, use something robust)
        import random, string
        invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        family = Family(name=user_in.family_name, invite_code=invite_code)
        db.add(family)
        db.commit()
        db.refresh(family)
    else:
        raise HTTPException(status_code=400, detail="Must provide family_name or invite_code")

    user = User(
        email=user_in.email,
        hashed_password=security.get_password_hash(user_in.password),
        family_id=family.id,
        role="admin" if not user_in.invite_code else "member" # First user is admin
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

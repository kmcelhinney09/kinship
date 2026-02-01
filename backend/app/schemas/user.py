from pydantic import BaseModel, EmailStr
from typing import Optional

class FamilyBase(BaseModel):
    name: str

class FamilyCreate(FamilyBase):
    pass

class Family(FamilyBase):
    id: str
    invite_code: Optional[str] = None
    
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str
    family_name: Optional[str] = None # For creating a new family
    invite_code: Optional[str] = None # For joining an existing family

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: str
    family_id: str
    role: str
    current_token: int = 0
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

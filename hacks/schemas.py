from datetime import datetime

from pydantic import BaseModel, EmailStr
from pydantic.class_validators import Optional


class Jobs(BaseModel):
    name: str
    location: str
    status: bool = True
    comments: Optional[str]
    positions: Optional[str]
    link: Optional[str]

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Token_data(BaseModel):
    id: Optional[str] = None

from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(UserBase):
    user_id: int
    register_date: datetime
    is_active: bool
    status: str
    role: str

    class Config:
        orm_mode = True
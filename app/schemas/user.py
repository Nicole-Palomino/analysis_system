from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    status: str
    role: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    user_id: int
    register_date: datetime

    class Config:
        orm_mode = True
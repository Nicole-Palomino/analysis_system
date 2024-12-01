from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "tb_users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    register_date = Column(Date)
    status = Column(String, default="inactive")  
    role = Column(String, default="user")
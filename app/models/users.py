from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "tb_users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(250), unique=True, index=True, nullable=False)
    password = Column(String(350), nullable=False)
    register_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    status = Column(String(20), default="inactive", nullable=False)
    role = Column(String(20), default="user", nullable=False)
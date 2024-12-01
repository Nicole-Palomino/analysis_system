import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_EMAIL = os.getenv("SMTP_EMAIL", "youemail@gmail.com")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "password")

settings = Settings()
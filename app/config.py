from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_EMAIL: str
    SMTP_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import get_db

import bcrypt

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Football Analysis API!"}
from fastapi import FastAPI
from app.models import users
from app.db.database import create_db_and_tables

app = FastAPI(
    title="API de Análisis de Fútbol",
    description="Registro, autenticación y manejo seguro de usuarios",
    version="1.0.0"
)

app.include_router(users.router)

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Football Analysis API!"}
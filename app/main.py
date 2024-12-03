from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.routers import users

app = FastAPI(
    title="API for ScoreXpert with FastAPI",
    description="Registration, authentication and secure user management.",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",  # Frontend en local
    "https://mi-frontend.com",  # Un dominio específico
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "API en funcionamiento. Visita /docs para la documentación."}
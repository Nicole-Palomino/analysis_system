from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API for ScoreXpert with FastAPI",
    description="Registration, authentication and secure user management.",
    version="1.0.0",
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API en funcionamiento. Visita /docs para la documentación."}
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import Base, get_db, engine

# Usar TestClient para simular peticiones a la API
client = TestClient(app)

# Crear la base de datos para pruebas
@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Crea las tablas
    yield
    Base.metadata.drop_all(bind=engine)  # Elimina las tablas al finalizar


def test_register_user():
    response = client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    assert response.json()["msg"] == "User registered. Please verify your email"


def test_login_without_verification():
    response = client.post(
        "/login",
        json={
            "email": "testuser@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email not verified"

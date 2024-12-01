from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

# Cargar las variables de entorno
load_dotenv()

# Obtener la URL de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("No se ha encontrado la URL de la base de datos en el archivo .env")

# Crear el motor de la base de datos con la URL de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear la sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base declarativa para los modelos
Base = declarative_base()

# Función para obtener la base de datos en cada solicitud
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
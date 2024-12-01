from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.users import User
from app.schemas.user import UserCreate, UserOut
from app.utils.token import create_access_token, verify_access_token
from app.utils.email import send_verification_email
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    token = create_access_token({"sub": user.email})
    send_verification_email(user.email, token)

    return db_user

@router.get("/verify")
def verify_email(token: str, db: Session = Depends(get_db)):
    try:
        payload = verify_access_token(token)
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=400, detail="Token inválido")

        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        user.is_active = True
        user.status = "active"
        db.commit()
        return {"message": "Correo verificado con éxito"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al verificar el token") from e

@router.post("/resend-verification")
def resend_verification(email: str, db: Session = Depends(get_db)):
    # Verifica si el usuario ya está registrado
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if user.is_active:
        raise HTTPException(status_code=400, detail="El usuario ya está verificado")

    # Genera un nuevo token de verificación
    new_token = create_access_token(data={"sub": user.email})

    # Envía el nuevo token por correo
    send_verification_email(user.email, new_token)  # Función para enviar correo con el token

    return {"message": "Nuevo token de verificación enviado al correo electrónico"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Correo no verificado")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
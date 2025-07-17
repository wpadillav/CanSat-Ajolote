from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import timedelta
from db.users import get_user_by_username, insert_user
from auth.jwt_handler import create_access_token, create_refresh_token, verify_token
from exceptions.user_exceptions import UserAlreadyExistsError
from models.user import User

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
async def register(user: User):
    hashed_password = pwd_context.hash(user.password)
    user_data = {
        "username": user.username,
        "hashed_password": hashed_password
    }

    try:
        insert_user(user_data)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": f"Usuario '{user.username}' creado correctamente."}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(form_data.username)

    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos.")

    access_token = create_access_token(data={"sub": user["username"]})
    refresh_token = create_refresh_token(data={"sub": user["username"]})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh")
async def refresh_token(request: Request):
    body = await request.json()
    token = body.get("refresh_token")
    if not token:
        raise HTTPException(status_code=400, detail="Falta refresh_token")

    username = verify_token(token, scope="refresh_token")
    if not username:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")

    new_access_token = create_access_token(data={"sub": username})
    return {"access_token": new_access_token, "token_type": "bearer"}

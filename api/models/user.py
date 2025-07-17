from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str  # Solo para entrada, no se guarda sin cifrar

class UserInDB(User):
    hashed_password: str

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str  # Solo se usa al momento de crear/iniciar sesión

class UserInDB(BaseModel):
    username: str
    hashed_password: str

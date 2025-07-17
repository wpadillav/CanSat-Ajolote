from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from config import MONGO_LOCAL_URI, MONGO_ATLAS_URI
from exceptions.user_exceptions import UserAlreadyExistsError

# === Conexión a MongoDB local ===
client_local = MongoClient(MONGO_LOCAL_URI)
db_local = client_local["Cansat"]
users_local = db_local["users"]

# === Conexión a MongoDB Atlas ===
client_atlas = MongoClient(MONGO_ATLAS_URI)
db_atlas = client_atlas["Cansat"]
users_atlas = db_atlas["users"]

# === Crear índices únicos en 'username' ===
users_local.create_index("username", unique=True)
users_atlas.create_index("username", unique=True)

# === Insertar usuario en ambas bases ===
def insert_user(user: dict):
    try:
        users_local.insert_one(user)
        users_atlas.insert_one(user)
    except DuplicateKeyError:
        raise UserAlreadyExistsError(user["username"])

# === Buscar usuario (por nombre de usuario) ===
def get_user_by_username(username: str):
    user = users_local.find_one({"username": username})
    if user:
        return user
    return users_atlas.find_one({"username": username})

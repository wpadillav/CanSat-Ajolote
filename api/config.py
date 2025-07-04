import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# === MongoDB Atlas (nube) ===
MONGO_ATLAS_URI = os.getenv("MONGO_ATLAS_URI")

# === MongoDB Local ===
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Construcción de URI de conexión local con autenticación
MONGO_LOCAL_URI = (
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"
)

# === Entorno de ejecución ===
# development (por defecto) o production
ENV = os.getenv("ENV", "development").lower()
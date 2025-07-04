from pymongo import MongoClient
from config import MONGO_ATLAS_URI, MONGO_DB, MONGO_COLLECTION

# Establece la conexión al clúster de MongoDB Atlas
client_atlas = MongoClient(MONGO_ATLAS_URI)

# Selecciona la base de datos especificada en el archivo .env
db_atlas = client_atlas[MONGO_DB]

# Obtiene la colección de telemetría dentro de la base de datos
telemetry_atlas = db_atlas[MONGO_COLLECTION]

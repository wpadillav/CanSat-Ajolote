from pymongo import MongoClient
from config import MONGO_LOCAL_URI, MONGO_DB, MONGO_COLLECTION

# Establece la conexión con la base de datos MongoDB local
client_local = MongoClient(MONGO_LOCAL_URI)

# Selecciona la base de datos definida en la configuración
db_local = client_local[MONGO_DB]

# Obtiene la colección de telemetría de la base de datos local
telemetry_local = db_local[MONGO_COLLECTION]

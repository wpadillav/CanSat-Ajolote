import os
import psutil
import pymongo
import socket
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

# Obtener las variables necesarias
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB = os.getenv("MONGO_DB", "Pruebas")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "datosequipos")

# Validación de variables críticas
if not all([MONGO_USER, MONGO_PASSWORD, MONGO_HOST]):
    raise ValueError("Faltan variables críticas de conexión en el archivo .env")

# Conexión a MongoDB
mongo_uri = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/admin"
cliente = pymongo.MongoClient(mongo_uri)

# Base de datos y colección
db = cliente[MONGO_DB]
coleccion = db[MONGO_COLLECTION]

# Recolectar información del sistema
def obtener_datos_maquina():
    datos = {}
    
    datos["hostname"] = socket.gethostname()
    datos["num_cores"] = psutil.cpu_count(logical=True)
    
    memoria = psutil.virtual_memory()
    datos["memoria_total_gb"] = round(memoria.total / (1024 ** 3), 2)
    
    return datos

# Insertar en MongoDB
def guardar_en_mongodb(datos):
    try:
        resultado = coleccion.insert_one(datos)
        print(f"Datos insertados con _id: {resultado.inserted_id}")
    except Exception as e:
        print(f"Error al insertar en MongoDB: {e}")

if __name__ == "__main__":
    datos_maquina = obtener_datos_maquina()
    print("Datos recolectados:", datos_maquina)
    guardar_en_mongodb(datos_maquina)

import os
import psutil
import pymongo
import socket
import time
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env en el directorio padre
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

# Obtener las variables necesarias
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB = os.getenv("MONGO_DB", "Pruebas")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "datosequipos")

# Verificar que las variables críticas estén definidas
if not all([MONGO_USER, MONGO_PASSWORD, MONGO_HOST]):
    raise ValueError("Faltan variables de entorno críticas para la conexión a MongoDB.")

# Conexión a MongoDB
mongo_uri = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/admin"
cliente = pymongo.MongoClient(mongo_uri)

# Base de datos y colección
db = cliente[MONGO_DB]
coleccion = db[MONGO_COLLECTION]

# Hostname para identificar la máquina
hostname = socket.gethostname()

def monitorear_uso_cpu_memoria_red():
    print(f"Iniciando monitoreo de CPU, memoria y red por 10 segundos...")

    # Capturar estado inicial de red
    net_anterior = psutil.net_io_counters()

    for i in range(10):
        inicio = time.time()

        # Uso de CPU y memoria
        uso_cpu = psutil.cpu_percent(interval=None)
        uso_memoria = psutil.virtual_memory().percent

        # Capturar estado actual de red
        net_actual = psutil.net_io_counters()
        bytes_descargados = net_actual.bytes_recv - net_anterior.bytes_recv
        bytes_subidos = net_actual.bytes_sent - net_anterior.bytes_sent

        net_anterior = net_actual

        timestamp = datetime.now().isoformat()

        documento = {
            "hostname": hostname,
            "timestamp": timestamp,
            "uso_cpu_porcentaje": uso_cpu,
            "uso_memoria_porcentaje": uso_memoria,
            "red_bytes_descargados": bytes_descargados,
            "red_bytes_subidos": bytes_subidos
        }

        try:
            resultado = coleccion.insert_one(documento)
            print(f"[{i+1}/10] Insertado: {documento}")
        except Exception as e:
            print(f"Error al insertar en MongoDB: {e}")

        tiempo_restante = 1.0 - (time.time() - inicio)
        if tiempo_restante > 0:
            time.sleep(tiempo_restante)

if __name__ == "__main__":
    monitorear_uso_cpu_memoria_red()

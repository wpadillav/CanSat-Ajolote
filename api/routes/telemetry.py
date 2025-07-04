from fastapi import APIRouter, Body
from models.telemetry import TelemetryData
from db.atlas import telemetry_atlas
from db.local import telemetry_local
from datetime import datetime

# Crea un router para agrupar las rutas relacionadas con la telemetría
router = APIRouter()

@router.post("/telemetry")
async def receive_telemetry(data: TelemetryData = Body(...)):
    """
    Endpoint que recibe datos de telemetría mediante una solicitud POST.
    Los datos se almacenan tanto en la base de datos local como en la nube.
    """
    # Convierte los datos recibidos a diccionario
    entry = data.dict()

    # Si no se proporciona timestamp, se asigna el tiempo actual en UTC
    entry["timestamp"] = entry.get("timestamp") or datetime.utcnow()

    # Inserta los datos en MongoDB local
    telemetry_local.insert_one(entry)

    # Inserta los datos en MongoDB Atlas
    telemetry_atlas.insert_one(entry)

    # Devuelve una respuesta indicando éxito
    return {"status": "success", "saved_at": entry["timestamp"]}

@router.get("/")
async def health_check():
    """
    Endpoint de salud que permite verificar que el servicio esté activo.
    """
    return {"status": "ok", "message": "Telemetry service is running"}

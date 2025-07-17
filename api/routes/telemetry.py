from fastapi import APIRouter, Body, Depends
from utils.dependencies import get_current_user
from models.telemetry import TelemetryData
from db.atlas import telemetry_atlas
from db.local import telemetry_local
from datetime import datetime

router = APIRouter()

@router.get("/telemetry")
async def get_telemetry(user: str = Depends(get_current_user)):
    """
    Devuelve los últimos 10 datos de telemetría.
    Requiere autenticación con JWT.
    """
    data_local = list(telemetry_local.find({}, {"_id": 0}).sort("timestamp", -1).limit(10))
    return {
        "source": "local",
        "count": len(data_local),
        "data": data_local
    }

@router.post("/telemetry")
async def receive_telemetry(
    data: TelemetryData = Body(...),
    user: str = Depends(get_current_user)
):
    """
    Endpoint que recibe datos de telemetría mediante una solicitud POST.
    Requiere autenticación mediante JWT.
    Los datos se almacenan tanto en la base de datos local como en la nube.
    """
    entry = data.dict()
    entry["timestamp"] = entry.get("timestamp") or datetime.utcnow()

    telemetry_local.insert_one(entry)
    telemetry_atlas.insert_one(entry)

    return {
        "status": "success",
        "saved_at": entry["timestamp"],
        "received_by": user
    }

@router.get("/")
async def health_check():
    """
    Endpoint de salud que permite verificar que el servicio esté activo.
    """
    return {"status": "ok", "message": "Telemetry service is running"}


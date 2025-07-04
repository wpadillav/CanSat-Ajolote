from pydantic import BaseModel, Extra
from typing import Optional
from datetime import datetime

# Modelo de datos que representa una entrada de telemetría
class TelemetryData(BaseModel):
    device_id: str              # ID único del dispositivo
    device_type: str            # Tipo de dispositivo (e.g., "satellite")
    device_name: str            # Nombre del dispositivo
    device_model: str           # Modelo del dispositivo
    temperature: Optional[float] = None   # Temperatura (opcional)
    humidity: Optional[float] = None      # Humedad (opcional)
    gps_lat: Optional[float] = None       # Latitud GPS (opcional)
    gps_lon: Optional[float] = None       # Longitud GPS (opcional)
    timestamp: Optional[datetime] = None  # Marca de tiempo (opcional)

    class Config:
        # Permite campos adicionales no definidos en el modelo
        extra = Extra.allow

# main.py
from fastapi import FastAPI
from routes.telemetry import router as telemetry_router
from config import ENV

# Solo activa documentación si no está en producción
is_production = ENV == "production"

app = FastAPI(
    title="CanSat Ajolote API",
    description="Recepción y almacenamiento de telemetría en MongoDB local y Atlas",
    version="1.0.0",
    docs_url=None if is_production else "/docs",             # Swagger UI
    redoc_url=None if is_production else "/redoc",           # ReDoc
    openapi_url=None if is_production else "/openapi.json"   # Esquema OpenAPI
)

# Montar rutas de telemetría
app.include_router(telemetry_router, prefix="/api")

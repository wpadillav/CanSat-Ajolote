# CanSat Ajolote API

**Recepción y almacenamiento de telemetría en MongoDB (local y Atlas)**

Esta API está diseñada para recibir datos de telemetría enviados por dispositivos mediante sensores, y almacenarlos simultáneamente en dos bases de datos MongoDB: una local y otra en la nube (MongoDB Atlas).

---

## Estructura del Proyecto

```

.
├── config.py                 # Configuración de MongoDB
├── db/                       # Conexiones a MongoDB
│   ├── atlas.py              # Cliente Atlas
│   └── local.py              # Cliente Local
├── main.py                   # Punto de entrada de FastAPI
├── models/
│   └── telemetry.py          # Modelo de datos (Pydantic)
├── requirements.txt          # Dependencias del proyecto
├── routes/
│   └── telemetry.py          # Rutas de la API
└── .env                      # Variables de entorno

````

---

## Configuracion y uso

### 1. Copia este directorio, crea un entorno virtual e instalar dependencias

```bash
python3 -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 2. Configurar las variables de entorno

Crea un archivo `.env` en el directorio raíz y agrega:

```env
# MongoDB Atlas (nube)
MONGO_ATLAS_URI=mongodb+srv://<usuario>:<contraseña>@<cluster>.mongodb.net/

# MongoDB local (servidor privado)
MONGO_USER=admin
MONGO_PASSWORD=tu_contraseña
MONGO_HOST=tu_ip_local
MONGO_PORT=27017
MONGO_DB=Cansat
MONGO_COLLECTION=telemetria

# Entorno: development o production
ENV=development
```

## Ejecución

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8888
```

Por defecto, la API estará disponible en: [http://localhost:8888](http://localhost:8888)

#### Documentación interactiva

* Swagger UI: [http://localhost:8888/docs](http://localhost:8888/docs)
* ReDoc: [http://localhost:8888/redoc](http://localhost:8888/redoc)

> **Nota:** Estas rutas solo estarán disponibles si la variable de entorno `ENV` está configurada como `development`.
> En producción (`ENV=production`), estas rutas se desactivan automáticamente por seguridad.

---

## Endpoints

### Health Check

**GET** `/api/`

Verifica si el servicio está funcionando correctamente.

**Respuesta:**

```json
{
  "status": "ok",
  "message": "Telemetry service is running"
}
```

---

### Enviar Telemetría

**POST** `/api/telemetry`

Envía datos de telemetría. Los datos se almacenan tanto en MongoDB local como en Atlas.

**Ejemplo de cuerpo JSON:**

```json
{
  "device_id": "ajolote-001",
  "device_type": "satellite",
  "device_name": "CanSat Ajolote",
  "device_model": "v1.0",
  "temperature": 24.7,
  "humidity": 55.3,
  "gps_lat": 19.4326,
  "gps_lon": -99.1332
}
```

**Respuesta:**

```json
{
  "status": "success",
  "saved_at": "2025-07-04T12:34:56.789Z"
}
```

---

## 🧪 Pruebas con `curl`

```bash
curl -X POST http://localhost:8888/api/telemetry \
-H "Content-Type: application/json" \
-d '{
  "device_id": "ajolote-001",
  "device_type": "satellite",
  "device_name": "CanSat Ajolote",
  "device_model": "v1.0",
  "temperature": 22.5,
  "humidity": 48.2,
  "gps_lat": 19.34,
  "gps_lon": -99.14
}'
```

---

## Tecnologías

* **FastAPI**: Framework web moderno y rápido para construir APIs con Python.
* **MongoDB**: Base de datos NoSQL tanto local como en la nube.
* **Pydantic**: Validación de datos para los modelos de entrada.
* **dotenv**: Gestión de variables de entorno.

---

## Notas

* El endpoint `/api/telemetry` guarda los datos automáticamente en **ambas bases de datos** (local y Atlas).
* Los campos `timestamp` se generan automáticamente si no se envían.
* Si deseas extender los datos del payload, puedes hacerlo sin modificar el modelo gracias a `extra = Extra.allow`.

---

## Contacto

¿Preguntas o sugerencias? Contáctanos en [willipadilla@proton.me](mailto:willipadilla@proton.me)

---

## Requisitos

* Python 3.10 o superior
* MongoDB en ejecución local y Mongo Atlas

# CanSat Ajolote 🛰️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ESP32](https://img.shields.io/badge/ESP32-TTGO_T18_v3-green.svg)](https://espressif.com)
[![Arduino IDE](https://img.shields.io/badge/Arduino-IDE-blue.svg)](https://arduino.cc)
[![Python](https://img.shields.io/badge/Backend-Python3-blue.svg)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen.svg)](https://www.mongodb.com)
[![LoRa](https://img.shields.io/badge/Radio-LoRa-orange.svg)](https://lora-alliance.org)

---

## Información del Proyecto

**Estudiantes:** William Enrique Padilla Vivero, Fabian Ricardo Orozco Infante, Henry Alexander Rivera Rojas, ...
**Docente:** Laura Mercedes Arteaga Rojas                   
**Universidad:** UNIMINUTO - Universidad Minuto de Dios             
**Programa:** Ingeniería de Software                
**Semillero:** AJOLOTE            

---

## Descripción del Proyecto

**CanSat Ajolote** es un nanosatélite educativo basado en **ESP32 TTGO T-Energy T18 v3**, orientado a la captura, almacenamiento y transmisión de datos ambientales y de ubicación en tiempo real.

El sistema integra sensores para variables ambientales, posicionamiento GPS y una cámara para captura de imágenes. La comunicación de telemetría entre el CanSat y la estación base terrestre se realiza mediante tecnología **LoRa**.

Toda la telemetría y las imágenes se almacenarán tanto de manera local como en dos instancias de **MongoDB**: una en la nube (**MongoDB Atlas**) y otra en un **servidor privado**.

---

## Objetivos del Proyecto

* Captura de variables ambientales: **temperatura**, **humedad**, **presión atmosférica (altura estimada)**.
* Adquisición de **ubicación GPS (NEO-6M)**.
* **Captura de imágenes** utilizando una cámara **OV2640**.
* **Comunicación LoRa** entre CanSat y Estación Base.
* **Almacenamiento local y replicación remota** en **MongoDB Atlas** y **MongoDB local** mediante un backend desarrollado en **Python 3**.
* Implementación de un sistema de recuperación (paracaídas).

---

## Arquitectura General del Sistema

* **CanSat (Módulo de vuelo):**

  * Captura de datos ambientales (BME280)
  * Obtención de ubicación GPS (NEO-6M)
  * Captura de imágenes (OV2640)
  * Envío de telemetría vía **LoRa**
  * Almacenamiento local (en desarrollo)

* **Estación Base:**

  * Recepción de datos vía **LoRa**
  * Ejecución de un **backend Python3** que recibe y almacena datos
  * Replicación de datos a:

    * **MongoDB Atlas (nube)**
    * **MongoDB en servidor privado**

* **Base de Datos:**

  * **MongoDB Atlas (cloud)**
  * **MongoDB local (on-premises)**

---

## Componentes Principales

| Componente                     | Función                                              |
| ------------------------------ | ---------------------------------------------------- |
| **ESP32 TTGO T-Energy T18 v3** | Unidad central de control y comunicaciones           |
| **BME280**                     | Sensor de temperatura, humedad y presión             |
| **SX1276/SX1278 (LoRa)**       | Comunicación inalámbrica entre módulos               |
| **NEO-6M**                     | Posicionamiento GPS                                  |
| **OV2640**                     | Captura de imágenes                                  |
| **Python 3 Backend**           | Recepción de datos, API REST y replicación a MongoDB |
| **MongoDB Atlas**              | Base de datos en la nube                             |
| **MongoDB local**              | Base de datos privada                                |
| **Sistema de recuperación**    | Paracaídas (planificado)                             |

---

## Estado Actual del Proyecto

**Fase actual:** Desarrollo de software

| Área                                           | Estado        |
| ---------------------------------------------- | ------------- |
| **Integración de sensores y módulos**          | En desarrollo |
| **Lectura y toma de datos (Python3)**          | En desarrollo |
| **Creación de la API REST para MongoDB**       | En desarrollo |
| **Replicación a ambas bases de datos MongoDB** | En desarrollo |
| **Pruebas de comunicación LoRa**               | Pendiente     |
| **Captura y almacenamiento de imágenes**       | Pendiente     |
| **Pruebas de campo y vuelos**                  | Pendiente     |
| **Sistema de recuperación**                    | Pendiente     |

---

## Estructura del Proyecto

```
CanSat-Ajolote/
├── api
├─── .env                 # Variables de entorno API
├─── config.py            # Configuración de MongoDB
├─── db/                  # Conexiones a MongoDB
│     ├── atlas.py        # Cliente Atlas
│     └── local.py        # Cliente Local
├─── main.py              # Punto de entrada de FastAPI
├─── models/
│     └── telemetry.py    # Modelo de datos (Pydantic)
├─── requirements.txt     # Dependencias del proyecto
├─── routes/
│     └── telemetry.py    # Rutas de la API
├── .env                  # Variables de entorno
├── flight-module/        # Código del CanSat (módulo de vuelo)
├── ground-station/       # Código de la estación base (receptor LoRa + backend Python)
├── backend/              # API REST y replicación a MongoDB
├── docs/                 # Documentación técnica y reportes
├── hardware/             # Esquemáticos y diagramas de conexión
└── tests/                # Scripts de prueba de sensores, LoRa y comunicación
```

---

## Próximos Pasos

1. Finalizar desarrollo de captura de datos de sensores.
2. Integrar el GPS NEO-6M y la cámara OV2640.
3. Terminar desarrollo del backend en Python3.
4. Configurar la replicación de datos a ambas bases MongoDB.
5. Iniciar pruebas de comunicación LoRa.
6. Realizar pruebas de captura y almacenamiento de imágenes.
7. Comenzar pruebas de campo y simulaciones de vuelo.
8. Desarrollar e implementar el sistema de recuperación (paracaídas).

---

## Licencia

Este proyecto está bajo la licencia **MIT**.
Consulta el archivo `LICENSE` para más información.

---

### Contexto Institucional

El objetivo institucional definido por el semillero es:

> **Diseñar, ensamblar y programar un CanSat que permita capturar variables ambientales (temperatura, presión, humedad, GPS, entre otros), transmitiendo los datos en tiempo real a una base MongoDB para su posterior análisis y visualización.**

### Plan de Trabajo por Fases

El proyecto sigue la siguiente estructura de fases institucional:

1. Diseño y capacitación
2. Integración de hardware
3. Programación de adquisición de datos
4. Programación de transmisión de datos
5. Desarrollo de backend y base de datos
6. Desarrollo de dashboard
7. Pruebas de campo
8. Documentación y presentación

> Puedes consultar el detalle completo del plan institucional en [`/docs/Proyecto_Semillero.md`](docs/Proyecto_Semillero.md).

---

## Contacto

**William Enrique Padilla Vivero**
GitHub: [@wpadillav](https://github.com/wpadillav)

---

**Última actualización:** Junio 2025
**Estado actual:** Desarrollo de software (sensores, API y bases de datos)
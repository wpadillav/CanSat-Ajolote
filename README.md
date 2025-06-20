# CanSat Ajolote 🛰️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ESP32](https://img.shields.io/badge/ESP32-TTGO_T18_v3-green.svg)](https://espressif.com)
[![Arduino IDE](https://img.shields.io/badge/Arduino-IDE-blue.svg)](https://arduino.cc)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen.svg)](https://www.mongodb.com)
[![DynamoDB](https://img.shields.io/badge/Database-DynamoDB-ff69b4.svg)](https://aws.amazon.com/dynamodb/)

---

## Información del Proyecto

**Estudiante:** William Enrique Padilla Vivero  
**Docente:** Laura Mercedes Arteaga Rojas  
**Universidad:** UNIMINUTO - Universidad Minuto de Dios  
**Programa:** Ingeniería de Software  
**Semillero:** AJOLOTE  

---

## Descripción del Proyecto

**CanSat Ajolote** es un nanosatélite educativo autónomo basado en microcontroladores **ESP32 TTGO T18 v3**. El sistema tiene como objetivo recopilar datos ambientales durante el vuelo, transmitirlos a una estación base terrestre y almacenar la información tanto localmente como en una base de datos remota.  

Se están evaluando las siguientes tecnologías para almacenamiento y análisis de datos:
- **MongoDB**: por su flexibilidad y fácil integración con dashboards.
- **DynamoDB**: por su escalabilidad y uso en la nube.

---

## Objetivos del Proyecto

- Captura de datos ambientales (temperatura, presión, humedad, GPS, aceleración)
- Comunicación autónoma entre dos módulos ESP32 mediante LoRa
- Almacenamiento local y remoto de datos de vuelo
- Diseño modular para facilitar pruebas y ampliaciones futuras

---

## Arquitectura General

- **CanSat Volador (ESP32 TTGO T18 v3):** recopilación de datos, captura de imágenes, almacenamiento en MicroSD, transmisión LoRa.
- **Estación Base (ESP32 TTGO T18 v3):** recepción de datos, respaldo en MicroSD, reenvío a base de datos MongoDB/DynamoDB (vía pasarela o integración futura).
- **Base de Datos (planeado):** MongoDB o DynamoDB como solución en la nube para visualizar y analizar la telemetría.

---

## Componentes Clave

| Componente         | Función                            |
|--------------------|-------------------------------------|
| ESP32 TTGO T18 v3  | Controlador principal               |
| BME280             | Sensor ambiental                    |
| MPU6050            | Sensor de movimiento                |
| NEO-8M             | Módulo GPS                          |
| ESP32-CAM          | Captura de imágenes (opcional)      |
| LoRa SX1276        | Comunicación inalámbrica            |
| MicroSD (32 GB)    | Almacenamiento local                |
| MongoDB/DynamoDB   | Almacenamiento remoto (planeado)    |

---

## Estado Actual del Proyecto

Actualmente en **fase de planificación y definición de materiales**.  
Se están evaluando tecnologías de comunicación, almacenamiento, diseño de la arquitectura base y componentes necesarios.

---

## Próximas Fases del Proyecto

1. **Diseño de hardware** (PCB, integración de sensores, chasis)
2. **Desarrollo de firmware** (lectura de sensores, envío LoRa, almacenamiento)
3. **Pruebas en laboratorio** (transmisión entre módulos, pruebas de sensores)
4. **Desarrollo del backend y conexión con base de datos MongoDB/DynamoDB**
5. **Desarrollo de dashboard para visualización web**
6. **Pruebas de campo y simulación de vuelo**
7. **Análisis de datos y optimización de sistema**

---

## Estructura General del Proyecto

```

CanSat-Ajolote/
├── cansat-flight/       # Código del módulo de vuelo
├── ground-station/      # Código de la estación base
├── docs/                # Documentación y manuales
├── hardware/            # Modelos físicos, esquemas
└── tests/               # Pruebas unitarias e integración

```

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

---

## Contacto

**William Enrique Padilla Vivero**  
- GitHub: [@wpadillav](https://github.com/wpadillav)  

---

## Agradecimientos


---

## Estado del Proyecto

**Última actualización:** Junio 2025  
**Estado actual:** Planificación y definición técnica  
**Siguiente hito:** Integración de sensores y pruebas con LoRa
```

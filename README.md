# CanSat Ajolote 🛰️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Compatible-red.svg)](https://raspberrypi.org)

## 👨‍🎓 Información del Proyecto

**Estudiante:** William Enrique Padilla Vivero  
**Docente:** Laura Mercedes Arteaga Rojas  
**Universidad:** UNIMINUTO - Universidad Minuto de Dios  
**Programa:** Ingeniería de Software  
**Semillero:** AJOLOTE  

---

## 📋 Descripción del Proyecto

CanSat Ajolote es un proyecto de nanosatélite educativo que simula una misión espacial completa. El sistema recopila datos ambientales durante el vuelo y los transmite en tiempo real a una estación base terrestre con dashboard interactivo.

### 🎯 Objetivos de la Misión

- **Captura de imágenes** aéreas durante el descenso
- **Monitoreo ambiental** (temperatura, presión, humedad)
- **Telemetría completa** (altitud, aceleración, coordenadas GPS)
- **Transmisión en tiempo real** de datos a estación base
- **Visualización interactiva** mediante dashboard web

---

## 🏗️ Arquitectura del Sistema

### CanSat (Payload)
- **Controlador:** Raspberry Pi Zero 2W
- **Comunicación:** LoRa (primario) + 4G (secundario opcional)
- **Sensores:** Cámara, BME280, GPS, MPU6050
- **Alimentación:** Batería LiPo con sistema de gestión

### Estación Base
- **Controlador:** Raspberry Pi 4B
- **Recepción:** Módulo LoRa + receptor 4G opcional
- **Interface:** Dashboard web en tiempo real
- **Almacenamiento:** Base de datos local + respaldo en nube

---

## 🔧 Componentes Principales

### Hardware del CanSat
| Componente | Modelo | Función |
|------------|--------|---------|
| Microcontrolador | Raspberry Pi Zero 2W | Procesamiento principal |
| Cámara | Pi Camera Module | Captura de imágenes |
| Sensor ambiental | BME280 | Temperatura, presión, humedad |
| GPS | NEO-8M | Coordenadas y altitud |
| Acelerómetro | MPU6050 | Aceleración y orientación |
| Comunicación | LoRa SX1278 | Transmisión de datos |
| Respaldo 4G | SIM800L | Comunicación secundaria |
| Batería | LiPo 3.7V | Alimentación |

### Software
- **Lenguaje:** Python 3.10+
- **Framework web:** FastAPI
- **Base de datos:** InfluxDB + SQLite
- **Frontend:** React.js
- **Visualización:** Grafana + custom dashboard
- **Tiempo real:** WebSockets

---

## 📊 Funcionalidades del Dashboard

### Telemetría en Tiempo Real
- 📈 Gráficas de sensores ambientales
- 🗺️ Tracking GPS en mapa interactivo
- 📸 Galería de imágenes transmitidas
- ⚡ Indicadores de estado del sistema
- 📊 Métricas de rendimiento

### Características Avanzadas
- 🎯 Predicción de zona de aterrizaje
- 🚨 Sistema de alertas automáticas
- 📱 Interface responsive (móvil/desktop)
- 💾 Exportación de datos
- 🔄 Sincronización con nube

---

## 🚀 Fases del Proyecto

### Fase 1: Diseño y Planificación ✅
- [x] Definición de objetivos
- [x] Selección de componentes
- [ ] Arquitectura del sistema
- [ ] Documentación técnica

### Fase 2: Desarrollo de Hardware
- [ ] Diseño de PCB
- [ ] Ensamblaje del CanSat
- [ ] Pruebas de componentes
- [ ] Integración de sensores

### Fase 3: Desarrollo de Software
- [ ] Firmware del CanSat
- [ ] Sistema de comunicaciones
- [ ] Dashboard web
- [ ] Base de datos

### Fase 4: Integración y Pruebas
- [ ] Pruebas de laboratorio
- [ ] Pruebas de campo
- [ ] Simulación de misión
- [ ] Optimización del sistema

### Fase 5: Misión y Análisis
- [ ] Lanzamiento del CanSat
- [ ] Monitoreo en tiempo real
- [ ] Recuperación de datos
- [ ] Análisis de resultados

---

## 🛠️ Instalación y Configuración

### Requisitos Previos


### Instalación del Proyecto


### Configuración


---

## 📁 Estructura del Proyecto 

```
CanSat-Ajolote/
├── cansat/                 # Código del CanSat
│   ├── sensors/           # Drivers de sensores
│   ├── communication/     # Módulos de comunicación
│   ├── camera/           # Sistema de cámara
│   └── main.py           # Programa principal
├── ground-station/        # Estación base
│   ├── backend/          # API y lógica del servidor
│   ├── frontend/         # Dashboard web
│   ├── database/         # Esquemas de BD
│   └── receivers/        # Receptores de datos
├── hardware/             # Diseños de PCB y esquemas
├── docs/                 # Documentación técnica
├── tests/                # Pruebas unitarias
└── simulation/           # Herramientas de simulación
```

---

## 📡 Protocolo de Comunicación

### LoRa (Primario)
- **Frecuencia:** 915 MHz
- **Alcance:** 5-15 km
- **Tasa de datos:** 250 bps - 5.5 kbps
- **Formato:** JSON comprimido

### 4G (Secundario)
- **Protocolo:** HTTP/MQTT
- **Uso:** Backup y transmisión de imágenes
- **Cobertura:** Según operador móvil

---

## 📊 Especificaciones Técnicas

### Dimensiones del CanSat
- **Diámetro:** 66 mm
- **Altura:** 115 mm
- **Peso:** < 350g

### Rangos de Sensores
- **Temperatura:** -40°C a +85°C
- **Presión:** 300-1100 hPa
- **Humedad:** 0-100% RH
- **Altitud:** 0-9000 m (GPS)
- **Aceleración:** ±16g

### Autonomía
- **Tiempo de vuelo:** 15-20 minutos
- **Transmisión continua:** 30 minutos
- **Standby:** 2 horas

---

## 🤝 Contribuciones

Este proyecto es de código abierto y las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 📞 Contacto

**William Enrique Padilla Vivero**  
- 🐙 GitHub: [@wpadillav](https://github.com/wpadillav)

---

## 🙏 Agradecimientos

---

## 📈 Estado del Proyecto

![Progreso](https://progress-bar.dev/15/?title=Progreso%20General)

**Última actualización:** Junio 2025  
**Estado:** En desarrollo activo  
**Próximo hito:** Prototipo funcional
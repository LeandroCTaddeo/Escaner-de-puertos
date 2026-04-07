# Escáner de Puertos TCP

## Descripción

Este proyecto consiste en un escáner de puertos desarrollado en Python que permite identificar puertos abiertos en una dirección IP específica.

La herramienta utiliza conexiones TCP para verificar el estado de los puertos dentro del rango completo (1–65535), permitiendo detectar servicios activos en un host.

Este tipo de análisis es fundamental en tareas de reconocimiento, auditorías de seguridad y monitoreo de infraestructura.

---

## Funcionamiento

El script solicita al usuario una dirección IP y realiza un escaneo secuencial de todos los puertos TCP disponibles.

Por cada puerto:

- Intenta establecer una conexión utilizando sockets
- Si la conexión es exitosa, el puerto se considera abierto
- En caso contrario, se considera cerrado

---

## Tecnologías utilizadas

- Python 3
- Librería estándar:
  - `socket`

---

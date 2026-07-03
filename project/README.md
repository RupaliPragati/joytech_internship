# joytech_internship
# CERT-SAT Backend Architecture

## Objective
Develop a scalable backend system for receiving, validating, processing, and storing satellite telemetry data.

## Technology Stack

- FastAPI
- Python 3.12
- Pydantic
- PostgreSQL (Future)
- Redis (Future)
- Docker (Future)

## System Architecture

Satellite Sensors
↓
Ground Station
↓
FastAPI Ingestion API
↓
Validation Layer
↓
Processing Service
↓
Database Storage
↓
Monitoring Dashboard

## Components

### Ingestion Layer
Receives telemetry packets from satellites through REST APIs.

### Validation Layer
Validates incoming telemetry using Pydantic schemas.

### Processing Layer
Normalizes telemetry values and prepares data for storage.

### Storage Layer
Stores telemetry history for analysis and monitoring.

### Monitoring Layer
Provides health status and system diagnostics.

## Future Improvements

- JWT Authentication
- Kafka Streaming
- Redis Cache
- Real-time WebSocket Telemetry
- Anomaly Detection


## how to run
python main.py
uvicorn main:app --reload
## for opening swagger
https://psychic-disco-x54x7vqqjvq6fpgv4-8000.app.github.dev/docs#/default/latest_telemetry_telemetry_latest_get

## Example Data 
{
  "satellite_id": "SAT-001",
  "timestamp": "2026-07-02T08:00:00",
  "battery_voltage": 4.8,
  "temperature": 35,
  "cpu_usage": 45,
  "signal_strength": 80
}
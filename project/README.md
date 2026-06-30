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
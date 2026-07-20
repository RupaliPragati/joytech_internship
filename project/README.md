# joytech_internship
# CERT-SAT Backend

A FastAPI-based backend for satellite telemetry processing, anomaly detection, and system monitoring.

---

# Features

- Receive satellite telemetry packets
- Validate telemetry using Pydantic
- Detect anomalies using the trained ML model
- Health monitoring endpoint
- Request logging middleware
- API versioning (`/api/v1`)
- Swagger API documentation

---

# Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy
- Scikit-learn
- Joblib
- Docker

---

# Project Structure

```
project/
│── app/
│── src/
│── docs/
│── models_saved/
│── main.py
│── requirements.txt
│── Dockerfile
│── .env.example
│── telemetry.db
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd project
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file by copying the example file.

```bash
cp .env.example .env
```

Update the required values if necessary.

---

# Running Locally

Start the backend

```bash
uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
https://psychic-disco-x54x7vqqjvq6fpgv4-8000.app.github.dev/docs#/default/latest_telemetry_telemetry_latest_get
```

---

# Docker

Build the image

```bash
docker build -t certsat-backend .
```

Run the container

```bash
docker run -p 8000:8000 cert-sat-backend
```

---

# API Endpoints

## Health

```
GET /api/v1/health
```

Returns

- API status
- Model status
- Backend version
- Timestamp

---

## Predict

```
POST /api/v1/predict
```

Example Request

```json
{
  "satellite_id": "SAT-001",
  "timestamp": "2026-07-16T10:00:00",
  "battery_voltage": 12.4,
  "temperature": 38.2,
  "cpu_usage": 43,
  "signal_strength": 91
}
```

---

# Telemetry

```
POST /api/v1/telemetry
```

```
GET /api/v1/telemetry/history
```

```
GET /api/v1/telemetry/latest
```

---

# Configuration

The backend uses environment variables defined in `.env`.

Example variables:

```
HOST
PORT
DEBUG
DATABASE_URL
LOG_LEVEL
MODEL_VERSION
```

---

# Testing

Run the prediction test

```bash
python test_predict.py
```

Run concurrent request testing

```bash
python test_concurrent.py
```

---

# Future Improvements

- JWT Authentication
- PostgreSQL
- Redis Cache
- Kafka Streaming
- WebSocket Telemetry
- CI/CD Pipeline

---

# License

MIT License


# for clean enviroment verification 
is:

Build the Docker image:

docker build -t certsat-backend .

Run it:

docker run -p 8000:8000 certsat-backend

Open:

http://localhost:8000/docs
Verify:
GET /api/v1/health returns 200 OK.
POST /api/v1/predict is accessible.
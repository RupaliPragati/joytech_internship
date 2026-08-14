# CERT-SAT Backend

A FastAPI-based backend for satellite telemetry processing, anomaly detection, authentication, and system monitoring.

## Features

- FastAPI REST APIs
- JWT Authentication
- Satellite Telemetry Processing
- ML-based Anomaly Detection
- Pydantic Request Validation
- Health Monitoring Endpoint
- Request Logging Middleware
- API Versioning
- Swagger API Documentation
- Docker Support

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- SQLAlchemy
- Uvicorn
- Scikit-learn
- Joblib
- Docker

## Project Structure

```text
project/
├── app/
├── docs/
├── models_saved/
├── src/
├── main.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── README.md
```

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd project
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

## Environment Setup

Create the environment file.

```bash
cp .env.example .env
```

Update the environment variables if required.

## Run Locally

Start the FastAPI server.

```bash
uvicorn main:app --reload
```

The backend will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

## Docker

Build the Docker image.

```bash
docker build -t certsat-backend .
```

Run the container.

```bash
docker run -p 8000:8000 certsat-backend
```

Open:

```
http://localhost:8000/docs
```

## API Endpoints

### Health Check

```
GET /api/v1/health
```

Returns the backend status, model status, version, and timestamp.

### Login

```
POST /api/v1/login
```

Returns a JWT access token.

### Prediction

```
POST /api/v1/predict
```

Example request:

```json
{
  "satellite_id": "SAT-001",
  "timestamp": "2026-07-16T10:00:00Z",
  "battery_voltage": 12.4,
  "temperature": 38.2,
  "cpu_usage": 43,
  "signal_strength": 91
}
```

### Telemetry

```
POST /api/v1/telemetry
```

```
GET /api/v1/telemetry/history
```

```
GET /api/v1/telemetry/latest
```

## Configuration

Environment variables are configured through the `.env` file.

Example:

```text
HOST
PORT
DEBUG
DATABASE_URL
SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
MODEL_PATH
LOG_LEVEL
API_VERSION
```

## Testing

Run the prediction test.

```bash
python test_predict.py
```

Run concurrent request testing.

```bash
python test_concurrent.py
```

## Deployment Verification

After deployment, verify the following:

1. Open:

```
http://localhost:8000/docs
```

2. Verify:

- `GET /api/v1/health` returns **200 OK**
- `POST /api/v1/login` returns a JWT token
- `POST /api/v1/predict` accepts authenticated requests
- Swagger loads successfully
- Docker container starts without errors
- Logs are generated correctly

## Documentation

Additional documentation is available in the `docs/` directory.

- API Documentation
- Backend Architecture
- ML Integration

## License

MIT License

python -m http.server 5500


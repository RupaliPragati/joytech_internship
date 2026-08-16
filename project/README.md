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
## Firebase Authentication Setup

The backend uses Firebase Admin SDK to verify Google authentication
tokens.

For security reasons, the Firebase service-account credential is NOT
included in the Git repository.

### 1. Create Firebase Service Account Credentials

Go to:

Firebase Console
→ Project Settings
→ Service Accounts
→ Firebase Admin SDK
→ Generate New Private Key

Download the generated JSON credential file.

### 2. Place the Credential

Create the following directory:

project/app/firebase/

Place the downloaded credential file inside it.

Example:

project/
├── app/
│   └── firebase/
│       └── firebase-service-account.json
├── main.py
├── requirements.txt
└── ...

### 3. Configure the Credential Path

Set the Firebase credential path using an environment variable:

FIREBASE_CREDENTIALS_PATH=app/firebase/firebase-service-account.json

### 4. Start the FastAPI Backend

From the project directory:

uvicorn main:app --reload

The API will then be available through the configured FastAPI server.

### Security Note

The Firebase service-account JSON contains private credentials and must
NOT be committed to Git or uploaded to the public repository.

The credential file is excluded using `.gitignore`.

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

python3 -m http.server 5500 --directory frontend


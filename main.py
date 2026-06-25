from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="CERT-SAT Backend",
    version="1.0.0"
)

class TelemetryData(BaseModel):
    satellite_id: str
    timestamp: datetime
    temperature: float
    voltage: float
    signal_strength: float

@app.get("/")
def root():
    return {"message": "CERT-SAT Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/telemetry")
def receive_telemetry(data: TelemetryData):
    return {
        "status": "received",
        "satellite": data.satellite_id,
        "timestamp": data.timestamp
    }
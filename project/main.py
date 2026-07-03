from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.telemetry import router as telemetry_router
from app.api.status import router as status_router
from app.core.config import settings
from app.exceptions.handlers import (
    TelemetryException,
    telemetry_exception_handler
)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend service for satellite telemetry processing and anomaly detection."
)
app.add_exception_handler(TelemetryException, telemetry_exception_handler)
app.include_router(health_router)
app.include_router(status_router)
app.include_router(telemetry_router)

@app.get("/")
def root():
    return {"message": "CERT-SAT Backend Running"}
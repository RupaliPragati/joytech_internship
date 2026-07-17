from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.telemetry import router as telemetry_router
from app.api.status import router as status_router
from app.core.config import settings
from app.exceptions.handlers import (
    TelemetryException,
    telemetry_exception_handler
)
from app.middleware.logging import RequestLoggingMiddleware
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend service for satellite telemetry processing and anomaly detection."
)
from app.api.auth import router as auth_router
app.add_middleware(RequestLoggingMiddleware)
app.add_exception_handler(TelemetryException, telemetry_exception_handler)
app.include_router(health_router, prefix="/api/v1")
app.include_router(status_router, prefix="/api/v1")
app.include_router(telemetry_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "message": "CERT-SAT Backend Running",
        "api_version": "v1",
        "docs": "/docs",
        "health": "/api/v1/health"
    }
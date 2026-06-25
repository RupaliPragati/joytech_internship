from fastapi import APIRouter
from app.models.telemetry import Telemetry
from app.services.telemetry_service import TelemetryService

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)

@router.post("/")
def ingest_telemetry(data: Telemetry):
    return TelemetryService.process(data)
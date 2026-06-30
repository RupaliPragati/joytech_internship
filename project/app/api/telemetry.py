from fastapi import APIRouter
from app.models.telemetry import Telemetry
from app.services.telemetry_service import TelemetryService
from app.models.telemetry import TelemetryPacket

router = APIRouter()

telemetry_service = TelemetryService()

@router.post("/telemetry")
def receive_telemetry(data: TelemetryPacket):

    result = telemetry_service.process(data)

    return result
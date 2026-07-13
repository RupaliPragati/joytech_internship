from fastapi import APIRouter

from app.models.telemetry import TelemetryPacket
from app.models.response import (
    TelemetryResponse,
    TelemetryData,
    StatisticsResponse,
)
from app.services.telemetry_service import TelemetryService

router = APIRouter()

telemetry_service = TelemetryService()


@router.post("/telemetry", response_model=TelemetryResponse)
def receive_telemetry(data: TelemetryPacket):
    """
    Receive, validate and process telemetry packets.
    """
    return telemetry_service.process(data)


@router.post("/predict", response_model=TelemetryResponse)
def predict(data: TelemetryPacket):
    """
    Run anomaly prediction on a telemetry packet.
    """
    return telemetry_service.process(data)


@router.get(
    "/telemetry/history",
    response_model=list[TelemetryData]
)
def telemetry_history():
    """
    Returns all stored telemetry packets.
    """
    return telemetry_service.get_history()


@router.get(
    "/telemetry/latest",
    response_model=TelemetryData
)
def latest_telemetry():
    """
    Returns the latest telemetry packet.
    """
    return telemetry_service.get_latest()


@router.get(
    "/telemetry/statistics",
    response_model=StatisticsResponse
)
def telemetry_statistics():
    """
    Returns telemetry statistics.
    """
    return telemetry_service.get_statistics()
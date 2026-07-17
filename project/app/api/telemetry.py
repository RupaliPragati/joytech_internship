from fastapi import APIRouter, Depends, HTTPException
from app.auth.dependencies import get_current_user
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
def receive_telemetry(data: TelemetryPacket, current_user=Depends(get_current_user)):
    """
    Receive, validate and process telemetry packets.
    """
    return telemetry_service.process(data)


@router.post("/predict", response_model=TelemetryResponse)
def predict(data: TelemetryPacket, current_user=Depends(get_current_user)):
    """
    Run anomaly prediction on a telemetry packet.
    """
    return telemetry_service.process(data)


@router.get(
    "/telemetry/history",
    response_model=list[TelemetryData]
)
def telemetry_history(current_user=Depends(get_current_user)):
    """
    Returns all stored telemetry packets.
    """
    return telemetry_service.get_history()


@router.get(
    "/telemetry/latest",
    response_model=TelemetryData
)
def latest_telemetry(current_user=Depends(get_current_user)):
    """
    Returns the latest telemetry packet.
    """
    return telemetry_service.get_latest()


@router.get(
    "/telemetry/statistics",
    response_model=StatisticsResponse
)
def telemetry_statistics(current_user=Depends(get_current_user)):
    """
    Returns telemetry statistics.
    """
    return telemetry_service.get_statistics()
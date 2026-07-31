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


@router.post(
    "/telemetry",
    response_model=TelemetryResponse,
    summary="Receive Telemetry",
    description="Receives telemetry packets and processes them.",
    responses={
        200: {
            "description": "Telemetry processed successfully",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "message": "Telemetry processed successfully",
                        "alerts": [],
                        "packets_received": 5,
                        "required_packets": 5,
                        "ml_prediction": {
                            "model_name": "BackendTelemetryScorer",
                            "is_anomaly": False,
                            "label": 0,
                            "score": 0.12
                        }
                    }
                }
            },
        },
        422: {
            "description": "Validation Error"
        },
    },
)
def receive_telemetry(data: TelemetryPacket):
    return telemetry_service.process(data)


@router.post(
    "/predict",
    response_model=TelemetryResponse,
    summary="Predict Telemetry Anomaly",
    description="Runs anomaly prediction on the provided telemetry packet.",
    responses={
        200: {"description": "Prediction completed successfully"},
        422: {"description": "Validation Error"},
    },
)
def predict(data: TelemetryPacket):
    return telemetry_service.process(data)


@router.get(
    "/telemetry/history",
    response_model=list[TelemetryData],
    summary="Get Telemetry History",
    description="Returns all stored telemetry packets.",
)
def telemetry_history():
    return telemetry_service.get_history()


@router.get(
    "/telemetry/latest",
    response_model=TelemetryData,
    summary="Get Latest Telemetry",
    description="Returns the latest telemetry packet received by the backend.",
)
def latest_telemetry():
    return telemetry_service.get_latest()


@router.get(
    "/telemetry/statistics",
    response_model=StatisticsResponse,
    summary="Get Telemetry Statistics",
    description="Returns summary statistics calculated from stored telemetry data.",
)
def telemetry_statistics():
    return telemetry_service.get_statistics()
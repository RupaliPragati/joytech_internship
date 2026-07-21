from fastapi import APIRouter, Depends
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


@router.post(
    "/telemetry",
    responses={
    200: {
        "description": "Prediction completed successfully",
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
    401: {
        "description": "Unauthorized",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Not authenticated"
                }
            }
        },
    },
    422: {
        "description": "Validation Error"
    },
    })
def receive_telemetry(
    data: TelemetryPacket,
    current_user=Depends(get_current_user)
):
    return telemetry_service.process(data)


@router.post(
    "/predict",
    response_model=TelemetryResponse,
    summary="Predict Telemetry Anomaly",
    description="Runs anomaly prediction on the provided telemetry packet.",
    responses={
        200: {"description": "Prediction completed successfully"},
        401: {"description": "Unauthorized"},
        422: {"description": "Validation Error"},
    },
)
def predict(
    data: TelemetryPacket,
    current_user=Depends(get_current_user)
):
    return telemetry_service.process(data)


@router.get(
    "/telemetry/history",
    response_model=list[TelemetryData],
    summary="Get Telemetry History",
    description="Returns all stored telemetry packets.",
    responses={
        200: {"description": "Telemetry history retrieved successfully"},
        401: {"description": "Unauthorized"},
    },
)
def telemetry_history(current_user=Depends(get_current_user)):
    return telemetry_service.get_history()


@router.get(
    "/telemetry/latest",
    response_model=TelemetryData,
    summary="Get Latest Telemetry",
    description="Returns the latest telemetry packet received by the backend.",
    responses={
        200: {"description": "Latest telemetry retrieved successfully"},
        401: {"description": "Unauthorized"},
    },
)
def latest_telemetry(current_user=Depends(get_current_user)):
    return telemetry_service.get_latest()


@router.get(
    "/telemetry/statistics",
    response_model=StatisticsResponse,
    summary="Get Telemetry Statistics",
    description="Returns summary statistics calculated from stored telemetry data.",
    responses={
        200: {"description": "Statistics retrieved successfully"},
        401: {"description": "Unauthorized"},
    },
)
def telemetry_statistics(current_user=Depends(get_current_user)):
    return telemetry_service.get_statistics()
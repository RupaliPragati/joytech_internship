from fastapi import APIRouter
from app.models.telemetry import TelemetryPacket
from app.models.response import (
    TelemetryResponse,
    TelemetryData,
    StatisticsResponse
)
from app.services.telemetry_service import TelemetryService


router = APIRouter()

telemetry_service = TelemetryService()


@router.post("/telemetry", response_model=TelemetryResponse)
def receive_telemetry(data: TelemetryPacket):

    result = telemetry_service.process(data)

    return result


@router.get(
    "/telemetry/history",
    response_model=list[TelemetryData]
)
def telemetry_history():
    """
    Returns all telemetry packets received so far.
    """
    return telemetry_service.get_history()


def get_latest(self):

    conn = self.get_connection()
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM telemetry
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)

    return {}


@router.get(
    "/telemetry/statistics",
    response_model=StatisticsResponse
)
def telemetry_statistics():
    """
    Returns basic telemetry statistics.
    """
    return telemetry_service.get_statistics()

@router.post("/telemetry", response_model=TelemetryResponse)
def receive_telemetry(data: TelemetryPacket):
    """
    Receive, validate, and process telemetry packets from satellites.
    """
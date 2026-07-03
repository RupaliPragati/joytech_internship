from pydantic import BaseModel
from datetime import datetime


class TelemetryResponse(BaseModel):
    status: str
    message: str
    alerts: list[str]
    ml_prediction: dict


class TelemetryData(BaseModel):
    id: int
    satellite_id: str
    timestamp: str
    battery_voltage: float
    temperature: float
    cpu_usage: float
    signal_strength: float


class StatisticsResponse(BaseModel):
    total_packets: int
from typing import Optional
from pydantic import BaseModel


class TelemetryResponse(BaseModel):
    status: str
    message: str
    alerts: list[str]
    packets_received: Optional[int] = None
    ml_prediction: Optional[dict] = None


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
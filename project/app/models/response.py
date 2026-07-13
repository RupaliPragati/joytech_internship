from typing import Optional
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    model_name: str
    is_anomaly: bool
    label: int
    score: float


class TelemetryResponse(BaseModel):
    status: str
    message: str
    alerts: list[str]
    packets_received: Optional[int] = None
    required_packets: Optional[int] = None
    ml_prediction: Optional[PredictionResponse] = None


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
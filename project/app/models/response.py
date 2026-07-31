from typing import Optional
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    is_anomaly: bool
    label: int
    score: float
    n_samples: int


class TelemetryResponse(BaseModel):
    status: str
    alerts: list[str]

    # Present only during warm-up
    buffer_size: Optional[int] = None
    required_buffer_size: Optional[int] = None

    # Present once the model starts scoring
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
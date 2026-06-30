from pydantic import BaseModel, Field
from datetime import datetime

class TelemetryPacket(BaseModel):
    satellite_id: str
    timestamp: datetime
    battery_voltage: float = Field(..., ge=0)
    temperature: float
    cpu_usage: float = Field(..., ge=0, le=100)
    signal_strength: float
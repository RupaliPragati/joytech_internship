from pydantic import BaseModel
from datetime import datetime

class Telemetry(BaseModel):
    satellite_id: str
    timestamp: datetime
    battery_voltage: float
    temperature: float
    signal_strength: float
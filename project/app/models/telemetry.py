from datetime import datetime
from pydantic import BaseModel, Field


class TelemetryPacket(BaseModel):
    satellite_id: str = Field(
        ...,
        description="Unique satellite identifier",
        examples=["SAT-001"]
    )

    timestamp: datetime = Field(
        ...,
        description="Telemetry timestamp",
        examples=["2026-07-14T10:00:00"]
    )

    battery_voltage: float = Field(
        ...,
        ge=0,
        description="Battery voltage in volts",
        examples=[12.5]
    )

    temperature: float = Field(
        ...,
        description="Satellite temperature in °C",
        examples=[35.4]
    )

    cpu_usage: float = Field(
        ...,
        ge=0,
        le=100,
        description="CPU usage percentage",
        examples=[42]
    )

    signal_strength: float = Field(
        ...,
        description="Signal strength percentage",
        examples=[90]
    )
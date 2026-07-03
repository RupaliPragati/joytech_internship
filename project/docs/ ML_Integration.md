# ML Integration Interface

The backend expects the ML model to expose a method:

predict(telemetry)

Input:
- TelemetryPacket

Output:

{
    "is_anomaly": bool,
    "confidence": float,
    "reason": str
}

The backend will call this method from TelemetryService and include the prediction in the API response.
# CERT-SAT Backend API

## POST /telemetry

### Description
Receives telemetry packets from the ground station.

### Request Body

- satellite_id
- timestamp
- battery_voltage
- temperature
- cpu_usage
- signal_strength

### Response

```json
{
    "status": "success",
    "alerts": [],
    "ml_prediction": {
        "is_anomaly": false,
        "confidence": 0.98,
        "reason": "No anomaly detected."
    }
}
```

### Future Enhancements

- Database Storage
- ML Model Integration
- Alert Dashboard
- MITRE ATT&CK Mapping
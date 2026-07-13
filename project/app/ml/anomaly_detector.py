from app.ml.model_loader import model_loader


class AnomalyDetector:
    """
    Handles live anomaly prediction using BackendTelemetryScorer.
    """

    def __init__(self):
        self.model = model_loader.get_model()

    def predict(self, telemetry):

        telemetry_data = {
            "battery_voltage": telemetry.battery_voltage,
            "temperature": telemetry.temperature,
            "cpu_usage": telemetry.cpu_usage,
            "signal_strength": telemetry.signal_strength,
        }

        result = self.model.handle_packet(
            satellite_id=telemetry.satellite_id,
            telemetry=telemetry_data,
        )

        if result["status"] == "warming_up":
            return {
                "status": "waiting",
                "message": "Collecting telemetry packets before prediction.",
                "packets_received": result["buffer_size"],
                "required_packets": result["required_buffer_size"],
                "ml_prediction": None,
            }

        return {
            "status": "success",
            "message": "Prediction completed successfully.",
            "ml_prediction": {
                "model_name": "Backend Telemetry Isolation Forest",
                "is_anomaly": result["is_anomaly"],
                "label": result["label"],
                "score": result["score"],
            },
        }
class AnomalyDetector:

    def predict(self, telemetry):

        is_anomaly = (
            telemetry.temperature > 60 or
            telemetry.cpu_usage > 90 or
            telemetry.signal_strength < 20
        )

        confidence = 0.97 if is_anomaly else 0.99

        return {
            "model_name": "Mock Satellite Anomaly Model",
            "model_version": "v1.0",
            "prediction": {
                "is_anomaly": is_anomaly,
                "confidence": confidence,
                "risk_level": "High" if is_anomaly else "Low"
            }
        }
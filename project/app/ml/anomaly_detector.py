from app.logger import logger
from app.ml.model_loader import model_loader


class AnomalyDetector:
    """
    Handles live anomaly prediction using BackendTelemetryScorer.
    """

    def __init__(self):
        logger.info("Initializing BackendTelemetryScorer...")
        self.model = model_loader.get_model()
        logger.info("BackendTelemetryScorer loaded successfully.")

    def predict(self, telemetry):
        logger.info(
            f"Starting prediction for satellite: {telemetry.satellite_id}"
        )

        telemetry_data = {
            "battery_voltage": telemetry.battery_voltage,
            "temperature": telemetry.temperature,
            "cpu_usage": telemetry.cpu_usage,
            "signal_strength": telemetry.signal_strength,
        }

        logger.info(f"Telemetry Data: {telemetry_data}")

        result = self.model.handle_packet(
            satellite_id=telemetry.satellite_id,
            telemetry=telemetry_data,
        )

        logger.info(f"Raw Model Response: {result}")

        if result["status"] == "warming_up":
            logger.warning(
                f"Model warming up for {telemetry.satellite_id} "
                f"({result['buffer_size']}/{result['required_buffer_size']} packets)"
            )

            return {
                "status": "waiting",
                "message": "Collecting telemetry packets before prediction.",
                "packets_received": result["buffer_size"],
                "required_packets": result["required_buffer_size"],
                "ml_prediction": None,
            }

        logger.info(
            f"Prediction completed for {telemetry.satellite_id}"
        )

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
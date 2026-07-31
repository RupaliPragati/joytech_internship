import logging

from app.ml.model_loader import model_loader

logger = logging.getLogger(__name__)


class AnomalyDetector:
    def __init__(self):
        logger.info("Initializing BackendTelemetryScorer...")
        self.model = model_loader.get_model()
        logger.info("BackendTelemetryScorer loaded successfully.")

    def predict(self, telemetry):
      return self.model.handle_packet(
        telemetry.satellite_id,
        {
            "battery_voltage": telemetry.battery_voltage,
            "temperature": telemetry.temperature,
            "cpu_usage": telemetry.cpu_usage,
            "signal_strength": telemetry.signal_strength,
        },
    )
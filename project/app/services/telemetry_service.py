from app.alerts.alert_service import AlertService
from app.ml.anomaly_detector import AnomalyDetector
from app.database.repository import TelemetryRepository
from app.logger import logger
from app.exceptions.handlers import TelemetryException

alert_service = AlertService()
anomaly_detector = AnomalyDetector()
repository = TelemetryRepository()


class TelemetryService:
    """
    Handles telemetry processing and coordinates
    alert generation, ML prediction, and future database operations.
    """

    def process(self, telemetry):

        logger.info(
            f"Telemetry received from {telemetry.satellite_id}"
        )

        if telemetry.temperature < -100:
            raise TelemetryException(
                "Invalid satellite temperature."
            )

        repository.save(telemetry)

        alerts = alert_service.check_alert(telemetry)
        logger.info(f"Generated Alerts: {alerts}")
        prediction = anomaly_detector.predict(telemetry)
        logger.info(f"ML Prediction: {prediction}")

        return {
            "status": "success",
            "message": "Telemetry processed successfully.",
            "alerts": alerts,
            "ml_prediction": prediction
        }

    def get_history(self):
        return repository.get_history()

    def get_latest(self):
        return repository.get_latest()

    def get_statistics(self):
        return repository.get_statistics()
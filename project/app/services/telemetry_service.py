from fastapi import HTTPException

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
    alert generation, ML prediction, and database operations.
    """

    def process(self, telemetry):
        try:
            logger.info(
                f"Received telemetry from satellite: {telemetry.satellite_id}"
            )

            # Validate telemetry
            if telemetry.temperature < -100:
                logger.error(
                    f"Invalid temperature received: {telemetry.temperature}"
                )
                raise TelemetryException(
                    "Invalid satellite temperature."
                )

            # Save telemetry
            logger.info("Saving telemetry to database...")
            repository.save(telemetry)

            # Generate alerts
            logger.info("Checking alert conditions...")
            alerts = alert_service.check_alert(telemetry)
            logger.info(f"Generated Alerts: {alerts}")

            # Run ML prediction
            logger.info("Running ML prediction...")
            prediction = anomaly_detector.predict(telemetry)
            logger.info(f"Prediction Result: {prediction}")

            # Model is still warming up
            if prediction["status"] == "waiting":
                logger.warning(
                    f"Model warming up ({prediction['packets_received']}/"
                    f"{prediction['required_packets']} packets collected)"
                )

                return {
                    "status": prediction["status"],
                    "message": prediction["message"],
                    "alerts": alerts,
                    "packets_received": prediction["packets_received"],
                    "required_packets": prediction["required_packets"],
                    "ml_prediction": None,
                }

            logger.info("Prediction completed successfully.")

            return {
                "status": prediction["status"],
                "message": prediction["message"],
                "alerts": alerts,
                "ml_prediction": prediction["ml_prediction"],
            }

        except TelemetryException as e:
            logger.error(f"Telemetry Error: {str(e)}")
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )

        except Exception as e:
            logger.exception("Unexpected error during telemetry processing.")

            raise HTTPException(
                status_code=500,
                detail="Internal server error while processing telemetry."
            )

    def get_history(self):
        logger.info("Fetching telemetry history.")
        return repository.get_history()

    def get_latest(self):
        logger.info("Fetching latest telemetry packet.")
        return repository.get_latest()

    def get_statistics(self):
        logger.info("Fetching telemetry statistics.")
        return repository.get_statistics()
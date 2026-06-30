from app.alerts.alert_service import AlertService

alert_service = AlertService()

class TelemetryService:

    def process(self, telemetry):

        alerts = alert_service.check_alert(telemetry)

        return {
            "status":"success",
            "alerts":alerts,
            "message":"Telemetry processed successfully."
        }
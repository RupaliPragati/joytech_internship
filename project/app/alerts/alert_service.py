class AlertService:

    def check_alert(self, telemetry):

        alerts = []

        if telemetry.temperature > 60:
            alerts.append("High Temperature")

        if telemetry.cpu_usage > 90:
            alerts.append("High CPU Usage")

        if telemetry.signal_strength < 20:
            alerts.append("Weak Signal")

        return alerts
class TelemetryService:

    @staticmethod
    def process(data):
        return {
            "status": "received",
            "satellite_id": data.satellite_id
        }
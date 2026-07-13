from pathlib import Path

from src.backend_telemetry_model import BackendTelemetryScorer


class ModelLoader:
    """
    Loads the trained backend telemetry model once and
    provides access throughout the application.
    """

    def __init__(self):
        self.model = BackendTelemetryScorer(
            Path("models_saved/backend_telemetry_isoforest.joblib")
        )

    def get_model(self):
        return self.model


# Singleton instance
model_loader = ModelLoader()
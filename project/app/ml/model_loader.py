from app.core.config import settings
from src.backend_telemetry_model import BackendTelemetryScorer


class ModelLoader:
    def __init__(self):
        self.model = None

    def load_model(self):
        self.model = BackendTelemetryScorer(settings.MODEL_PATH)
        return self.model

    def get_model(self):
        if self.model is None:
            self.load_model()
        return self.model


model_loader = ModelLoader()
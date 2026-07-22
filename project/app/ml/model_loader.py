from app.core.config import settings
import joblib


class ModelLoader:
    def __init__(self):
        self.model = None

    def load_model(self):
        self.model = joblib.load(settings.MODEL_PATH)
        return self.model

    def get_model(self):
        if self.model is None:
            self.load_model()
        return self.model


model_loader = ModelLoader()
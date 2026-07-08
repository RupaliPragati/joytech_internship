from pathlib import Path
from src.models.isolation_forest import MultiChannelIsolationForest


class ModelLoader:
    """
    Loads the trained ML model once and provides
    access to it throughout the application.
    """

    def __init__(self):
        self.model = MultiChannelIsolationForest.load(
            Path("models_saved/isoforest_all_channels_with_scalers.joblib")
        )

    def get_model(self):
        return self.model


# Singleton instance
model_loader = ModelLoader()
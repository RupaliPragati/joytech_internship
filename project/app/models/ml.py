from pydantic import BaseModel


class MLPrediction(BaseModel):
    is_anomaly: bool
    confidence: float
    risk_level: str


class MLInferenceResponse(BaseModel):
    model_name: str
    model_version: str
    prediction: MLPrediction
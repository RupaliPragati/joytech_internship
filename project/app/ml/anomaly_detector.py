import numpy as np

from app.ml.model_loader import model_loader
from app.ml.telemetry_buffer import telemetry_buffer

from src.inference.live_window import preprocess_live_window


class AnomalyDetector:
    """
    Handles live anomaly prediction using the trained
    Isolation Forest model.
    """

    def predict(self, telemetry):

        # TODO: Confirm with ML team whether satellite_id
        # or channel_id should be used.
        ch_id = telemetry.satellite_id

        # Convert telemetry packet into feature vector
        feature_vector = [
            telemetry.battery_voltage,
            telemetry.temperature,
            telemetry.cpu_usage,
            telemetry.signal_strength,
        ]

        # Store packet in rolling buffer
        telemetry_buffer.add_packet(ch_id, feature_vector)

        # Wait until enough packets are collected
        if not telemetry_buffer.is_ready(ch_id):
            return {
                "status": "waiting",
                "message": "Collecting telemetry packets before prediction.",
                "packets_received": len(
                    telemetry_buffer.buffers[ch_id]
                ),
            }

        # Get rolling window
        raw_buffer = telemetry_buffer.get_buffer(ch_id)

        # Load trained model
        manager = model_loader.get_model()

        # Convert telemetry window into model features
        X_test = preprocess_live_window(
            ch_id,
            raw_buffer,
            manager
        )

        # Run prediction
        result = manager.predict(ch_id, X_test)

        return {
            "model_name": "Isolation Forest",
            "prediction": {
                "is_anomaly": bool(result["is_anomaly"][0]),
                "score": float(result["score"][0]),
                "label": int(result["label"][0]),
            },
        }
from collections import deque
import numpy as np

from src.utils.config import WINDOW_SIZE


class TelemetryBuffer:
    """
    Maintains a rolling buffer of telemetry feature vectors
    for each channel.
    """

    def __init__(self):
        self.buffers = {}

    def add_packet(self, channel_id, feature_vector):
        """
        Store one telemetry feature vector for a channel.
        """

        if channel_id not in self.buffers:
            self.buffers[channel_id] = deque(maxlen=WINDOW_SIZE)

        self.buffers[channel_id].append(feature_vector)

    def is_ready(self, channel_id):
        """
        Returns True once WINDOW_SIZE packets are collected.
        """

        return (
            channel_id in self.buffers
            and len(self.buffers[channel_id]) == WINDOW_SIZE
        )

    def get_buffer(self, channel_id):
        """
        Returns the rolling telemetry window as a NumPy array.
        Shape:
            (WINDOW_SIZE, n_features)
        """

        if channel_id not in self.buffers:
            return np.empty((0, 0))

        return np.array(self.buffers[channel_id], dtype=float)


telemetry_buffer = TelemetryBuffer()
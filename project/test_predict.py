import requests
from datetime import datetime

URL = "http://127.0.0.1:8000/predict"
# If you're using the GitHub tunnel instead of localhost, replace with the tunnel URL.

for i in range(125):
    payload = {
        "satellite_id": "SAT-001",
        "timestamp": datetime.now().isoformat(),
        "battery_voltage": 12.4,
        "temperature": 38.2,
        "cpu_usage": 43,
        "signal_strength": 91,
    }

    response = requests.post(URL, json=payload)

    print(f"\nPacket {i+1}")
    print("Status Code:", response.status_code)

    try:
        print(response.json())
    except Exception:
        print(response.text)
        break
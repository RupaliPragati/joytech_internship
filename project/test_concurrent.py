import threading
import requests
from datetime import datetime

URL = "http://127.0.0.1:8000/predict"


def send_request(i):
    payload = {
        "satellite_id": f"SAT-{i%3}",
        "timestamp": datetime.now().isoformat(),
        "battery_voltage": 12.5,
        "temperature": 35,
        "cpu_usage": 45,
        "signal_strength": 90,
    }

    response = requests.post(URL, json=payload)

    print(f"Request {i}: {response.status_code}")


threads = []

for i in range(20):
    t = threading.Thread(target=send_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nConcurrent testing completed successfully.")
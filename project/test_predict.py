import requests
import time

BASE_URL = "http://127.0.0.1:8000"

LOGIN_URL = f"{BASE_URL}/api/v1/login"
PREDICT_URL = f"{BASE_URL}/api/v1/predict"

# Change these if your credentials are different
USERNAME = "admin"
PASSWORD = "admin123"

# Your BackendTelemetryScorer requires 120 packets
WINDOW_SIZE = 120


def login():
    """Authenticate and get JWT token"""

    response = requests.post(
        LOGIN_URL,
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "username": USERNAME,
            "password": PASSWORD
        }
    )

    if response.status_code != 200:
        print(" Login Failed")
        print("Status Code:", response.status_code)
        print(response.text)
        exit()

    token = response.json()["access_token"]

    print("Login Successful")
    print()

    return token


def send_packets(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    satellite_id = "SAT-001"

    for i in range(1, WINDOW_SIZE + 1):

        telemetry = {
            "satellite_id": satellite_id,
            "timestamp": f"2026-07-23T12:{i % 60:02d}:00Z",
            "battery_voltage": 12.5,
            "temperature": 35.4,
            "cpu_usage": 42.0,
            "signal_strength": 90.0
        }

        response = requests.post(
            PREDICT_URL,
            json=telemetry,
            headers=headers
        )

        print("=" * 60)
        print(f"Packet {i}/{WINDOW_SIZE}")
        print("Status Code:", response.status_code)

        try:
            result = response.json()
            print(result)

            if result.get("status") == "success":
                print("\n🎉 Prediction Completed Successfully!")
                print(result["ml_prediction"])
                break

            elif result.get("status") == "waiting":
                print(
                    f"Waiting... "
                    f"{result['packets_received']}/"
                    f"{result['required_packets']} packets received."
                )

        except Exception:
            print(response.text)

        time.sleep(0.05)


if __name__ == "__main__":
    token = login()
    send_packets(token)

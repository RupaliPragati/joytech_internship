import sqlite3

DATABASE_NAME = "telemetry.db"


class TelemetryRepository:

    def __init__(self):
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(DATABASE_NAME)

    def create_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            satellite_id TEXT,
            timestamp TEXT,
            battery_voltage REAL,
            temperature REAL,
            cpu_usage REAL,
            signal_strength REAL
        )
        """)

        conn.commit()
        conn.close()

    def save(self, telemetry):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO telemetry
        (satellite_id, timestamp, battery_voltage, temperature, cpu_usage, signal_strength)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            telemetry.satellite_id,
            str(telemetry.timestamp),
            telemetry.battery_voltage,
            telemetry.temperature,
            telemetry.cpu_usage,
            telemetry.signal_strength
        ))

        conn.commit()
        conn.close()

    def get_history(self):
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM telemetry")

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]

    def get_latest(self):
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM telemetry
        ORDER BY id DESC
        LIMIT 1
        """)

        row = cursor.fetchone()

        conn.close()

        if row:
            return dict(row)

        return {}

    def get_statistics(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM telemetry")

        total = cursor.fetchone()[0]

        conn.close()

        return {
            "total_packets": total
        }
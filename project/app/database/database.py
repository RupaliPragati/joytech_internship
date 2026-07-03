import sqlite3

DATABASE_NAME = "telemetry.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    conn = get_connection()
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


create_table()
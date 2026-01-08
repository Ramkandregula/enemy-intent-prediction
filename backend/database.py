import sqlite3

conn = sqlite3.connect("satellite_data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS satellite_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    speed REAL,
    distance REAL,
    direction REAL,
    hospitality REAL,
    latitude REAL,
    longitude REAL
)
""")

conn.commit()
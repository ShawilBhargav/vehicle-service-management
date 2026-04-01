import sqlite3

def connect():
    return sqlite3.connect("vehicle_service.db")

def setup_database():
    conn = connect()
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
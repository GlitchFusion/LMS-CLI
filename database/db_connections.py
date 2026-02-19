import sqlite3 as sql
from config import DATABASE_PATH

def get_connection():
    try:
        conn = sql.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    except sql.Error as e:
        print(f"Error connecting to database: {e}")
        return None
import sqlite3
import os

# Ensure DB file is created in current directory
DB_PATH = os.path.join(os.getcwd(), "expenses.db")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)


def create_tables():
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        payment_method TEXT,
        date TEXT
    )
    """)

    conn.commit()
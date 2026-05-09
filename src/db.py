import sqlite3

conn = sqlite3.connect("database/expenses.db", check_same_thread=False)
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        date TEXT,
        category TEXT,
        amount REAL,
        payment_method TEXT,
        description TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
        category TEXT,
        amount REAL
    )
    """)

    conn.commit()
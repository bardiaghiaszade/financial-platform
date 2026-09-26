import sqlite3


def get_connection():
    connection = sqlite3.connect("platform.db")

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT,
            email TEXT UNIQUE NOT NULL,
            user_name TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    connection.commit()

    return connection
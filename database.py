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
            password TEXT NOT NULL,
            verification_code_hash TEXT,
            verification_expires_at TEXT
        )
    """)

    # Add the new columns if the database already existed
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]

    if "verification_code_hash" not in columns:
        cursor.execute("""
            ALTER TABLE users
            ADD COLUMN verification_code_hash TEXT
        """)

    if "verification_expires_at" not in columns:
        cursor.execute("""
            ALTER TABLE users
            ADD COLUMN verification_expires_at TEXT
        """)

    connection.commit()

    return connection
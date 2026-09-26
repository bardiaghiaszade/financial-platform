from database import get_connection
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(first_name, last_name, phone_number, email, user_name, password):

    hashed_password = generate_password_hash(password)

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (first_name, last_name, phone_number, email, user_name, password)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (first_name, last_name, phone_number, email, user_name, hashed_password)
    )

    connection.commit()
    connection.close()


def check_login(email, password):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    connection.close()

    if user and check_password_hash(user[6], password):
        return user

    return None
from database import get_connection


def create_user(first_name, last_name, phone_number, email, user_name, password):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (first_name, last_name, phone_number, email, user_name, password)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (first_name, last_name, phone_number, email, user_name, password)
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
        WHERE email = ? AND password = ?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    connection.close()

    return user
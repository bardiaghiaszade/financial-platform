from database import get_connection


def create_user(name, email, password):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        (name, email, password)
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
from database import get_connection
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(
    first_name,
    last_name,
    phone_number,
    email,
    user_name,
    password
):
    hashed_password = generate_password_hash(password)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (
            first_name,
            last_name,
            phone_number,
            email,
            user_name,
            password
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            first_name,
            last_name,
            phone_number,
            email,
            user_name,
            hashed_password
        )
    )

    connection.commit()

    user_id = cursor.lastrowid

    connection.close()

    return user_id


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


def get_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    connection.close()

    return user


def get_user_by_email(email):
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

    return user


def save_verification_code(user_id, code_hash, expires_at):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET verification_code_hash = ?,
            verification_expires_at = ?
        WHERE id = ?
        """,
        (
            code_hash,
            expires_at,
            user_id
        )
    )

    connection.commit()
    connection.close()


def verify_code(user_id, code):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT verification_code_hash,
               verification_expires_at
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    result = cursor.fetchone()

    connection.close()

    if not result:
        return False

    code_hash = result[0]
    expires_at = result[1]

    if not code_hash or not expires_at:
        return False

    if not check_password_hash(code_hash, code):
        return False

    return True


def clear_verification_code(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET verification_code_hash = NULL,
            verification_expires_at = NULL
        WHERE id = ?
        """,
        (user_id,)
    )

    connection.commit()
    connection.close()


def update_password(user_id, new_password):
    hashed_password = generate_password_hash(new_password)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET password = ?
        WHERE id = ?
        """,
        (
            hashed_password,
            user_id
        )
    )

    connection.commit()
    connection.close()
from datetime import datetime, timedelta

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    jsonify,
    session
)

from werkzeug.security import generate_password_hash

from email_service import (
    send_welcome_email,
    send_verification_email
)

from auth import (
    create_user,
    check_login,
    get_user_by_id,
    get_user_by_email,
    save_verification_code,
    verify_code,
    clear_verification_code,
    update_password
)

from log import setup_logging


# Creating the Object
app = Flask(__name__)

# Secret key for Flask sessions
app.secret_key = "change-this-to-a-random-secret-key"

# Creating a logger
setup_logging(app=app)


# =========================
# PAGE ROUTES
# =========================

@app.route("/")
def home_page():
    return render_template("login.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/signup")
def signup_page():
    return render_template("signup.html")


@app.route("/forgot-password")
def forgot_password_page():
    return render_template("forgotPass.html")


@app.route("/verify-code")
def verify_code_page():
    if not session.get("reset_user_id"):
        return redirect("/forgot-password")

    return render_template("verifyCode.html")


@app.route("/dashboard")
def dashboard_page():
    user_id = session.get("user_id")

    if not user_id:
        return redirect("/login")

    user = get_user_by_id(user_id)

    if not user:
        session.clear()
        return redirect("/login")

    return render_template(
        "dashboard.html",
        user=user
    )


@app.route("/recover-pass")
def reset_password_page():
    if not session.get("reset_verified"):
        return redirect("/forgot-password")

    return render_template("recoverPass.html")


# =========================
# SIGNUP API
# =========================

@app.route("/api/signup", methods=["POST"])
def signup_api():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Credentials missing"
        }), 400

    firstName = data.get("firstName")
    lastName = data.get("lastName")
    phone = data.get("phone")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not all([
        firstName,
        lastName,
        phone,
        email,
        username,
        password
    ]):
        return jsonify({
            "success": False,
            "message": "Credentials missing"
        }), 400

    try:
        user_id = create_user(
            firstName,
            lastName,
            phone,
            email,
            username,
            password
        )

        # Automatically log the user in
        session["user_id"] = user_id

        try:
            send_welcome_email(
                email,
                firstName
            )

            app.logger.info("New User")

        except Exception:
            app.logger.warning(
                "Email connection failed"
            )

    except Exception:
        app.logger.warning(
            "Database failure"
        )

        return jsonify({
            "success": False,
            "message": "Internal Server Error"
        }), 500

    return jsonify({
        "success": True,
        "message": "Signup successful"
    }), 201


# =========================
# LOGIN API
# =========================

@app.route("/api/login", methods=["POST"])
def login_api():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({
            "success": False,
            "message": "Credentials missing"
        }), 400

    user = check_login(
        email,
        password
    )

    if user:
        session["user_id"] = user[0]

        app.logger.info(
            "User logged in"
        )

        return jsonify({
            "success": True,
            "message": "Login successful"
        }), 200

    app.logger.warning(
        "Attempt to login unsuccessful"
    )

    return jsonify({
        "success": False,
        "message": "Wrong email or password"
    }), 401


# =========================
# FORGOT PASSWORD API
# =========================

@app.route("/api/forgotPass", methods=["POST"])
def forgotPass_api():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Email missing"
        }), 400

    email = data.get("email")

    if not email:
        return jsonify({
            "success": False,
            "message": "Email missing"
        }), 400

    user = get_user_by_email(email)

    if not user:
        return jsonify({
            "success": False,
            "message": "No account found with this email"
        }), 404

    try:
        verification_code = send_verification_email(
            email
        )

        verification_code_hash = generate_password_hash(
            verification_code
        )

        expires_at = (
            datetime.utcnow() + timedelta(minutes=10)
        ).isoformat()

        save_verification_code(
            user[0],
            verification_code_hash,
            expires_at
        )

        # Remember which user is resetting password
        session["reset_user_id"] = user[0]

        app.logger.info(
            "Password reset code sent"
        )

        return jsonify({
            "success": True,
            "message": "Verification code sent to your email"
        }), 200

    except Exception:
        app.logger.warning(
            "Failed to send password reset email"
        )

        return jsonify({
            "success": False,
            "message": "Could not send verification email"
        }), 500


# =========================
# VERIFY CODE API
# =========================

@app.route("/api/verify-code", methods=["POST"])
def verify_code_api():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Verification code missing"
        }), 400

    code = data.get("code")

    if not code:
        return jsonify({
            "success": False,
            "message": "Verification code missing"
        }), 400

    user_id = session.get("reset_user_id")

    if not user_id:
        return jsonify({
            "success": False,
            "message": "Password reset session expired"
        }), 401

    user = get_user_by_id(user_id)

    if not user:
        session.clear()

        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    # Get expiration time from database
    connection = None

    try:
        from database import get_connection

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT verification_expires_at
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        )

        result = cursor.fetchone()

    finally:
        if connection:
            connection.close()

    if not result or not result[0]:
        return jsonify({
            "success": False,
            "message": "Verification code expired"
        }), 400

    expires_at = datetime.fromisoformat(
        result[0]
    )

    if datetime.utcnow() > expires_at:
        clear_verification_code(user_id)

        return jsonify({
            "success": False,
            "message": "Verification code expired"
        }), 400

    if not verify_code(user_id, code):
        return jsonify({
            "success": False,
            "message": "Wrong verification code"
        }), 400

    # Code is correct
    session["reset_verified"] = True

    # Code cannot be used again
    clear_verification_code(user_id)

    return jsonify({
        "success": True,
        "message": "Code verified successfully"
    }), 200


# =========================
# RESET PASSWORD API
# =========================

@app.route("/api/reset-password", methods=["POST"])
def reset_password_api():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Password missing"
        }), 400

    new_password = data.get("password")

    if not new_password:
        return jsonify({
            "success": False,
            "message": "Password missing"
        }), 400

    user_id = session.get("reset_user_id")
    reset_verified = session.get("reset_verified")

    if not user_id or not reset_verified:
        return jsonify({
            "success": False,
            "message": "Password reset not authorized"
        }), 401

    user = get_user_by_id(user_id)

    if not user:
        session.clear()

        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    update_password(
        user_id,
        new_password
    )

    # Clear password reset information
    session.pop("reset_user_id", None)
    session.pop("reset_verified", None)

    app.logger.info(
        "Password reset successful"
    )

    return jsonify({
        "success": True,
        "message": "Password reset successful"
    }), 200
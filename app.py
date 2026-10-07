from flask import Flask, render_template, request, redirect, jsonify
from email_service import send_welcome_email
from auth import create_user, check_login
from log import setup_logging

# Creating the Object
app = Flask(__name__)

# Creating a logger
setup_logging(app=app)


# ----------------------------------------Routes----------------------------------------

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

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@app.route("/recover-pass")
def reset_password_page():
    return render_template("recoverPass.html")

# -------------------------------------------------------------------------------------
@app.route("/api/forgotPass", methods=["POST"])
def forgotPass_api():
    
    data = request.get_json()

    if not data:
        return jsonify({
            "success" : False,
            "message" : "Credentials missing"
        }), 400
    
    email = data.get("email")

    if not email:
        return jsonify({
            "success" : False,
            "message" : "Credentials missing"
        }), 400
    




    ######
    ###### search_user(email) if user exists send him the link via mail if not return that such user does not exist, for now i just return false
    ######

    return jsonify({
        "success" : False,
        "message" : "User does not exist"
    }), 400




@app.route("/api/signup", methods=["POST"])
def signup_api():

    data = request.get_json()

    if not data:
        return jsonify({
            "success" : False,
            "message" : "Credentials missing"
        }), 400

    firstName = data.get("firstName")
    lastName = data.get("lastName")
    phone = data.get("phone")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not all([firstName, 
                lastName,
                phone,
                email,
                username,
                password]):
        return jsonify({
            "success" : False,
            "message" : "credentials missing"
        }), 400
    try:
        create_user(
            firstName,
            lastName,
            phone,
            email,
            username,
            password
        )
        try:
            send_welcome_email(
                email,
                firstName
                )
            app.logger.info(f"New User")
        except Exception as e:
            app.logger.warning("Email connection failed")
        
    except Exception as e:
        app.logger.warning("Database failure")
        return jsonify({
            "success" : False,
            "message" : "Internal Server Error"
        }), 500

    return jsonify({
        "success" : True,
        "message" : "Signup successful"
    }), 201


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
            "success" : False,
            "message" : "Credentials missing"
        }), 400
    
    user = check_login(email, password)
    
    if user:
            app.logger.info("User logged in")
            return jsonify({
                "success" : True,
                "message" : "Login successful"
            }), 200
    
    app.logger.warning("Attempt to login unseccesful")
    
    return jsonify({
        "success" : False,
        "message" : "Wrong email or password"
        }), 401
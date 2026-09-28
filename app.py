from flask import Flask, render_template, request, redirect
from email_service import send_welcome_email
from auth import create_user, check_login


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        phone_number = request.form["phone_number"]
        email = request.form["email"]
        user_name = request.form["user_name"]
        password = request.form["password"]

        create_user(
            first_name,
            last_name,
            phone_number,
            email,
            user_name,
            password
        )

        try:
            send_welcome_email(
                email,
                first_name
            )
        except Exception as e:
            print("Welcome email could not be sent because .env was not created (you are dumb!):", e)

        return redirect("/dashboard")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = check_login(email, password)

        if user:
            return redirect("/dashboard")

        return "Wrong email or password"

    return render_template("login.html")


@app.route("/forgot-password")
def forgot_password():
    return render_template("forgotPass.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
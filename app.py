from flask import Flask, render_template, request, redirect

from auth import create_user, check_login


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        create_user(name, email, password)

        return redirect("/login")

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
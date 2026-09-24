from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/forgot-password")
def forgot_password():
    return render_template("forgotPass.html")
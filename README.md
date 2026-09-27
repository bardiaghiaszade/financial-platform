# 🏦 Bank Transaction Platform

A simple web-based banking platform built with **Python and Flask**.
The project provides user registration, login, password hashing, account-related functionality, a personal dashboard, password recovery, SQLite database storage, and email notifications.

> ⚠️ **Educational Project:** This application is intended for learning and development purposes. It is **not** a real banking system and should not be used to process real financial transactions or store real banking credentials.

---

## ✨ Features

* 🔐 User registration and login
* 👤 User account information
* 🔒 Secure password hashing
* 💰 Account balance management
* 💸 Banking transaction functionality
* 📊 Personal dashboard
* 🔑 Password recovery page
* 📧 Welcome email after registration
* 📨 HTML email with an animated GIF
* 🗄️ SQLite database
* 🎨 HTML/CSS web interface
* 🔒 Environment variables for email credentials

---

## 🛡️ Authentication & Security

User passwords are **not stored as plain text**.

During registration, the password is hashed using Werkzeug:

```python
generate_password_hash(password)
```

When the user logs in, the entered password is checked against the stored hash using:

```python
check_password_hash()
```

This means the original password is not stored directly in the database.

The application also uses parameterized SQL queries when inserting and retrieving user information.

---

## 📧 Email Service

After a successful registration, the application can send a welcome email to the user's email address.

The email is sent through **Gmail SMTP** and contains:

* The user's first name
* A welcome message
* An animated GIF

Email credentials are loaded from environment variables using `python-dotenv`.

### Important

Your real email credentials must **never be committed to GitHub**.

The project uses:

```text
.env
```

for real credentials.

The `.env` file is ignored by Git through `.gitignore`.

Instead, the repository contains:

```text
.env.example
```

as a template.

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/bardiaghiaszade/financial-platform.git
cd financial-platform
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If the project dependencies are not yet listed in `requirements.txt`, install the required packages manually:

```bash
pip install flask python-dotenv
```

The project uses:

* Flask
* python-dotenv
* Werkzeug
* SQLite (included with Python)

---

# 🔐 4. Configure the `.env` file

The `.env` file is **not included in the GitHub repository** because it contains private credentials.

After cloning the project, create a new file in the project root:

```text
.env
```

The project should look like:

```text
financial-platform/
│
├── .env
├── .env.example
├── app.py
├── auth.py
├── database.py
├── email_service.py
├── run.py
├── platform.db
├── requirements.txt
├── static/
└── templates/
```

Open `.env` and add your own email credentials:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### Gmail App Password

If you want to use Gmail for the email service:

1. Enable **2-Step Verification** on your Google account.
2. Create a **Google App Password**.
3. Put the generated App Password in `.env`.
4. Do **not** use your normal Gmail password.
5. Never commit `.env` to GitHub.

The `.env.example` file shows the required variables without containing real credentials:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### Why is `.env` not on GitHub?

Because every developer should use their own credentials.

For example:

```text
Developer A
.env
EMAIL_ADDRESS=developerA@gmail.com
EMAIL_PASSWORD=developerA_app_password
```

and:

```text
Developer B
.env
EMAIL_ADDRESS=developerB@gmail.com
EMAIL_PASSWORD=developerB_app_password
```

The Python code stays the same.

---

# ▶️ 5. Run the application

Start the application with:

```bash
python run.py
```

Flask will provide a local address, normally:

```text
http://127.0.0.1:5000
```

Open that address in your browser.

---

# 🗄️ Database

The application uses **SQLite** for local data storage.

The database file is:

```text
platform.db
```

The `users` table contains information such as:

```text
id
first_name
last_name
phone_number
email
user_name
password
```

The email and username fields are unique.

Passwords are stored as hashes rather than plain-text passwords.

The database is intended for **local development and testing**.

---

# 📁 Project Structure

```text
financial-platform/
│
├── app.py                  # Main Flask application
├── run.py                  # Application entry point
├── auth.py                 # Registration and login logic
├── database.py             # SQLite database connection and table creation
├── email_service.py        # Welcome email service
│
├── platform.db             # SQLite database
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Files ignored by Git
├── README.md               # Project documentation
├── TODO.md                 # Future tasks
│
├── static/
│   └── style.css           # Application styles
│
└── templates/
    ├── dashboard.html      # User dashboard
    ├── forgotPass.html     # Password recovery page
    ├── login.html          # Login page
    └── signup.html         # Registration page
```

---

# 🔄 Application Flow

## Registration

```text
User
  ↓
Signup Form
  ↓
Flask
  ↓
create_user()
  ↓
Password Hashing
  ↓
SQLite Database
  ↓
Welcome Email
```

## Login

```text
User
  ↓
Login Form
  ↓
Flask
  ↓
check_login()
  ↓
Find User by Email
  ↓
Check Password Hash
  ↓
Dashboard
```

---

# 🧩 Main Components

### `app.py`

Contains the Flask routes and handles requests from the web interface.

Main routes include:

```text
/
 /signup
 /login
 /forgot-password
 /dashboard
```

### `auth.py`

Handles authentication-related functionality:

* Creating users
* Hashing passwords
* Checking login credentials

### `database.py`

Handles the SQLite connection and creates the `users` table when necessary.

### `email_service.py`

Handles sending welcome emails through Gmail SMTP.

### `run.py`

Starts the Flask application.

---

# 🛡️ Files That Must Not Be Committed

The following files are ignored by Git:

```gitignore
.env
__pycache__/
*.pyc
```

The `.env` file contains private credentials and should remain only on your local machine.

---

# ⚠️ Security Disclaimer

This project is for **educational and development purposes only**.

It is **not a production banking application**.

Do not use this project to:

* Process real financial transactions
* Store real banking credentials
* Store real payment information
* Store sensitive financial data
* Handle real customer accounts

A production banking application would require significantly stronger security controls, authentication, authorization, encryption, auditing, database security, session management, CSRF protection, validation, monitoring, and other security measures.

---

# 🔮 Future Improvements

* [ ] Detailed transaction history
* [ ] Account-to-account transfers
* [ ] Improved password recovery functionality
* [ ] Email verification
* [ ] Better authentication and session management
* [ ] Transaction notifications
* [ ] Improved dashboard
* [ ] Better input validation
* [ ] Automated tests
* [ ] Improved error handling
* [ ] Improved UI/UX
* [ ] Production-ready email service
* [ ] Database migrations
* [ ] More advanced security controls

---

# 📄 License

This project is intended for **educational and personal use**.

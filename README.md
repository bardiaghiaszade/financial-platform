🏦 Bank Transaction Platform


<img width="2527" height="1181" alt="Screenshot 2026-09-24 at 12 07 15" src="https://github.com/user-attachments/assets/9c048611-c456-4ed0-940a-9e819ec91c12" />



A simple web-based banking platform built with Python and Flask. The project provides basic user authentication, account management, and banking functionality through a web interface.

✨ Features

🔐 User registration and login

💰 Account balance management

💸 Bank transaction functionality

📊 Personal dashboard

🔑 Password recovery

🗄️ SQLite database

🎨 Simple web interface

🛠️ Technologies

Python 3

Flask

SQLite

HTML5

CSS3

```text
📁 Project Structure
.
├── app.py                 # Main Flask application
├── run.py                 # Application entry point
├── requirements.txt       # Python dependencies
├── platform.db            # SQLite database
│
├── static/
│   └── style.css          # Application styles
│
├── templates/
│   ├── dashboard.html     # User dashboard
│   ├── forgotPass.html    # Password recovery page
│   ├── login.html         # Login page
│   └── signup.html        # Registration page
│
└── README.md              # Project documentation

```
🚀 Getting Started
1. Clone the repository
git clone <your-repository-url>
cd <project-folder>

2. Create a virtual environment
python -m venv venv


Activate the virtual environment:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python run.py


Then open the local address provided by Flask in your browser.

🗄️ Database

The application uses SQLite for data storage.

The database file is:

platform.db


The database is intended for local development and testing.

⚠️ Disclaimer

This project was created for educational and development purposes only.

It is not intended to process real financial transactions or store real banking credentials or sensitive financial information.

🔮 Future Improvements

Add detailed transaction history

Add account-to-account transfers

Improve authentication and security

Add transaction notifications

Improve the user interface

Add automated tests

📄 License

This project is intended for educational and personal use.

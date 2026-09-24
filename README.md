🏦 Bank Transaction Platform

A simple web-based banking platform built with Python. The application provides basic account management and banking functionality through a clean and simple web interface.

✨ Features

🔐 User registration and login

💰 Account balance management

💸 Bank transaction handling

📊 User dashboard

🔑 Password recovery

🗄️ SQLite database integration

🎨 Simple responsive web interface

🛠️ Tech Stack

Python 3

Flask

SQLite

HTML5

CSS3

📁 Project Structure
Bank-Transaction-Platform/
│
├── app.py                 # Main application
├── run.py                 # Application entry point
├── requirements.txt       # Python dependencies
├── platform.db            # SQLite database
│
├── static/
│   └── style.css          # Application styles
│
├── templates/
│   ├── dashboard.html     # User dashboard
│   ├── forgotPass.html    # Password recovery
│   ├── login.html         # Login page
│   └── signup.html        # Registration page
│
└── README.md

🚀 Getting Started
1. Clone the repository
git clone <your-repository-url>
cd <project-folder>

2. Create a virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python run.py


Then open the local URL shown in your terminal.

🗄️ Database

The application uses SQLite for storing application data. The database file is:

platform.db


For development, the database is stored locally within the project.

⚠️ Disclaimer

This project was created for educational and development purposes. It is not intended to process real financial transactions or store real banking credentials or sensitive financial information.

📌 Future Improvements

Add transaction history

Improve authentication and security

Add account-to-account transfers

Add transaction notifications

Improve UI/UX

Add automated tests

📄 License

This project is for educational and personal use.
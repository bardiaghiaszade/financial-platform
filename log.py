import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(app):
    # Finding the root directory
    log_dir = os.path.join(app.root_path, "logs")
    
    # Making the directory if it does not exist
    os.makedirs(log_dir, exist_ok=True)

    # Creating the log file
    log_file = os.path.join(log_dir, "app.log")

    # Handler is just who actually handles all the logging as the name says
    # All before this was just finding the directory and now initiallizing it
    # It will be logging till 5 Mb volume then it will be logging in next file app.log2 ...
    handler = RotatingFileHandler(
              log_file,
              maxBytes= 5 * 1024 * 1024,
              backupCount=5
    )

    # Formatting the log lines e.g. 2025.12.03 12:25 | INFO | app | User Logged in
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
    )
    handler.setLevel(logging.INFO)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    return app
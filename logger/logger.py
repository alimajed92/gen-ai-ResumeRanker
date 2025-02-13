import logging
import os
from datetime import datetime


def setup_logger(name):
    # logging folder
    log_dir = "logs"

    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a custom logger
    logger = logging.getLogger(name)

    # Set the default log level
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    log_filename = os.path.join(log_dir, datetime.now().strftime("%Y-%m-%d") + ".log")
    f_handler = logging.FileHandler(log_filename)

    # Set level for handlers
    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to handlers
    c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


app_logger = setup_logger("app_logger")

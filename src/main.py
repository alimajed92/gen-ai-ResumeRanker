from logger.logger import setup_logger, app_logger
from exceptions.exceptions import AppException
import sys
from dotenv import load_dotenv
import os
from config import CVS_DIR


app_logger.info(CVS_DIR)
example_variable = "Hello, World!"


def main():
    print("this is from main application")


if __name__ == "__main__":
    app_logger.info("this is from main")

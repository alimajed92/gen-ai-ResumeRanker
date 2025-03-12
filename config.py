from dotenv import load_dotenv
import os
from pathlib import Path
from exceptions.exceptions import AppException
from logger.logger import app_logger

# Load environment variables
load_dotenv()


class Config:
    """Application Configuration Class"""

    BASE_DIR = Path(__file__).resolve().parent
    OLLAMA_API = os.getenv(
        "OLLAMA_API", "default_api_url"
    )  # Set a default if not provided
    MODEL_NAME = os.getenv("MODEL_NAME", "gemma2:27b")
    CVS_DIR = BASE_DIR / "cvs"

    @classmethod
    def validate(cls):
        """Ensure that required settings are available."""
        try:
            if cls.OLLAMA_API is None:
                raise AppException("OLLAMA_API is not set in environment variables")

            if cls.CVS_DIR is None:
                raise AppException("Foldername is not set in environment variables")

        except AppException as e:
            app_logger.error(f"Configuration Validation Error: {str(e)}")
            raise

    @classmethod
    def display(cls):
        """Display configuration for debugging purposes."""
        app_logger.info(f"Base Directory: {cls.BASE_DIR}")
        app_logger.info(f"Ollama API: {cls.OLLAMA_API}")
        app_logger.info(f"Model Name: {cls.MODEL_NAME}")
        app_logger.info(f"CVS Directory: {cls.CVS_DIR}")


if __name__ == "__main__":
    Config.validate()
    Config.display()

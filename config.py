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
        app_logger.info("Validating Configuration...")
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
        # Define ANSI color codes
        BLUE = "\033[94m"  # Blue for labels
        YELLOW = "\033[93m"  # Yellow for variable values
        RESET = "\033[0m"  # Reset color to default
        app_logger.info("Configuration Details:")
        app_logger.info(f"{YELLOW}Base Directory:{RESET} {BLUE}{cls.BASE_DIR}{RESET}")
        app_logger.info(f"{YELLOW}Ollama API:{RESET} {BLUE}{cls.OLLAMA_API}{RESET}")
        app_logger.info(f"{YELLOW}Model Name:{RESET} {BLUE}{cls.MODEL_NAME}{RESET}")
        app_logger.info(f"{YELLOW}CVS Directory:{RESET} {BLUE}{cls.CVS_DIR}{RESET}")


if __name__ == "__main__":
    # Config.validate()
    # Config.display()
    pass

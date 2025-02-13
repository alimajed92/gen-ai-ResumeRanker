from dotenv import load_dotenv
import os

load_dotenv()
from pathlib import Path

# Get the current script's directory (assuming this script is inside the main project folder)
BASE_DIR = Path(__file__).resolve().parent
OLLAMA_API = os.getenv("OLLAMA_API")
MODEL_NAME = "gemma2:27b"

# Path to the 'cvs' folder dynamically
CVS_DIR = BASE_DIR / "cvs"


if __name__ == "__main__":
    pass

import os
import subprocess
import sys


def create_virtualenv():
    """Create a virtual environment."""
    subprocess.check_call([sys.executable, "-m", "venv", "env"])


def activate_virtualenv():
    """Activate the virtual environment."""
    if os.name == "nt":
        activate_script = os.path.join("env", "Scripts", "activate.bat")
    else:
        activate_script = os.path.join("env", "bin", "activate")
    print(f"To activate the virtual environment, run '{activate_script}'")


def install_requirements():
    """Install the required dependencies from all requirements files in the requirements folder."""
    requirements_folder = "requirements"
    for filename in os.listdir(requirements_folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(requirements_folder, filename)
            subprocess.check_call(
                [os.path.join("env", "Scripts", "pip"), "install", "-r", filepath]
            )


def run_application():
    """Run the application."""
    subprocess.check_call([os.path.join("env", "Scripts", "python"), "run.py"])


def main():
    """Main setup script."""
    print("Creating virtual environment...")
    create_virtualenv()
    print("Virtual environment created.")

    activate_virtualenv()
    print("Installing dependencies...")

    install_requirements()
    print("Dependencies installed.")

    user_input = input("Do you want to run the application now? (Y/N): ")
    if user_input.lower() == "y":
        run_application()


if __name__ == "__main__":
    main()

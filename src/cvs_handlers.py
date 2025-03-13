from config import Config
import os
from logger.logger import app_logger

uploaded = False


def file_upload_handler(uploaded_files):
    """
    Handles file uploads.

    Parameters:
        uploaded_files (list): List of uploaded files.

    Returns:
        None
    """
    # Check if the upload folder exists
    if not os.path.exists(Config.CVS_DIR):
        os.makedirs(Config.CVS_DIR)

    # Loop through the uploaded
    for uploaded_file in uploaded_files:
        # Check if it's a PDF (already handled by `type=["pdf"]`)
        if uploaded_file.name.endswith(".pdf"):
            # Define the file path
            file_path = os.path.join(Config.CVS_DIR, uploaded_file.name)

            # Save the file
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())
                app_logger.info(f"File saved: {file_path}")
                uploaded = True
            return uploaded

        else:
            app_logger.warning(f"Invalid file format: {uploaded_file.name}")
            uploaded = False
            return uploaded

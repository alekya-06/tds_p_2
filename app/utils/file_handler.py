import os
import shutil
import tempfile
import logging
from fastapi import UploadFile
import httpx

logging.basicConfig(level=logging.INFO)

async def save_upload_file_temporarily(upload_file: UploadFile) -> str:
    """
    Save an uploaded file temporarily and return the path to the saved file.
    """
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, upload_file.filename)

        # Save the file
        with open(file_path, "wb") as f:
            contents = await upload_file.read()
            f.write(contents)

        logging.info(f"File saved temporarily at: {file_path}")
        return file_path
    except Exception as e:
        logging.error(f"Error saving file: {str(e)}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise e

async def read_saved_file(file_path: str) -> str:
    """
    Read the content of the saved file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        raise e

async def delete_temp_file(file_path: str):
    """
    Delete the temporary file and its directory.
    """
    try:
        dir_path = os.path.dirname(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        logging.info(f"Temporary file and directory deleted: {file_path}")
    except Exception as e:
        logging.error(f"Error deleting file {file_path}: {str(e)}")
        raise e


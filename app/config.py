import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# OpenAI API configuration
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
AIPROXY_BASE_URL = os.getenv("AIPROXY_BASE_URL")

# Other configurations
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./uploads")
TEMP_FOLDER = os.getenv("TEMP_FOLDER", "./temp")

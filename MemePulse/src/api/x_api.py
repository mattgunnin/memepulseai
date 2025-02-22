from dotenv import load_dotenv
import os

load_dotenv()

def get_x_credentials():
    return {
        "api_key": os.getenv("X_API_KEY"),
        "api_secret": os.getenv("X_API_SECRET"),
        "access_token": os.getenv("X_ACCESS_TOKEN"),
        "access_secret": os.getenv("X_ACCESS_SECRET")
    }
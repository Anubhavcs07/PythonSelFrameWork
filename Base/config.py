import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://rahulshettyacademy.com/loginpagePractise/")
    ENV_NAME = os.getenv("ENV", "prod")

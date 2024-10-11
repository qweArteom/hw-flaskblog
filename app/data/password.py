import os

from dotenv import load_dotenv


load_dotenv()

ADMIN_PASS = os.getenv("ADMIN_PASS")

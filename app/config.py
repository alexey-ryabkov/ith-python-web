import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_DATABASE", "match_result"),
    "port": int(os.getenv("DB_PORT", "3306")),
}

FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))

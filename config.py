import logging
import os
from pathlib import Path

BOT_TOKEN = os.getenv("BOT_TOKEN")

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "db.sqlite3"
SQLA_DB_URI = f"sqlite+aiosqlite:///{DB_PATH}"

logging.basicConfig(level=logging.INFO)

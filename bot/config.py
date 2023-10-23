import logging
import os
from pathlib import Path

BOT_TOKEN = os.getenv("BOT_TOKEN")

BASE_DIR = Path(__file__).parent
MEDIA_DIR = BASE_DIR / "media"
DOCUMENTS_DIR = MEDIA_DIR / "documents"
CHATS_ZIP_PATH = MEDIA_DIR / "chats_data.zip"

CONULT_FORM = "https://forms.wix.com/f/6988831737677611262"
EMAIL = "nativcentre@gmail.com"

DB_PATH = BASE_DIR / "db.sqlite3"
SQLA_DB_URI = f"sqlite+aiosqlite:///{DB_PATH}"

LATITUDE = 60.004934811312374
LONGITUDE = 30.197177012066668

logging.basicConfig(level=logging.INFO)

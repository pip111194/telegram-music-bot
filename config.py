import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    
    # Music Settings
    DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "900"))  # 15 minutes
    SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", "600"))  # 10 minutes
    
    # Bot Settings
    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "")
    SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "")

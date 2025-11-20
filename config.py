import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram Configuration
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # Database
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
    
    # Bot Settings
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    
    # Music Platform API Keys
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")
    SOUNDCLOUD_CLIENT_ID = os.getenv("SOUNDCLOUD_CLIENT_ID", "")
    
    # Music Settings
    DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "900"))  # 15 minutes
    SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", "600"))  # 10 minutes
    
    # Bot Settings
    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "")
    SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "")
    
    # Platform Settings
    ENABLE_SPOTIFY = os.getenv("ENABLE_SPOTIFY", "true").lower() == "true"
    ENABLE_APPLE_MUSIC = os.getenv("ENABLE_APPLE_MUSIC", "true").lower() == "true"
    ENABLE_SOUNDCLOUD = os.getenv("ENABLE_SOUNDCLOUD", "true").lower() == "true"
    ENABLE_DEEZER = os.getenv("ENABLE_DEEZER", "true").lower() == "true"
    ENABLE_YOUTUBE = os.getenv("ENABLE_YOUTUBE", "true").lower() == "true"

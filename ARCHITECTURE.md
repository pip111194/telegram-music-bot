# 🏗️ System Architecture / सिस्टम आर्किटेक्चर

## 📊 Project Structure / प्रोजेक्ट संरचना

```
telegram-music-bot/
│
├── bot.py                      # Main entry point / मुख्य एंट्री पॉइंट
├── config.py                   # Configuration / कॉन्फ़िगरेशन
├── requirements.txt            # Dependencies / डिपेंडेंसीज
├── .env.example               # Environment template / एनवायरनमेंट टेम्पलेट
├── .gitignore                 # Git ignore file
│
├── README.md                  # Project overview / प्रोजेक्ट ओवरव्यू
├── SETUP.md                   # Setup guide / सेटअप गाइड
├── PLATFORMS.md               # Platform details / प्लेटफॉर्म विवरण
├── ARCHITECTURE.md            # This file / यह फ़ाइल
│
├── handlers/                  # Command handlers / कमांड हैंडलर्स
│   ├── __init__.py           # Module init
│   ├── music.py              # Music playback commands
│   ├── admin.py              # Admin commands
│   ├── misc.py               # Miscellaneous commands
│   ├── platforms.py          # Platform-specific handlers
│   └── free_platforms.py     # Free platform handlers
│
├── helpers/                   # Helper modules / हेल्पर मॉड्यूल्स
│   ├── __init__.py           # Module init
│   │
│   ├── music_platforms.py    # Unified platform manager
│   │
│   ├── spotify.py            # Spotify API integration
│   ├── apple_music.py        # Apple Music API
│   ├── soundcloud.py         # SoundCloud API
│   ├── deezer.py             # Deezer API
│   ├── ytdl.py               # YouTube downloader
│   │
│   ├── jiosaavn.py           # JioSaavn API (Free!)
│   ├── gaana.py              # Gaana API (Free!)
│   ├── wynk.py               # Wynk Music API (Free!)
│   ├── jamendo.py            # Jamendo API (Free!)
│   ├── audiomack.py          # Audiomack API (Free!)
│   │
│   ├── decorators.py         # Function decorators
│   ├── filters.py            # Custom filters
│   ├── database.py           # MongoDB operations
│   └── call_manager.py       # Voice call management
│
└── downloads/                 # Downloaded audio files
```

---

## 🔄 System Flow / सिस्टम फ्लो

### 1. Bot Initialization / बॉट इनिशियलाइज़ेशन
```
bot.py
  ↓
Load .env → config.py
  ↓
Initialize Pyrogram Client
  ↓
Load handlers/ plugins
  ↓
Connect to MongoDB
  ↓
Bot Ready ✅
```

### 2. Command Processing / कमांड प्रोसेसिंग
```
User sends: /jiosaavn Kesariya
  ↓
handlers/free_platforms.py → jiosaavn_search()
  ↓
helpers/music_platforms.py → search_platform("jiosaavn", "Kesariya")
  ↓
helpers/jiosaavn.py → search()
  ↓
API Request to JioSaavn
  ↓
Return results (5 songs)
  ↓
Display inline buttons
  ↓
User selects song
  ↓
handlers/platforms.py → platform_callback()
  ↓
helpers/music_platforms.py → get_download_url()
  ↓
helpers/jiosaavn.py → get_download_url()
  ↓
Download audio file
  ↓
helpers/call_manager.py → start_call()
  ↓
Play in voice chat ✅
```

### 3. Multi-Platform Search / मल्टी-प्लेटफॉर्म सर्च
```
User sends: /search Kesariya
  ↓
handlers/platforms.py → search_all_platforms()
  ↓
helpers/music_platforms.py → search_all_platforms()
  ↓
Parallel search on all enabled platforms:
  ├── JioSaavn
  ├── Gaana
  ├── Wynk
  ├── Spotify
  ├── YouTube
  └── Others
  ↓
Collect all results
  ↓
Display formatted results
  ↓
User can use platform-specific command
```

---

## 🧩 Module Details / मॉड्यूल विवरण

### 1. **bot.py** - Main Entry Point
**Purpose:** Bot initialization और startup  
**Key Functions:**
- `MusicBot.__init__()` - Bot configuration
- `MusicBot.start()` - Bot startup
- `MusicBot.stop()` - Bot shutdown

**Flow:**
```python
1. Load environment variables
2. Initialize Pyrogram client
3. Load all handlers as plugins
4. Start bot
5. Print success message
```

---

### 2. **config.py** - Configuration Manager
**Purpose:** सभी settings को centralize करना  
**Key Components:**
- Telegram credentials
- Database connection
- Platform enable/disable flags
- API keys (optional)

**Usage:**
```python
from config import Config

api_id = Config.API_ID
spotify_enabled = Config.ENABLE_SPOTIFY
```

---

### 3. **handlers/** - Command Handlers

#### **music.py** - Basic Music Commands
**Commands:**
- `/play <song>` - YouTube से play
- `/pause` - Pause playback
- `/resume` - Resume playback
- `/skip` - Skip song
- `/stop` - Stop playback
- `/queue` - Show queue

#### **platforms.py** - Platform-Specific Commands
**Commands:**
- `/spotify <song>` - Spotify search
- `/apple <song>` - Apple Music search
- `/soundcloud <song>` - SoundCloud search
- `/deezer <song>` - Deezer search
- `/search <song>` - All platforms

**Key Functions:**
- `spotify_search()` - Spotify handler
- `apple_music_search()` - Apple Music handler
- `platform_callback()` - Button callback handler

#### **free_platforms.py** - Free Platform Commands
**Commands:**
- `/jiosaavn <song>` - JioSaavn search
- `/gaana <song>` - Gaana search
- `/wynk <song>` - Wynk search
- `/jamendo <song>` - Jamendo search
- `/audiomack <song>` - Audiomack search

**Key Functions:**
- `jiosaavn_search()` - JioSaavn handler
- `gaana_search()` - Gaana handler
- `wynk_search()` - Wynk handler

#### **admin.py** - Admin Commands
**Commands:**
- `/stats` - Bot statistics
- `/broadcast <msg>` - Broadcast message

#### **misc.py** - Miscellaneous Commands
**Commands:**
- `/start` - Welcome message
- `/help` - Help message
- `/about` - About bot

---

### 4. **helpers/** - Helper Modules

#### **music_platforms.py** - Unified Platform Manager
**Purpose:** सभी platforms को manage करना  
**Key Class:** `MusicPlatformManager`

**Key Methods:**
```python
search_platform(platform, query, limit)
  → Specific platform पर search

search_all_platforms(query, limit)
  → सभी enabled platforms पर search

get_download_url(platform, track_info)
  → Download URL प्राप्त करना

is_platform_enabled(platform)
  → Platform enabled है या नहीं

get_platform_emoji(platform)
  → Platform का emoji

get_platform_name(platform)
  → Platform का display name
```

**Usage:**
```python
from helpers.music_platforms import music_manager

# Single platform search
results = await music_manager.search_platform("jiosaavn", "Kesariya", 5)

# All platforms search
all_results = await music_manager.search_all_platforms("Kesariya", 3)

# Get download URL
url = await music_manager.get_download_url("jiosaavn", track_info)
```

#### **Platform-Specific Helpers**

##### **jiosaavn.py** - JioSaavn Integration
**API:** Public API (No key required)  
**Key Methods:**
```python
search(query, limit) → List[Dict]
get_song_details(song_id) → Dict
get_download_url(song_id) → str
```

##### **gaana.py** - Gaana Integration
**API:** Public API (No key required)  
**Key Methods:**
```python
search(query, limit) → List[Dict]
get_song_details(track_id) → Dict
get_download_url(track_id) → str
```

##### **wynk.py** - Wynk Music Integration
**API:** Public API (No key required)  
**Key Methods:**
```python
search(query, limit) → List[Dict]
get_song_details(song_id) → Dict
get_download_url(song_id) → str
```

##### **jamendo.py** - Jamendo Integration
**API:** Optional API key  
**Key Methods:**
```python
search(query, limit) → List[Dict]
get_song_details(track_id) → Dict
get_download_url(track_id) → str
```

##### **audiomack.py** - Audiomack Integration
**API:** Optional API key  
**Key Methods:**
```python
search(query, limit) → List[Dict]
get_song_details(song_id) → Dict
get_download_url(song_id) → str
```

##### **spotify.py** - Spotify Integration
**API:** Optional API key (recommended)  
**Key Methods:**
```python
search_track(query, limit) → List[Dict]
get_track_info(track_id) → Dict
```

##### **ytdl.py** - YouTube Downloader
**Library:** yt-dlp  
**Key Methods:**
```python
search(query, limit) → List[Dict]
download(url) → Tuple[str, Dict]
```

#### **decorators.py** - Function Decorators
**Decorators:**
- `@authorized_users_only` - Admin-only commands
- `@errors` - Error handling wrapper

#### **filters.py** - Custom Filters
**Filters:**
- `command()` - Custom command filter

#### **database.py** - MongoDB Operations
**Key Functions:**
- Database connection
- User management
- Statistics tracking

#### **call_manager.py** - Voice Call Management
**Key Functions:**
- `start_call()` - Start voice chat
- `pause_call()` - Pause playback
- `resume_call()` - Resume playback
- `stop_call()` - Stop playback

---

## 🔐 Security / सुरक्षा

### Environment Variables
- सभी sensitive data `.env` में
- `.env` को `.gitignore` में add करें
- Production में strong credentials use करें

### Admin Controls
- Admin-only commands के लिए decorators
- Owner ID verification
- Group admin verification

### API Rate Limiting
- Platform APIs के rate limits का ध्यान
- Retry logic implement करें
- Error handling properly करें

---

## 📊 Data Flow / डेटा फ्लो

### Search Flow
```
User Input
  ↓
Command Handler
  ↓
Platform Manager
  ↓
Platform API Helper
  ↓
HTTP Request
  ↓
API Response
  ↓
Parse & Format
  ↓
Return Results
  ↓
Display to User
```

### Download Flow
```
User Selection
  ↓
Get Track Info
  ↓
Get Download URL
  ↓
Download Audio
  ↓
Save to downloads/
  ↓
Start Voice Call
  ↓
Play Audio
  ↓
Update Queue
```

---

## 🔧 Error Handling / एरर हैंडलिंग

### Levels of Error Handling

1. **API Level**
```python
try:
    response = await session.get(url)
    if response.status != 200:
        return []
except Exception as e:
    print(f"API Error: {e}")
    return []
```

2. **Platform Level**
```python
try:
    results = await platform_api.search(query)
except Exception as e:
    print(f"Platform Error: {e}")
    return None
```

3. **Handler Level**
```python
@errors
async def command_handler():
    try:
        # Command logic
    except Exception as e:
        await message.reply(f"Error: {e}")
```

---

## 🚀 Performance Optimization / परफॉर्मेंस ऑप्टिमाइज़ेशन

### 1. Async Operations
- सभी API calls async हैं
- Parallel platform searches
- Non-blocking downloads

### 2. Session Management
- Reuse aiohttp sessions
- Connection pooling
- Proper session cleanup

### 3. Caching
- Search results caching (optional)
- Track info caching
- Platform availability caching

### 4. Resource Management
- Downloaded files cleanup
- Memory management
- Database connection pooling

---

## 📈 Scalability / स्केलेबिलिटी

### Horizontal Scaling
- Multiple bot instances
- Load balancing
- Shared database

### Vertical Scaling
- Increase server resources
- Optimize code
- Better caching

### Database Scaling
- MongoDB sharding
- Read replicas
- Indexing

---

## 🧪 Testing / टेस्टिंग

### Unit Tests
```python
# Test platform search
async def test_jiosaavn_search():
    results = await jiosaavn_api.search("Kesariya", 5)
    assert len(results) > 0
    assert results[0]['name'] is not None
```

### Integration Tests
```python
# Test full flow
async def test_music_flow():
    # Search
    results = await music_manager.search_platform("jiosaavn", "Kesariya")
    
    # Get download URL
    url = await music_manager.get_download_url("jiosaavn", results[0])
    
    # Verify URL
    assert url is not None
```

---

## 📝 Code Style / कोड स्टाइल

### Python Style Guide
- PEP 8 compliance
- Type hints जहाँ possible
- Docstrings for functions
- Clear variable names

### Example:
```python
async def search_platform(
    self, 
    platform: str, 
    query: str, 
    limit: int = 10
) -> Optional[List[Dict]]:
    """
    Search specific platform for songs
    
    Args:
        platform: Platform name (e.g., "jiosaavn")
        query: Search query
        limit: Maximum results
        
    Returns:
        List of track dictionaries or None
    """
    # Implementation
```

---

## 🔄 Update Process / अपडेट प्रोसेस

### Adding New Platform

1. **Create helper file**
```python
# helpers/newplatform.py
class NewPlatformAPI:
    async def search(self, query, limit):
        # Implementation
```

2. **Update config.py**
```python
ENABLE_NEWPLATFORM = os.getenv("ENABLE_NEWPLATFORM", "true").lower() == "true"
```

3. **Update music_platforms.py**
```python
from helpers.newplatform import newplatform_api

self.platforms["newplatform"] = newplatform_api
```

4. **Create handler**
```python
# handlers/platforms.py or free_platforms.py
@Client.on_message(command(["newplatform"]))
async def newplatform_search():
    # Implementation
```

5. **Update documentation**
- README.md
- PLATFORMS.md
- .env.example

---

## 📚 Dependencies / डिपेंडेंसीज

### Core Dependencies
```
pyrogram==2.0.106          # Telegram MTProto framework
TgCrypto==1.2.5            # Cryptography for Pyrogram
py-tgcalls==0.9.7          # Voice calls support
python-dotenv==1.0.0       # Environment variables
```

### Music & Download
```
youtube-search-python==1.6.6  # YouTube search
yt-dlp==2023.12.30           # YouTube downloader
```

### HTTP & Async
```
aiohttp==3.9.1              # Async HTTP client
aiofiles==23.2.1            # Async file operations
requests==2.31.0            # HTTP requests
```

### Database
```
motor==3.3.2                # Async MongoDB driver
pymongo==4.6.1              # MongoDB driver
```

### Utilities
```
pillow==10.1.0              # Image processing
```

---

## 🎯 Best Practices / बेस्ट प्रैक्टिसेज

1. **Always use async/await** for I/O operations
2. **Handle errors gracefully** at every level
3. **Close sessions properly** to avoid memory leaks
4. **Use environment variables** for configuration
5. **Log important events** for debugging
6. **Keep code modular** and reusable
7. **Document your code** with comments
8. **Test before deploying** to production
9. **Monitor bot performance** regularly
10. **Keep dependencies updated** for security

---

**📖 यह documentation आपको पूरे system को समझने में मदद करेगी!**

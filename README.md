# 🎵 Multi-Platform Telegram Music Bot

A comprehensive Telegram Music Bot that supports **5 major music platforms** - Spotify, Apple Music, SoundCloud, Deezer, and YouTube. Stream high-quality music in voice chats with interactive search and queue management.

## ✨ Features

### 🎯 Multi-Platform Support
- 🟢 **Spotify** - Access millions of tracks with rich metadata
- 🍎 **Apple Music** - iTunes catalog with preview support
- 🟠 **SoundCloud** - Independent artists and remixes
- 🔵 **Deezer** - International music catalog
- 🔴 **YouTube** - Largest music library with direct playback

### 🎛️ Core Features
- 🔍 **Cross-platform search** - Search all platforms simultaneously
- 🎵 **Interactive selection** - Choose from 5 search results per platform
- 📥 **Audio downloads** - Download songs as audio files
- ⏸️ **Playback controls** - Pause, resume, skip, stop
- 📋 **Queue management** - Add multiple songs to queue
- 👥 **Admin controls** - Restrict commands to admins
- 📊 **Statistics** - Track bot usage and analytics
- 📡 **Broadcast** - Send messages to all groups

## 🚀 Setup Guide

### Prerequisites
- Python 3.8 or higher
- MongoDB database
- FFmpeg installed
- Telegram Bot Token
- Telegram API credentials
- Platform API keys (optional but recommended)

### Step 1: Get API Credentials

#### Telegram
1. Get API ID & Hash from https://my.telegram.org
2. Create bot via @BotFather and get Bot Token

#### Spotify (Recommended)
1. Go to https://developer.spotify.com/dashboard
2. Create an app
3. Copy Client ID and Client Secret

#### SoundCloud (Optional)
1. Visit https://soundcloud.com/you/apps
2. Register a new app
3. Copy Client ID

**Note:** Apple Music and Deezer work without API keys (public APIs)

### Step 2: Installation

```bash
# Clone repository
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot

# Install FFmpeg
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows - Download from https://ffmpeg.org/download.html

# Install Python dependencies
pip install -r requirements.txt

# Create downloads folder
mkdir downloads
```

### Step 3: Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env file
nano .env
```

**Required Configuration:**
```env
# Telegram (Required)
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token

# Database (Required)
MONGO_DB_URI=mongodb://localhost:27017/musicbot

# Bot Settings (Required)
OWNER_ID=your_telegram_user_id
LOG_GROUP_ID=your_log_group_id

# Spotify (Optional but recommended)
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

# SoundCloud (Optional)
SOUNDCLOUD_CLIENT_ID=your_soundcloud_client_id
```

### Step 4: Run the Bot

```bash
python bot.py
```

## 📝 Commands Reference

### 🎵 Platform-Specific Commands

| Platform | Command | Shortcut | Example |
|----------|---------|----------|---------|
| YouTube | `/play <song>` | - | `/play Kesariya` |
| Spotify | `/spotify <song>` | `/sp` | `/spotify Tum Hi Ho` |
| Apple Music | `/apple <song>` | `/am` | `/apple Apna Bana Le` |
| SoundCloud | `/soundcloud <song>` | `/sc` | `/sc Remix 2024` |
| Deezer | `/deezer <song>` | `/dz` | `/deezer Chaleya` |

### 🔍 Universal Search
- `/search <song>` or `/s <song>` - Search across all platforms

### 🎛️ Playback Controls
- `/pause` - Pause current song
- `/resume` - Resume playback
- `/skip` - Skip to next song
- `/stop` - Stop playback and clear queue
- `/queue` - Show current queue

### 📥 Download
- `/song <name>` - Download song as audio file

### ℹ️ Information
- `/start` - Start the bot
- `/help` - Show help message
- `/platforms` - Show supported platforms

### 👑 Admin Commands (Owner Only)
- `/broadcast` - Broadcast message to all chats
- `/stats` - Show bot statistics

## 🎯 Usage Examples

### Search and Play from Spotify
```
/spotify Kesariya
```
Bot shows 5 Spotify results → Click to play

### Search All Platforms
```
/search Tum Hi Ho
```
Bot shows top 3 results from each platform

### Play YouTube URL
```
/play https://youtube.com/watch?v=xxxxx
```
Direct playback from URL

### Download Song
```
/song Apna Bana Le
```
Bot downloads and sends audio file

## 🔧 Advanced Configuration

Edit `config.py` for advanced settings:

```python
# Duration limits
DURATION_LIMIT = 900  # Max 15 minutes
SONG_DOWNLOAD_DURATION = 600  # Max 10 minutes

# Enable/disable platforms
ENABLE_SPOTIFY = True
ENABLE_APPLE_MUSIC = True
ENABLE_SOUNDCLOUD = True
ENABLE_DEEZER = True
ENABLE_YOUTUBE = True
```

## 📦 Project Structure

```
telegram-music-bot/
├── bot.py                    # Main bot file
├── config.py                 # Configuration
├── requirements.txt          # Dependencies
├── .env.example             # Environment template
├── .gitignore               # Git ignore rules
├── helpers/
│   ├── __init__.py
│   ├── database.py          # MongoDB operations
│   ├── decorators.py        # Custom decorators
│   ├── filters.py           # Custom filters
│   ├── ytdl.py              # YouTube downloader
│   ├── spotify.py           # Spotify integration
│   ├── apple_music.py       # Apple Music integration
│   ├── soundcloud.py        # SoundCloud integration
│   ├── deezer.py            # Deezer integration
│   ├── music_platforms.py   # Platform manager
│   └── call_manager.py      # Voice call manager
└── handlers/
    ├── __init__.py
    ├── music.py             # YouTube music commands
    ├── platforms.py         # Multi-platform commands
    ├── admin.py             # Admin commands
    └── misc.py              # Misc commands
```

## 🔍 How It Works

1. **User searches** for a song using platform-specific command
2. **Bot queries** the respective platform API
3. **Results displayed** with interactive buttons (5 options)
4. **User selects** desired song
5. **Bot finds** YouTube equivalent for download
6. **Downloads** audio using yt-dlp
7. **Plays** in voice chat using PyTgCalls

## 🛠️ Troubleshooting

### Platform Search Not Working

**Spotify:**
- Verify Client ID and Secret in `.env`
- Check if credentials are valid
- Token expires after 1 hour (auto-refreshes)

**SoundCloud:**
- Verify Client ID in `.env`
- SoundCloud API can be rate-limited

**Apple Music/Deezer:**
- No API key needed
- Should work out of the box

**YouTube:**
- Update yt-dlp: `pip install -U yt-dlp`
- Check internet connection

### Voice Chat Issues
- Ensure bot has admin rights
- Bot needs "Manage Voice Chats" permission
- Check pytgcalls installation

### Download Errors
- Install FFmpeg properly
- Check disk space in `downloads/` folder
- Verify file permissions

### MongoDB Connection
- Ensure MongoDB is running
- Check connection string in `.env`
- Test connection: `mongosh <your_uri>`

## 🎨 Customization

### Add More Platforms
1. Create helper file in `helpers/` (e.g., `tidal.py`)
2. Implement search and track methods
3. Add to `music_platforms.py`
4. Create handler in `handlers/platforms.py`

### Change Bot Behavior
- Edit `config.py` for limits and settings
- Modify `helpers/decorators.py` for permissions
- Update `handlers/` for command logic

## 🤝 Contributing

Contributions welcome! Areas to improve:
- Add more music platforms (Tidal, Pandora, etc.)
- Improve search algorithms
- Add playlist support
- Implement lyrics fetching
- Add audio effects

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Credits

Built with:
- [Pyrogram](https://github.com/pyrogram/pyrogram) - Telegram MTProto API
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls) - Voice chat library
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloader
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/)
- [SoundCloud API](https://developers.soundcloud.com/)
- [Deezer API](https://developers.deezer.com/)

## 💬 Support

- 🐛 Report bugs via GitHub Issues
- 💡 Suggest features via GitHub Discussions
- 📧 Contact: [Your Email]
- 💬 Telegram: [Your Support Group]

## 🌟 Features Roadmap

- [ ] Playlist import from platforms
- [ ] Lyrics display
- [ ] Audio equalizer
- [ ] Voice commands
- [ ] Multi-language support
- [ ] Web dashboard
- [ ] Premium features

---

Made with ❤️ for music lovers worldwide

**Star ⭐ this repo if you find it useful!**

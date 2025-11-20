# 🎵 Multi-Platform Telegram Music Bot

A comprehensive Telegram Music Bot supporting **10 music platforms** including **5 FREE Indian platforms** (JioSaavn, Gaana, Wynk) that work without any API keys! Stream high-quality music in voice chats with interactive search and queue management.

## ✨ Features

### 🎯 10 Music Platforms Support

#### 🆓 Free Platforms (No API Key Required!)
- 🎵 **JioSaavn** - Indian music, Bollywood, Regional songs
- 🎶 **Gaana** - Indian music, Bollywood hits
- 🎧 **Wynk Music** - Indian & International music
- 🎼 **Jamendo** - Creative Commons music
- 🎤 **Audiomack** - Hip-Hop, Rap, Afrobeats
- 🔴 **YouTube** - Largest music library
- 🍎 **Apple Music** - iTunes catalog (public API)
- 🔵 **Deezer** - International music (public API)

#### 🔑 Optional API Key Platforms
- 🟢 **Spotify** - Millions of tracks (optional API key)
- 🟠 **SoundCloud** - Independent artists (optional API key)

### 🎛️ Core Features
- 🔍 **Cross-platform search** - Search all platforms simultaneously
- 🎵 **Interactive selection** - Choose from 5 search results per platform
- 📥 **Audio downloads** - Download songs as audio files
- ⏸️ **Playback controls** - Pause, resume, skip, stop
- 📋 **Queue management** - Add multiple songs to queue
- 👥 **Admin controls** - Restrict commands to admins
- 📊 **Statistics** - Track bot usage and analytics
- 📡 **Broadcast** - Send messages to all groups
- ⚙️ **Flexible configuration** - Enable/disable any platform

## 🚀 Quick Start (No API Keys Needed!)

### Minimal Setup
```bash
# Clone repository
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot

# Install dependencies
pip install -r requirements.txt

# Copy and edit .env
cp .env.example .env
nano .env
```

**Minimal .env Configuration:**
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

# Enable Free Platforms (No API keys needed!)
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true
ENABLE_YOUTUBE=true
ENABLE_APPLE_MUSIC=true
ENABLE_DEEZER=true
ENABLE_JAMENDO=true
ENABLE_AUDIOMACK=true
```

**Start Bot:**
```bash
python bot.py
```

**Use Commands:**
```
/jiosaavn Kesariya
/gaana Tum Hi Ho
/wynk Apna Bana Le
/play Shape of You
```

## 📋 Commands

### Music Commands
```
/play <song> - Play from YouTube
/jiosaavn <song> - Play from JioSaavn (Free!)
/gaana <song> - Play from Gaana (Free!)
/wynk <song> - Play from Wynk Music (Free!)
/spotify <song> - Play from Spotify
/apple <song> - Play from Apple Music
/soundcloud <song> - Play from SoundCloud
/deezer <song> - Play from Deezer
/jamendo <song> - Play from Jamendo (Free CC music)
/audiomack <song> - Play from Audiomack (Free!)
/search <song> - Search all platforms
```

### Short Commands
```
/jio, /js - JioSaavn
/gn - Gaana
/wk - Wynk
/sp - Spotify
/am - Apple Music / Audiomack
/sc - SoundCloud
/dz - Deezer
/jm - Jamendo
/yt - YouTube
```

### Playback Controls
```
/pause - Pause playback
/resume - Resume playback
/skip - Skip current song
/stop - Stop and clear queue
/queue - Show current queue
```

### Admin Commands
```
/stats - Bot statistics
/broadcast - Send message to all groups
```

## 🔧 Full Setup Guide

### Prerequisites
- Python 3.8+
- MongoDB database
- FFmpeg installed
- Telegram Bot Token
- Telegram API credentials

### Step 1: Get Telegram Credentials

#### Telegram API
1. Visit https://my.telegram.org
2. Login with your phone number
3. Go to "API Development Tools"
4. Create an app and get API ID & Hash

#### Bot Token
1. Open @BotFather on Telegram
2. Send `/newbot`
3. Follow instructions
4. Copy the Bot Token

### Step 2: Install FFmpeg

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Step 3: Install Dependencies

```bash
# Clone repository
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot

# Install Python packages
pip install -r requirements.txt

# Create downloads folder
mkdir downloads
```

### Step 4: Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit configuration
nano .env
```

**Complete .env Configuration:**
```env
# Telegram Configuration (Required)
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token

# Database (Required)
MONGO_DB_URI=mongodb://localhost:27017/musicbot

# Bot Settings (Required)
LOG_GROUP_ID=your_log_group_id
OWNER_ID=your_user_id

# Optional API Keys (Better results)
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SOUNDCLOUD_CLIENT_ID=your_soundcloud_client_id
JAMENDO_CLIENT_ID=your_jamendo_client_id
AUDIOMACK_API_KEY=your_audiomack_api_key

# Platform Enable/Disable
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true
ENABLE_SPOTIFY=true
ENABLE_APPLE_MUSIC=true
ENABLE_SOUNDCLOUD=true
ENABLE_DEEZER=true
ENABLE_YOUTUBE=true
ENABLE_JAMENDO=true
ENABLE_AUDIOMACK=true
```

### Step 5: Get Optional API Keys

#### Spotify (Recommended)
1. Go to https://developer.spotify.com/dashboard
2. Create an app
3. Copy Client ID and Client Secret

#### SoundCloud (Optional)
1. Visit https://soundcloud.com/you/apps
2. Register a new app
3. Copy Client ID

#### Jamendo (Optional)
1. Visit https://developer.jamendo.com
2. Register for API access
3. Copy Client ID

#### Audiomack (Optional)
1. Visit https://www.audiomack.com/data-api
2. Request API access
3. Copy API Key

### Step 6: Run Bot

```bash
# Start bot
python bot.py

# Or use screen/tmux for background
screen -S musicbot
python bot.py
# Press Ctrl+A then D to detach
```

## 📊 Platform Comparison

| Platform | Free | API Key | Indian Music | International | Commands |
|----------|------|---------|--------------|---------------|----------|
| JioSaavn | ✅ | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐ | `/jiosaavn`, `/jio`, `/js` |
| Gaana | ✅ | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐ | `/gaana`, `/gn` |
| Wynk | ✅ | ❌ | ⭐⭐⭐⭐ | ⭐⭐⭐ | `/wynk`, `/wk` |
| YouTube | ✅ | ❌ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | `/play`, `/yt` |
| Jamendo | ✅ | Optional | ⭐⭐ | ⭐⭐⭐⭐ | `/jamendo`, `/jm` |
| Audiomack | ✅ | Optional | ⭐⭐ | ⭐⭐⭐⭐ | `/audiomack`, `/am` |
| Apple Music | ✅ | ❌ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | `/apple`, `/am` |
| Deezer | ✅ | ❌ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | `/deezer`, `/dz` |
| Spotify | ✅ | Optional | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | `/spotify`, `/sp` |
| SoundCloud | ✅ | Optional | ⭐⭐ | ⭐⭐⭐⭐ | `/soundcloud`, `/sc` |

## 💡 Usage Tips

### For Indian Music
```
/jiosaavn Kesariya
/gaana Tum Hi Ho
/wynk Apna Bana Le
```

### For International Music
```
/spotify Starboy
/apple Blinding Lights
/deezer Levitating
```

### For Everything
```
/play Shape of You
/search Kesariya
```

### For Creative Commons Music
```
/jamendo Chill Music
```

### For Hip-Hop/Rap
```
/audiomack Hip Hop Beats
```

## 🔧 Troubleshooting

### Platform Not Working?
1. Check if platform is enabled in `.env`
2. Verify API key (if required)
3. Check internet connection
4. Try different platform

### No Results Found?
1. Try different search terms
2. Use `/search` to search all platforms
3. Try platform-specific search

### Download Failed?
1. Check if song is available
2. Try different platform
3. YouTube is used as fallback

## 📝 Notes

- **8 platforms work without ANY API keys!**
- **Only Spotify & SoundCloud need optional API keys**
- **All Indian platforms (JioSaavn, Gaana, Wynk) are completely free**
- **Enable/disable any platform anytime in `.env`**
- **Multiple platforms work simultaneously**
- **Bot automatically falls back to YouTube if direct download fails**

## 📚 Documentation

For detailed platform documentation, see [PLATFORMS.md](PLATFORMS.md)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new music platforms
- Improve existing features
- Fix bugs
- Enhance documentation

## 📄 License

This project is licensed under the MIT License.

## 🙏 Credits

- Pyrogram - Telegram MTProto API framework
- yt-dlp - YouTube downloader
- All music platform APIs

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Contact: [Your Contact Info]

---

**Made with ❤️ for music lovers**

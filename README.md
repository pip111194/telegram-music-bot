# 🎵 Multi-Platform Telegram Music Bot

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0-green.svg)](https://docs.pyrogram.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/Platforms-10-red.svg)](PLATFORMS.md)

**A comprehensive Telegram Music Bot supporting 10 music platforms including 5 FREE Indian platforms (JioSaavn, Gaana, Wynk) that work without any API keys!**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Commands](#-commands) • [Support](#-support)

</div>

---

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

#### 🔑 Optional API Key Platforms (Better Results)
- 🟢 **Spotify** - Millions of tracks
- 🟠 **SoundCloud** - Independent artists

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
- 🌐 **Multi-language** - Hindi & English support

---

## 🚀 Quick Start

### Option 1: Minimal Setup (No API Keys!)

```bash
# 1. Clone repository
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install FFmpeg
sudo apt install ffmpeg  # Linux
brew install ffmpeg      # macOS

# 4. Configure
cp .env.example .env
nano .env  # Add your Telegram credentials

# 5. Start bot
python bot.py
```

**Minimum .env Configuration:**
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=mongodb://localhost:27017/musicbot
OWNER_ID=your_telegram_user_id
LOG_GROUP_ID=your_log_group_id

# Enable free platforms
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true
ENABLE_YOUTUBE=true
```

**Start Using:**
```
/jiosaavn Kesariya
/gaana Tum Hi Ho
/play Shape of You
```

### Option 2: Full Setup (With Optional API Keys)

See [SETUP.md](SETUP.md) for detailed step-by-step installation guide.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [📖 SETUP.md](SETUP.md) | Complete step-by-step setup guide (Hindi & English) |
| [🎵 PLATFORMS.md](PLATFORMS.md) | Detailed platform documentation and comparison |
| [🏗️ ARCHITECTURE.md](ARCHITECTURE.md) | System architecture and code structure |
| [🤝 CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines and how to add platforms |
| [❓ FAQ.md](FAQ.md) | Frequently asked questions (50+ Q&A) |

---

## 💬 Commands

### Music Commands
| Command | Description | Example |
|---------|-------------|---------|
| `/play <song>` | Play from YouTube | `/play Shape of You` |
| `/jiosaavn <song>` | Play from JioSaavn | `/jiosaavn Kesariya` |
| `/gaana <song>` | Play from Gaana | `/gaana Tum Hi Ho` |
| `/wynk <song>` | Play from Wynk | `/wynk Apna Bana Le` |
| `/spotify <song>` | Play from Spotify | `/spotify Starboy` |
| `/apple <song>` | Play from Apple Music | `/apple Blinding Lights` |
| `/soundcloud <song>` | Play from SoundCloud | `/soundcloud Mix` |
| `/deezer <song>` | Play from Deezer | `/deezer Levitating` |
| `/jamendo <song>` | Play from Jamendo | `/jamendo Chill` |
| `/audiomack <song>` | Play from Audiomack | `/audiomack Hip Hop` |
| `/search <song>` | Search all platforms | `/search Kesariya` |

### Short Commands
```
/jio, /js    → JioSaavn
/gn          → Gaana
/wk          → Wynk
/sp          → Spotify
/yt          → YouTube
/dz          → Deezer
/jm          → Jamendo
/am          → Audiomack (or Apple Music)
/sc          → SoundCloud
```

### Playback Controls
| Command | Description |
|---------|-------------|
| `/pause` | Pause current playback |
| `/resume` | Resume playback |
| `/skip` | Skip to next song |
| `/stop` | Stop playback and clear queue |
| `/queue` | Show current queue |

### Admin Commands
| Command | Description |
|---------|-------------|
| `/stats` | Show bot statistics |
| `/broadcast <msg>` | Send message to all groups |

---

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

---

## 💡 Usage Examples

### For Indian Music
```bash
/jiosaavn Kesariya          # Bollywood
/gaana Tum Hi Ho            # Romantic
/wynk Apna Bana Le          # Latest hits
```

### For International Music
```bash
/spotify Starboy            # Pop
/apple Blinding Lights      # International hits
/deezer Levitating          # Dance
```

### For Everything
```bash
/play Shape of You          # YouTube
/search Kesariya            # All platforms
```

### For Creative Commons
```bash
/jamendo Chill Music        # Free CC music
```

### For Hip-Hop/Rap
```bash
/audiomack Hip Hop Beats    # Latest rap
```

---

## 🔧 Configuration

### Enable/Disable Platforms

Edit `.env` file:

```env
# Free Indian Platforms (No API key needed!)
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true

# Free International Platforms
ENABLE_YOUTUBE=true
ENABLE_APPLE_MUSIC=true
ENABLE_DEEZER=true
ENABLE_JAMENDO=true
ENABLE_AUDIOMACK=true

# Optional API Key Platforms
ENABLE_SPOTIFY=false
ENABLE_SOUNDCLOUD=false
```

### Add Optional API Keys (Better Results)

```env
# Spotify (https://developer.spotify.com/dashboard)
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret

# SoundCloud (https://soundcloud.com/you/apps)
SOUNDCLOUD_CLIENT_ID=your_client_id

# Jamendo (https://developer.jamendo.com)
JAMENDO_CLIENT_ID=your_client_id

# Audiomack (https://www.audiomack.com/data-api)
AUDIOMACK_API_KEY=your_api_key
```

---

## 📋 Requirements

- **Python 3.8+**
- **MongoDB** (local or Atlas)
- **FFmpeg**
- **Telegram Bot Token**
- **Telegram API credentials**

### System Requirements
- **OS:** Linux, macOS, or Windows
- **RAM:** 1GB minimum, 2GB recommended
- **Storage:** 5GB for downloads
- **Internet:** Stable connection

---

## 🐛 Troubleshooting

### Common Issues

**Bot not starting?**
```bash
pip install -r requirements.txt --upgrade
python --version  # Check 3.8+
```

**No results found?**
- Check internet connection
- Verify platform is enabled in `.env`
- Try different platform

**Download failed?**
```bash
ffmpeg -version  # Check FFmpeg
mkdir downloads  # Create folder
```

**Commands not working?**
- Make bot admin in group
- Start voice chat
- Send `/start` command

See [FAQ.md](FAQ.md) for 50+ common questions and solutions.

---

## 🏗️ Project Structure

```
telegram-music-bot/
├── bot.py                 # Main entry point
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
│
├── handlers/             # Command handlers
│   ├── music.py         # Music commands
│   ├── platforms.py     # Platform handlers
│   ├── free_platforms.py # Free platform handlers
│   ├── admin.py         # Admin commands
│   └── misc.py          # Misc commands
│
├── helpers/              # Helper modules
│   ├── music_platforms.py # Platform manager
│   ├── jiosaavn.py      # JioSaavn API
│   ├── gaana.py         # Gaana API
│   ├── wynk.py          # Wynk API
│   ├── spotify.py       # Spotify API
│   ├── ytdl.py          # YouTube downloader
│   └── ...              # Other helpers
│
└── downloads/            # Downloaded files
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system architecture.

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to contribute
- Adding new platforms
- Code guidelines
- Pull request process

---

## 📝 Notes

- **8 platforms work without ANY API keys!**
- **Only Spotify & SoundCloud need optional API keys**
- **All Indian platforms (JioSaavn, Gaana, Wynk) are completely free**
- **Enable/disable any platform anytime in `.env`**
- **Multiple platforms work simultaneously**
- **Bot automatically falls back to YouTube if direct download fails**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- **Pyrogram** - Telegram MTProto API framework
- **yt-dlp** - YouTube downloader
- **All music platform APIs**
- **Contributors** - Thank you for your contributions!

---

## 📞 Support

### Documentation
- [Setup Guide](SETUP.md) - Complete installation guide
- [Platform Guide](PLATFORMS.md) - Platform details
- [FAQ](FAQ.md) - Common questions
- [Architecture](ARCHITECTURE.md) - System design
- [Contributing](CONTRIBUTING.md) - How to contribute

### Community
- **GitHub Issues** - Bug reports and feature requests
- **Discussions** - Questions and ideas
- **Telegram** - [Support Group] (if available)

---

## 🌟 Star History

If you like this project, please give it a ⭐ on GitHub!

---

<div align="center">

**Made with ❤️ for music lovers**

[⬆ Back to Top](#-multi-platform-telegram-music-bot)

</div>

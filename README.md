# 🎵 Telegram Music Bot

A feature-rich Telegram Music Bot for streaming music in voice chats with interactive search, queue management and admin controls.

## ✨ Features

- 🎶 Play music from YouTube (URL or search)
- 🔍 **Interactive search results** - Choose from 5 search results
- 📥 Download songs as audio files
- ⏸️ Pause/Resume playback
- ⏭️ Skip songs
- 📋 Queue management
- 👥 Admin-only controls
- 📊 Statistics tracking
- 📡 Broadcast messages
- 🎯 Async operations for better performance

## 🚀 Setup

### Prerequisites
- Python 3.8+
- MongoDB database
- Telegram Bot Token (from @BotFather)
- Telegram API ID & Hash (from https://my.telegram.org)
- FFmpeg installed on system

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot
```

2. **Install FFmpeg:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create `.env` file:**
```bash
cp .env.example .env
```

5. **Edit `.env` with your credentials:**
```env
API_ID=your_api_id_from_my.telegram.org
API_HASH=your_api_hash_from_my.telegram.org
BOT_TOKEN=your_bot_token_from_botfather
MONGO_DB_URI=mongodb://localhost:27017/musicbot
LOG_GROUP_ID=your_log_group_id
OWNER_ID=your_telegram_user_id
```

6. **Create downloads folder:**
```bash
mkdir downloads
```

7. **Run the bot:**
```bash
python bot.py
```

## 📝 Commands

### User Commands
- `/start` - Start the bot
- `/help` - Show help message
- `/play <song name or URL>` - Play a song (shows 5 search results to choose from)
- `/song <song name>` - Download song as audio file
- `/pause` - Pause current song
- `/resume` - Resume playback
- `/skip` - Skip to next song
- `/stop` - Stop playback and clear queue
- `/queue` - Show current queue

### Admin Commands (Owner Only)
- `/broadcast` - Broadcast message to all chats
- `/stats` - Show bot statistics

## 🎯 Usage Examples

**Play a song by search:**
```
/play Kesariya
```
Bot will show 5 search results with buttons to choose from.

**Play from YouTube URL:**
```
/play https://youtube.com/watch?v=xxxxx
```

**Download a song:**
```
/song Tum Hi Ho
```

## 🔧 Configuration

Edit `config.py` to customize:
```python
DURATION_LIMIT = 900  # Max song duration (15 minutes)
SONG_DOWNLOAD_DURATION = 600  # Max download duration (10 minutes)
```

## 📦 Project Structure

```
telegram-music-bot/
├── bot.py              # Main bot file
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
├── .gitignore         # Git ignore rules
├── helpers/
│   ├── __init__.py
│   ├── database.py     # MongoDB operations
│   ├── decorators.py   # Custom decorators
│   ├── filters.py      # Custom filters
│   ├── ytdl.py         # YouTube downloader with search
│   └── call_manager.py # Voice call manager
└── handlers/
    ├── __init__.py
    ├── music.py        # Music commands with inline search
    ├── admin.py        # Admin commands
    └── misc.py         # Misc commands
```

## 🔍 How Search Works

1. User sends `/play Kesariya`
2. Bot searches YouTube and returns 5 results
3. User clicks on desired song button
4. Bot downloads and plays the selected song
5. Shows now playing info with title, duration, uploader

## 🛠️ Troubleshooting

**Search not working:**
- Check internet connection
- Verify YouTube is accessible
- Update yt-dlp: `pip install -U yt-dlp`

**Voice chat issues:**
- Ensure bot has admin rights in group
- Bot needs permission to manage voice chats
- Check if pytgcalls is properly installed

**Download errors:**
- Install FFmpeg properly
- Check disk space in downloads folder
- Verify file permissions

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

For support and updates:
- Open an issue on GitHub
- Join our [Support Group](https://t.me/your_support_group)

## 🙏 Credits

Built with:
- [Pyrogram](https://github.com/pyrogram/pyrogram) - Telegram MTProto API framework
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls) - Voice chat library
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloader
- [youtube-search-python](https://github.com/alexmercerind/youtube-search-python) - YouTube search

---

Made with ❤️ for music lovers

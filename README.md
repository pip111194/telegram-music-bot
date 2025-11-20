# 🎵 Telegram Music Bot

A feature-rich Telegram Music Bot for streaming music in voice chats with queue management and admin controls.

## ✨ Features

- 🎶 Play music from YouTube
- 🔍 Search songs by name
- ⏸️ Pause/Resume playback
- ⏭️ Skip songs
- 📋 Queue management
- 👥 Admin-only controls
- 📊 Statistics tracking
- 📡 Broadcast messages

## 🚀 Setup

### Prerequisites
- Python 3.8+
- MongoDB database
- Telegram Bot Token
- Telegram API ID & Hash

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Edit `.env` with your credentials:
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
LOG_GROUP_ID=your_log_group_id
OWNER_ID=your_user_id
```

5. Run the bot:
```bash
python bot.py
```

## 📝 Commands

### User Commands
- `/start` - Start the bot
- `/help` - Show help message
- `/play <song>` - Play a song
- `/pause` - Pause current song
- `/resume` - Resume playback
- `/skip` - Skip to next song
- `/stop` - Stop playback
- `/queue` - Show current queue

### Admin Commands (Owner Only)
- `/broadcast` - Broadcast message to all chats
- `/stats` - Show bot statistics

## 🔧 Configuration

Edit `config.py` to customize:
- Duration limits
- Download settings
- Support group/channel links

## 📦 Project Structure

```
telegram-music-bot/
├── bot.py              # Main bot file
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── helpers/
│   ├── database.py     # Database operations
│   ├── decorators.py   # Custom decorators
│   ├── filters.py      # Custom filters
│   ├── ytdl.py         # YouTube downloader
│   └── call_manager.py # Voice call manager
└── handlers/
    ├── music.py        # Music commands
    ├── admin.py        # Admin commands
    └── misc.py         # Misc commands
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

For support, join our [Support Group](https://t.me/your_support_group)

---

Made with ❤️ by [Your Name]

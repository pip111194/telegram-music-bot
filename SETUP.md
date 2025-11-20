# 🚀 Complete Setup Guide / पूर्ण सेटअप गाइड

## 📋 Table of Contents / विषय सूची
1. [Requirements / आवश्यकताएं](#requirements)
2. [Installation / इंस्टॉलेशन](#installation)
3. [Configuration / कॉन्फ़िगरेशन](#configuration)
4. [Running Bot / बॉट चलाना](#running)
5. [Troubleshooting / समस्या समाधान](#troubleshooting)

---

## 1️⃣ Requirements / आवश्यकताएं {#requirements}

### System Requirements / सिस्टम आवश्यकताएं
- **Python 3.8+** installed
- **MongoDB** database (local or cloud)
- **FFmpeg** installed
- **Internet connection** / इंटरनेट कनेक्शन
- **Telegram account** / टेलीग्राम अकाउंट

### What You Need / आपको क्या चाहिए
✅ Telegram API ID & Hash  
✅ Telegram Bot Token  
✅ MongoDB connection string  
✅ Your Telegram User ID  

---

## 2️⃣ Installation / इंस्टॉलेशन {#installation}

### Step 1: Install Python
**Windows:**
```bash
# Download from https://www.python.org/downloads/
# Install करते समय "Add Python to PATH" check करें
```

**Linux/Ubuntu:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**macOS:**
```bash
brew install python3
```

### Step 2: Install FFmpeg
**Windows:**
```bash
# Download from https://ffmpeg.org/download.html
# Extract और PATH में add करें
```

**Linux/Ubuntu:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

### Step 3: Install MongoDB
**Option 1: Local MongoDB**
```bash
# Ubuntu/Debian
sudo apt install mongodb

# macOS
brew install mongodb-community

# Windows
# Download from https://www.mongodb.com/try/download/community
```

**Option 2: MongoDB Atlas (Cloud - Recommended)**
1. Visit https://www.mongodb.com/cloud/atlas
2. Create free account
3. Create cluster
4. Get connection string

### Step 4: Clone Repository
```bash
# Clone करें
git clone https://github.com/pip111194/telegram-music-bot.git

# Folder में जाएं
cd telegram-music-bot

# Dependencies install करें
pip install -r requirements.txt
```

---

## 3️⃣ Configuration / कॉन्फ़िगरेशन {#configuration}

### Step 1: Get Telegram API Credentials

#### A. API ID & Hash लें
1. Visit: https://my.telegram.org
2. Login with your phone number
3. Click "API Development Tools"
4. Create new application:
   - **App title:** Music Bot
   - **Short name:** musicbot
   - **Platform:** Other
5. Copy **API ID** और **API Hash**

#### B. Bot Token लें
1. Telegram पर @BotFather खोलें
2. Send: `/newbot`
3. Bot name दें: `My Music Bot`
4. Username दें: `my_music_bot` (unique होना चाहिए)
5. Copy **Bot Token**

#### C. Your User ID लें
1. Telegram पर @userinfobot खोलें
2. `/start` send करें
3. Copy your **User ID**

#### D. Log Group बनाएं
1. Telegram पर new group बनाएं
2. Bot को group में add करें
3. Bot को admin बनाएं
4. Group में कोई message send करें
5. Visit: `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`
6. Copy **chat id** (negative number)

### Step 2: Configure .env File

```bash
# .env.example को copy करें
cp .env.example .env

# Edit करें
nano .env
# या
notepad .env
```

**Minimum Configuration (बिना API keys के):**
```env
# ============================================
# REQUIRED SETTINGS (जरूरी सेटिंग्स)
# ============================================

# Telegram Configuration
API_ID=12345678
API_HASH=abcdef1234567890abcdef1234567890
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Database (MongoDB Atlas या Local)
MONGO_DB_URI=mongodb://localhost:27017/musicbot
# या Atlas: mongodb+srv://username:password@cluster.mongodb.net/musicbot

# Bot Settings
LOG_GROUP_ID=-1001234567890
OWNER_ID=123456789

# ============================================
# FREE PLATFORMS (API key नहीं चाहिए!)
# ============================================
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true
ENABLE_YOUTUBE=true
ENABLE_APPLE_MUSIC=true
ENABLE_DEEZER=true
ENABLE_JAMENDO=true
ENABLE_AUDIOMACK=true

# ============================================
# OPTIONAL PLATFORMS (बेहतर results के लिए)
# ============================================
ENABLE_SPOTIFY=false
ENABLE_SOUNDCLOUD=false

# Spotify API (Optional)
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=

# SoundCloud API (Optional)
SOUNDCLOUD_CLIENT_ID=
```

### Step 3: Optional API Keys (बेहतर results के लिए)

#### Spotify API (Recommended)
1. Visit: https://developer.spotify.com/dashboard
2. Login with Spotify account
3. Click "Create an App"
4. Fill details:
   - **App name:** Music Bot
   - **App description:** Telegram Music Bot
5. Copy **Client ID** और **Client Secret**
6. Add to .env:
```env
ENABLE_SPOTIFY=true
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

#### SoundCloud API (Optional)
1. Visit: https://soundcloud.com/you/apps
2. Register new app
3. Copy **Client ID**
4. Add to .env:
```env
ENABLE_SOUNDCLOUD=true
SOUNDCLOUD_CLIENT_ID=your_client_id_here
```

---

## 4️⃣ Running Bot / बॉट चलाना {#running}

### Method 1: Direct Run (Testing के लिए)
```bash
# Bot start करें
python bot.py

# या Python 3
python3 bot.py
```

### Method 2: Screen (Background में चलाने के लिए)
```bash
# Screen install करें (if not installed)
sudo apt install screen

# Screen session start करें
screen -S musicbot

# Bot start करें
python bot.py

# Detach करें (Ctrl+A फिर D)
# Reattach करने के लिए: screen -r musicbot
```

### Method 3: Systemd Service (Production के लिए)
```bash
# Service file बनाएं
sudo nano /etc/systemd/system/musicbot.service
```

**Service file content:**
```ini
[Unit]
Description=Telegram Music Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/telegram-music-bot
ExecStart=/usr/bin/python3 /path/to/telegram-music-bot/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Enable और start करें:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable musicbot
sudo systemctl start musicbot

# Status check करें
sudo systemctl status musicbot

# Logs देखें
sudo journalctl -u musicbot -f
```

---

## 5️⃣ Testing / टेस्टिंग

### Step 1: Bot को Group में Add करें
1. Telegram पर अपना group खोलें
2. Bot को add करें
3. Bot को **admin** बनाएं (जरूरी!)

### Step 2: Commands Test करें
```
/start - Bot शुरू करें
/help - Commands देखें
/jiosaavn Kesariya - JioSaavn से गाना play करें
/gaana Tum Hi Ho - Gaana से गाना play करें
/play Shape of You - YouTube से गाना play करें
/search Kesariya - सभी platforms पर search करें
```

### Step 3: Voice Chat में Test करें
1. Group में voice chat start करें
2. कोई गाना play करें
3. Playback controls test करें:
   - `/pause` - Pause करें
   - `/resume` - Resume करें
   - `/skip` - Next song
   - `/stop` - Stop करें

---

## 6️⃣ Troubleshooting / समस्या समाधान {#troubleshooting}

### Problem 1: Bot Start नहीं हो रहा
**Solution:**
```bash
# Dependencies फिर से install करें
pip install -r requirements.txt --upgrade

# Python version check करें
python --version  # 3.8+ होना चाहिए

# .env file check करें
cat .env  # सभी values सही हैं?
```

### Problem 2: MongoDB Connection Error
**Solution:**
```bash
# Local MongoDB running है?
sudo systemctl status mongodb

# या MongoDB Atlas connection string सही है?
# Format: mongodb+srv://username:password@cluster.mongodb.net/dbname
```

### Problem 3: FFmpeg Not Found
**Solution:**
```bash
# FFmpeg install है?
ffmpeg -version

# नहीं है तो install करें
sudo apt install ffmpeg  # Linux
brew install ffmpeg      # macOS
```

### Problem 4: Bot Commands काम नहीं कर रहे
**Solution:**
1. Bot को group में **admin** बनाएं
2. Bot को **all permissions** दें
3. Group में `/start` send करें
4. Voice chat start करें

### Problem 5: No Results Found
**Solution:**
1. Internet connection check करें
2. Platform enabled है? `.env` में check करें
3. Different platform try करें:
   ```
   /jiosaavn Kesariya
   /gaana Kesariya
   /play Kesariya
   ```

### Problem 6: Download Failed
**Solution:**
1. FFmpeg properly install है?
2. `downloads` folder exist करता है?
   ```bash
   mkdir downloads
   chmod 777 downloads
   ```
3. Disk space available है?

---

## 7️⃣ Common Commands / सामान्य कमांड्स

### Music Commands
| Command | Description | Example |
|---------|-------------|---------|
| `/jiosaavn <song>` | JioSaavn से play करें | `/jiosaavn Kesariya` |
| `/gaana <song>` | Gaana से play करें | `/gaana Tum Hi Ho` |
| `/wynk <song>` | Wynk से play करें | `/wynk Apna Bana Le` |
| `/play <song>` | YouTube से play करें | `/play Shape of You` |
| `/search <song>` | सभी platforms पर search | `/search Kesariya` |

### Playback Controls
| Command | Description |
|---------|-------------|
| `/pause` | Playback pause करें |
| `/resume` | Playback resume करें |
| `/skip` | Current song skip करें |
| `/stop` | Playback stop करें |
| `/queue` | Queue देखें |

### Admin Commands
| Command | Description |
|---------|-------------|
| `/stats` | Bot statistics |
| `/broadcast <msg>` | सभी groups में message |

---

## 8️⃣ Platform Enable/Disable

### सभी Free Platforms Enable करें
```env
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true
ENABLE_YOUTUBE=true
ENABLE_APPLE_MUSIC=true
ENABLE_DEEZER=true
ENABLE_JAMENDO=true
ENABLE_AUDIOMACK=true
```

### Specific Platforms Disable करें
```env
ENABLE_JIOSAAVN=true   # ✅ Enabled
ENABLE_GAANA=false     # ❌ Disabled
ENABLE_WYNK=true       # ✅ Enabled
```

---

## 9️⃣ Support / सहायता

### Documentation
- **README.md** - Overview और features
- **PLATFORMS.md** - Platform details
- **SETUP.md** - यह guide

### Common Issues
1. **Bot offline** - Server/internet check करें
2. **Commands not working** - Bot admin है?
3. **No audio** - Voice chat active है?
4. **Platform error** - Platform enabled है?

### Contact
- GitHub Issues: Report bugs
- Telegram: @your_support_group

---

## ✅ Quick Checklist / त्वरित चेकलिस्ट

- [ ] Python 3.8+ installed
- [ ] FFmpeg installed
- [ ] MongoDB running
- [ ] Repository cloned
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured
- [ ] Telegram API credentials added
- [ ] Bot token added
- [ ] MongoDB URI added
- [ ] Bot started (`python bot.py`)
- [ ] Bot added to group
- [ ] Bot made admin
- [ ] Commands tested
- [ ] Voice chat tested

---

**🎉 Setup Complete! अब आप music enjoy कर सकते हैं!**

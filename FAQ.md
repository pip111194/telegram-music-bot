# ❓ Frequently Asked Questions / अक्सर पूछे जाने वाले प्रश्न

## 📋 Table of Contents

1. [General Questions](#general)
2. [Setup & Installation](#setup)
3. [Configuration](#configuration)
4. [Platform Questions](#platforms)
5. [Commands & Usage](#commands)
6. [Troubleshooting](#troubleshooting)
7. [Performance](#performance)
8. [Advanced](#advanced)

---

## 🌟 General Questions {#general}

### Q1: यह bot क्या करता है?
**A:** यह एक Telegram Music Bot है जो 10 different music platforms से songs play कर सकता है। आप voice chat में high-quality music stream कर सकते हैं।

### Q2: कौन से platforms supported हैं?
**A:** 
**Free (No API key):**
- JioSaavn, Gaana, Wynk (Indian music)
- YouTube, Apple Music, Deezer
- Jamendo, Audiomack

**Optional API key:**
- Spotify, SoundCloud

### Q3: क्या यह free है?
**A:** हाँ! Bot completely free और open-source है। 8 platforms बिना किसी API key के काम करते हैं।

### Q4: API keys क्यों चाहिए?
**A:** API keys optional हैं। वे better search results और more features provide करते हैं, लेकिन जरूरी नहीं हैं।

---

## 🚀 Setup & Installation {#setup}

### Q5: System requirements क्या हैं?
**A:**
- Python 3.8 या higher
- MongoDB database
- FFmpeg installed
- 1GB RAM minimum
- Stable internet connection

### Q6: MongoDB कहाँ से मिलेगा?
**A:** दो options हैं:
1. **Local:** `sudo apt install mongodb`
2. **Cloud (Recommended):** MongoDB Atlas - https://www.mongodb.com/cloud/atlas (Free tier available)

### Q7: FFmpeg क्यों जरूरी है?
**A:** FFmpeg audio processing के लिए जरूरी है। यह audio files को download और convert करता है।

### Q8: Windows पर कैसे install करें?
**A:**
```bash
# 1. Python install करें (python.org से)
# 2. FFmpeg download करें (ffmpeg.org से)
# 3. Repository clone करें
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot

# 4. Dependencies install करें
pip install -r requirements.txt

# 5. .env configure करें
copy .env.example .env
notepad .env

# 6. Bot start करें
python bot.py
```

### Q9: Linux पर कैसे install करें?
**A:**
```bash
# Dependencies install करें
sudo apt update
sudo apt install python3 python3-pip ffmpeg mongodb

# Repository clone करें
git clone https://github.com/pip111194/telegram-music-bot.git
cd telegram-music-bot

# Python packages install करें
pip3 install -r requirements.txt

# Configure करें
cp .env.example .env
nano .env

# Start करें
python3 bot.py
```

---

## ⚙️ Configuration {#configuration}

### Q10: .env file कैसे configure करें?
**A:** Minimum configuration:
```env
API_ID=12345678
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=mongodb://localhost:27017/musicbot
LOG_GROUP_ID=-1001234567890
OWNER_ID=123456789
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_YOUTUBE=true
```

### Q11: Telegram API credentials कहाँ से मिलेंगे?
**A:**
1. Visit: https://my.telegram.org
2. Login with phone number
3. Go to "API Development Tools"
4. Create app और copy API ID & Hash

### Q12: Bot Token कैसे प्राप्त करें?
**A:**
1. Telegram पर @BotFather खोलें
2. `/newbot` send करें
3. Bot name और username दें
4. Token copy करें

### Q13: User ID कैसे पता करें?
**A:**
1. @userinfobot खोलें
2. `/start` send करें
3. आपकी User ID दिखेगी

### Q14: Log Group ID कैसे मिलेगा?
**A:**
1. New group बनाएं
2. Bot को add करें और admin बनाएं
3. Group में message send करें
4. Visit: `https://api.telegram.org/bot<TOKEN>/getUpdates`
5. Chat ID copy करें (negative number)

---

## 🎵 Platform Questions {#platforms}

### Q15: कौन से platforms API key के बिना काम करते हैं?
**A:** 8 platforms:
- JioSaavn ✅
- Gaana ✅
- Wynk ✅
- YouTube ✅
- Apple Music ✅
- Deezer ✅
- Jamendo ✅
- Audiomack ✅

### Q16: Spotify API key कैसे प्राप्त करें?
**A:**
1. Visit: https://developer.spotify.com/dashboard
2. Login करें
3. "Create an App" click करें
4. App details fill करें
5. Client ID और Secret copy करें

### Q17: क्या सभी platforms एक साथ use कर सकते हैं?
**A:** हाँ! आप सभी platforms को simultaneously enable कर सकते हैं। User किसी भी platform से search कर सकता है।

### Q18: Platform disable कैसे करें?
**A:** .env file में:
```env
ENABLE_JIOSAAVN=false  # Disabled
ENABLE_GAANA=true      # Enabled
```

### Q19: Indian music के लिए best platform कौन सा है?
**A:** JioSaavn, Gaana, और Wynk Indian music के लिए best हैं। सभी free हैं और API key नहीं चाहिए।

### Q20: International music के लिए?
**A:** Spotify, Apple Music, Deezer, और YouTube international music के लिए best हैं।

---

## 💬 Commands & Usage {#commands}

### Q21: Basic commands क्या हैं?
**A:**
```
/start - Bot शुरू करें
/help - Help message
/play <song> - YouTube से play
/jiosaavn <song> - JioSaavn से play
/gaana <song> - Gaana से play
/search <song> - सभी platforms पर search
/pause - Pause करें
/resume - Resume करें
/skip - Next song
/stop - Stop करें
```

### Q22: Short commands क्या हैं?
**A:**
```
/jio, /js - JioSaavn
/gn - Gaana
/wk - Wynk
/sp - Spotify
/yt - YouTube
/dz - Deezer
```

### Q23: Voice chat में कैसे use करें?
**A:**
1. Group में voice chat start करें
2. Bot को admin बनाएं
3. Command send करें: `/jiosaavn Kesariya`
4. Song select करें
5. Music play होगा!

### Q24: Multiple songs कैसे queue करें?
**A:** एक के बाद एक songs play करें। Bot automatically queue manage करेगा।

### Q25: Admin commands क्या हैं?
**A:**
```
/stats - Bot statistics
/broadcast <message> - सभी groups में message
```

---

## 🔧 Troubleshooting {#troubleshooting}

### Q26: Bot start नहीं हो रहा?
**A:** Check करें:
```bash
# Python version
python --version  # 3.8+ होना चाहिए

# Dependencies
pip install -r requirements.txt --upgrade

# .env file
cat .env  # सभी values correct हैं?

# MongoDB
sudo systemctl status mongodb
```

### Q27: "No results found" error आ रहा है?
**A:**
1. Internet connection check करें
2. Platform enabled है? `.env` में check करें
3. Different platform try करें
4. Search query change करें

### Q28: Download failed error?
**A:**
1. FFmpeg install है? `ffmpeg -version`
2. Downloads folder exist करता है? `mkdir downloads`
3. Disk space available है?
4. Internet stable है?

### Q29: Bot commands काम नहीं कर रहे?
**A:**
1. Bot को group में admin बनाएं
2. Bot को all permissions दें
3. Voice chat start करें
4. `/start` command send करें

### Q30: MongoDB connection error?
**A:**
```bash
# Local MongoDB check करें
sudo systemctl status mongodb
sudo systemctl start mongodb

# या Atlas connection string verify करें
# Format: mongodb+srv://user:pass@cluster.mongodb.net/db
```

### Q31: "Module not found" error?
**A:**
```bash
# सभी dependencies फिर से install करें
pip install -r requirements.txt --force-reinstall

# या specific module
pip install pyrogram --upgrade
```

### Q32: Voice chat में audio नहीं आ रहा?
**A:**
1. Voice chat active है?
2. Bot admin है?
3. Bot को voice chat permissions हैं?
4. FFmpeg properly install है?

---

## ⚡ Performance {#performance}

### Q33: Bot slow क्यों है?
**A:**
1. Server resources check करें
2. Internet speed check करें
3. Multiple platforms disable करें
4. Cache enable करें (if implemented)

### Q34: Memory usage ज्यादा है?
**A:**
1. Downloaded files regularly delete करें
2. Old sessions close करें
3. Restart bot periodically
4. Server RAM increase करें

### Q35: Bot crash हो जाता है?
**A:**
1. Logs check करें
2. Error messages note करें
3. Dependencies update करें
4. Systemd service use करें (auto-restart)

### Q36: Multiple users handle कर सकता है?
**A:** हाँ! Bot multiple users और groups को simultaneously handle कर सकता है।

---

## 🔬 Advanced {#advanced}

### Q37: Production में कैसे deploy करें?
**A:**
```bash
# Systemd service बनाएं
sudo nano /etc/systemd/system/musicbot.service

# Service enable करें
sudo systemctl enable musicbot
sudo systemctl start musicbot

# Logs देखें
sudo journalctl -u musicbot -f
```

### Q38: Multiple bot instances चला सकते हैं?
**A:** हाँ! Different bot tokens और ports use करें। Shared MongoDB use कर सकते हैं।

### Q39: Custom platform कैसे add करें?
**A:** CONTRIBUTING.md देखें। Step-by-step guide है नया platform add करने के लिए।

### Q40: Database backup कैसे लें?
**A:**
```bash
# MongoDB backup
mongodump --db musicbot --out /backup/

# Restore
mongorestore --db musicbot /backup/musicbot/
```

### Q41: Logs कहाँ हैं?
**A:**
```bash
# Direct run
# Console में दिखेंगे

# Systemd service
sudo journalctl -u musicbot -f

# Screen
screen -r musicbot
```

### Q42: Bot update कैसे करें?
**A:**
```bash
# Latest code pull करें
git pull origin main

# Dependencies update करें
pip install -r requirements.txt --upgrade

# Bot restart करें
sudo systemctl restart musicbot
```

### Q43: Custom commands add कर सकते हैं?
**A:** हाँ! `handlers/` में new file बनाएं और commands add करें।

### Q44: Rate limiting handle कैसे करें?
**A:** Platform APIs में built-in error handling है। Retry logic automatically काम करती है।

### Q45: Security best practices?
**A:**
1. `.env` file को git में commit न करें
2. Strong bot token use करें
3. Admin commands को restrict करें
4. Regular updates करें
5. Logs monitor करें

---

## 📊 Statistics & Monitoring

### Q46: Bot statistics कैसे देखें?
**A:** `/stats` command use करें। यह show करेगा:
- Total users
- Total groups
- Songs played
- Platform usage

### Q47: Logs monitor कैसे करें?
**A:**
```bash
# Real-time logs
sudo journalctl -u musicbot -f

# Last 100 lines
sudo journalctl -u musicbot -n 100

# Errors only
sudo journalctl -u musicbot -p err
```

---

## 🆘 Getting Help

### Q48: Help कहाँ से मिलेगी?
**A:**
1. **Documentation:** README.md, SETUP.md, PLATFORMS.md
2. **GitHub Issues:** Bug reports और feature requests
3. **Discussions:** Questions और ideas
4. **Community:** Telegram support group

### Q49: Bug report कैसे करें?
**A:** GitHub पर issue खोलें with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details

### Q50: Feature request कैसे करें?
**A:** GitHub पर feature request issue खोलें with:
- Problem description
- Proposed solution
- Alternative solutions
- Use cases

---

## 📚 Additional Resources

- **README.md** - Project overview
- **SETUP.md** - Detailed setup guide
- **PLATFORMS.md** - Platform documentation
- **ARCHITECTURE.md** - System architecture
- **CONTRIBUTING.md** - Contribution guide

---

**Still have questions? / अभी भी सवाल हैं?**
Open an issue on GitHub या documentation check करें! 🎵

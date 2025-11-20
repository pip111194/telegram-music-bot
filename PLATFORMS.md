# 🎵 Supported Music Platforms

## 🆓 Free Platforms (No API Key Required!)

### 1. **JioSaavn** 🎵
- **Commands:** `/jiosaavn`, `/jio`, `/js`
- **API Key:** Not required
- **Features:** Indian music, Bollywood, Regional songs
- **Example:** `/jiosaavn Kesariya`

### 2. **Gaana** 🎶
- **Commands:** `/gaana`, `/gn`
- **API Key:** Not required
- **Features:** Indian music, Bollywood, Regional songs
- **Example:** `/gaana Tum Hi Ho`

### 3. **Wynk Music** 🎧
- **Commands:** `/wynk`, `/wk`
- **API Key:** Not required
- **Features:** Indian music, International songs
- **Example:** `/wynk Apna Bana Le`

### 4. **Jamendo** 🎼
- **Commands:** `/jamendo`, `/jm`
- **API Key:** Optional (works without)
- **Features:** Creative Commons music, Free to use
- **Example:** `/jamendo Chill Music`

### 5. **Audiomack** 🎤
- **Commands:** `/audiomack`, `/am`
- **API Key:** Optional (works without)
- **Features:** Hip-Hop, Rap, Afrobeats
- **Example:** `/audiomack Hip Hop Beats`

### 6. **YouTube** 🔴
- **Commands:** `/play`, `/yt`
- **API Key:** Not required (uses yt-dlp)
- **Features:** All types of music and videos
- **Example:** `/play Shape of You`

### 7. **Apple Music** 🍎
- **Commands:** `/apple`, `/am`
- **API Key:** Not required (uses iTunes API)
- **Features:** International music
- **Example:** `/apple Blinding Lights`

### 8. **Deezer** 🔵
- **Commands:** `/deezer`, `/dz`
- **API Key:** Not required (uses public API)
- **Features:** International music
- **Example:** `/deezer Levitating`

---

## 🔑 Platforms with Optional API Keys

### 9. **Spotify** 🟢
- **Commands:** `/spotify`, `/sp`
- **API Key:** Optional (recommended for better results)
- **Get API Key:** https://developer.spotify.com/dashboard
- **Features:** Largest music library
- **Example:** `/spotify Starboy`

### 10. **SoundCloud** 🟠
- **Commands:** `/soundcloud`, `/sc`
- **API Key:** Optional
- **Get API Key:** https://soundcloud.com/you/apps
- **Features:** Independent artists, remixes
- **Example:** `/soundcloud Electronic Mix`

---

## 🎯 How to Use

### Basic Search
```
/jiosaavn Kesariya
/gaana Tum Hi Ho
/wynk Apna Bana Le
/play Shape of You
```

### Search All Platforms
```
/search Kesariya
```
This will search across ALL enabled platforms and show results from each.

### Platform-Specific Search
Use platform-specific commands to search only on that platform:
- `/jiosaavn <song name>` - Search JioSaavn only
- `/gaana <song name>` - Search Gaana only
- `/wynk <song name>` - Search Wynk only
- `/spotify <song name>` - Search Spotify only
- `/youtube <song name>` - Search YouTube only

---

## ⚙️ Configuration

### Enable/Disable Platforms

Edit your `.env` file:

```env
# Free Indian Platforms (No API key needed!)
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true

# Free International Platforms
ENABLE_JAMENDO=true
ENABLE_AUDIOMACK=true
ENABLE_YOUTUBE=true
ENABLE_APPLE_MUSIC=true
ENABLE_DEEZER=true

# Platforms with API keys
ENABLE_SPOTIFY=true
ENABLE_SOUNDCLOUD=true
```

### Add API Keys (Optional)

```env
# Spotify (Optional)
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret

# SoundCloud (Optional)
SOUNDCLOUD_CLIENT_ID=your_client_id

# Jamendo (Optional)
JAMENDO_CLIENT_ID=your_client_id

# Audiomack (Optional)
AUDIOMACK_API_KEY=your_api_key
```

---

## 🚀 Quick Start

### 1. Without Any API Keys
Just enable free platforms in `.env`:
```env
ENABLE_JIOSAAVN=true
ENABLE_GAANA=true
ENABLE_WYNK=true
ENABLE_YOUTUBE=true
```

Start using:
```
/jiosaavn Kesariya
/gaana Tum Hi Ho
/play Shape of You
```

### 2. With API Keys (Better Results)
Add Spotify/SoundCloud keys for more options:
```env
SPOTIFY_CLIENT_ID=your_id
SPOTIFY_CLIENT_SECRET=your_secret
ENABLE_SPOTIFY=true
```

---

## 📊 Platform Comparison

| Platform | Free | API Key | Indian Music | International | Quality |
|----------|------|---------|--------------|---------------|---------|
| JioSaavn | ✅ | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐ | High |
| Gaana | ✅ | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐ | High |
| Wynk | ✅ | ❌ | ⭐⭐⭐⭐ | ⭐⭐⭐ | High |
| YouTube | ✅ | ❌ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Variable |
| Jamendo | ✅ | Optional | ⭐⭐ | ⭐⭐⭐⭐ | High |
| Audiomack | ✅ | Optional | ⭐⭐ | ⭐⭐⭐⭐ | High |
| Apple Music | ✅ | ❌ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | High |
| Deezer | ✅ | ❌ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | High |
| Spotify | ✅ | Optional | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | High |
| SoundCloud | ✅ | Optional | ⭐⭐ | ⭐⭐⭐⭐ | Variable |

---

## 💡 Tips

1. **For Indian Music:** Use JioSaavn, Gaana, or Wynk
2. **For International Music:** Use Spotify, Apple Music, or Deezer
3. **For Everything:** Use YouTube
4. **For Creative Commons:** Use Jamendo
5. **For Hip-Hop/Rap:** Use Audiomack

---

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
3. YouTube is used as fallback for most platforms

---

## 📝 Notes

- **All free platforms work without any API keys!**
- **API keys are optional and only improve results**
- **You can enable/disable any platform anytime**
- **Multiple platforms can work simultaneously**
- **Bot automatically falls back to YouTube if direct download fails**

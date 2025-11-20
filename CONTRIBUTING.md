# 🤝 Contributing Guide / योगदान गाइड

Thank you for considering contributing to the Telegram Music Bot! / टेलीग्राम म्यूजिक बॉट में योगदान करने के लिए धन्यवाद!

## 📋 Table of Contents

1. [How to Contribute](#how-to-contribute)
2. [Development Setup](#development-setup)
3. [Code Guidelines](#code-guidelines)
4. [Adding New Platforms](#adding-new-platforms)
5. [Testing](#testing)
6. [Pull Request Process](#pull-request-process)

---

## 🚀 How to Contribute / कैसे योगदान करें

### Ways to Contribute
1. **Report bugs** - Issue खोलें
2. **Suggest features** - Feature request करें
3. **Fix bugs** - Bug fix PR submit करें
4. **Add platforms** - नया music platform add करें
5. **Improve docs** - Documentation improve करें
6. **Write tests** - Test cases add करें

---

## 💻 Development Setup / डेवलपमेंट सेटअप

### 1. Fork Repository
```bash
# GitHub पर fork button click करें
# फिर clone करें
git clone https://github.com/YOUR_USERNAME/telegram-music-bot.git
cd telegram-music-bot
```

### 2. Create Branch
```bash
# Feature branch बनाएं
git checkout -b feature/new-platform

# या Bug fix branch
git checkout -b fix/bug-description
```

### 3. Setup Development Environment
```bash
# Virtual environment बनाएं
python -m venv venv

# Activate करें
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Dependencies install करें
pip install -r requirements.txt
```

### 4. Configure .env
```bash
cp .env.example .env
# .env file edit करें
```

---

## 📝 Code Guidelines / कोड गाइडलाइन्स

### Python Style
- Follow **PEP 8** style guide
- Use **type hints** where possible
- Write **docstrings** for functions
- Keep functions **small and focused**

### Example:
```python
async def search_platform(
    self, 
    platform: str, 
    query: str, 
    limit: int = 10
) -> Optional[List[Dict]]:
    """
    Search specific platform for songs.
    
    Args:
        platform: Platform name (e.g., "jiosaavn")
        query: Search query string
        limit: Maximum number of results
        
    Returns:
        List of track dictionaries or None if error
        
    Example:
        results = await search_platform("jiosaavn", "Kesariya", 5)
    """
    if platform not in self.platforms:
        return None
    
    try:
        # Implementation
        pass
    except Exception as e:
        print(f"Error: {e}")
        return None
```

### File Structure
```python
# 1. Imports
import asyncio
from typing import List, Dict, Optional

# 2. Constants
BASE_URL = "https://api.example.com"

# 3. Classes
class PlatformAPI:
    def __init__(self):
        pass

# 4. Functions
async def helper_function():
    pass

# 5. Global instances
platform_api = PlatformAPI()
```

---

## 🎵 Adding New Platforms / नया प्लेटफॉर्म जोड़ना

### Step 1: Create Helper File
```python
# helpers/newplatform.py

"""
New Platform Music Integration
Description of the platform
"""

import aiohttp
from typing import List, Dict, Optional

class NewPlatformAPI:
    def __init__(self):
        self.base_url = "https://api.newplatform.com"
        self.session = None
    
    async def get_session(self):
        """Get or create aiohttp session"""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session
    
    async def close(self):
        """Close session"""
        if self.session and not self.session.closed:
            await self.session.close()
    
    def format_duration(self, seconds: int) -> str:
        """Convert seconds to MM:SS format"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"
    
    async def search(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for songs on New Platform
        
        Args:
            query: Search query
            limit: Maximum results
            
        Returns:
            List of track dictionaries
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/search"
            params = {
                "q": query,
                "limit": limit
            }
            
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    return []
                
                data = await response.json()
                
                tracks = []
                for song in data.get("results", [])[:limit]:
                    track = {
                        "id": song.get("id", ""),
                        "name": song.get("title", "Unknown"),
                        "artists": song.get("artist", "Unknown"),
                        "album": song.get("album", "Unknown"),
                        "duration": self.format_duration(song.get("duration", 0)),
                        "duration_seconds": song.get("duration", 0),
                        "image": song.get("image", ""),
                        "url": song.get("url", ""),
                        "platform": "newplatform"
                    }
                    tracks.append(track)
                
                return tracks
                
        except Exception as e:
            print(f"NewPlatform search error: {e}")
            return []
    
    async def get_song_details(self, song_id: str) -> Optional[Dict]:
        """Get detailed song information"""
        # Implementation
        pass
    
    async def get_download_url(self, song_id: str) -> Optional[str]:
        """Get direct download URL"""
        song_details = await self.get_song_details(song_id)
        if song_details:
            return song_details.get("download_url")
        return None

# Global instance
newplatform_api = NewPlatformAPI()
```

### Step 2: Update config.py
```python
# Add to config.py

# New Platform API Key (if needed)
NEWPLATFORM_API_KEY = os.getenv("NEWPLATFORM_API_KEY", "")

# Platform Settings
ENABLE_NEWPLATFORM = os.getenv("ENABLE_NEWPLATFORM", "true").lower() == "true"
```

### Step 3: Update music_platforms.py
```python
# Add import
from helpers.newplatform import newplatform_api

# Add to platforms dict
self.platforms = {
    # ... existing platforms
    "newplatform": newplatform_api
}

# Add to _get_enabled_platforms()
if Config.ENABLE_NEWPLATFORM:
    enabled.append("newplatform")

# Add to search_platform()
elif platform == "newplatform":
    return await newplatform_api.search(query, limit)

# Add to get_download_url()
elif platform == "newplatform":
    track_id = track_info.get("id")
    if track_id:
        return await newplatform_api.get_download_url(track_id)

# Add to get_platform_emoji()
"newplatform": "🎵"

# Add to get_platform_name()
"newplatform": "New Platform"
```

### Step 4: Create Handler
```python
# handlers/free_platforms.py or platforms.py

@Client.on_message(command(["newplatform", "np"]) & filters.group)
@authorized_users_only
@errors
async def newplatform_search(client: Client, message: Message):
    """Search and play from New Platform"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text(
            "❌ Please provide a song name!\n\n"
            "Example: `/newplatform Song Name`"
        )
    
    status = await message.reply_text("🎵 Searching on New Platform...")
    
    try:
        results = await music_manager.search_platform("newplatform", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on New Platform!")
        
        platform_results[message.from_user.id] = {
            "platform": "newplatform",
            "results": results
        }
        
        buttons = []
        for i, track in enumerate(results[:5], 1):
            title = track.get("name", "Unknown")[:35]
            artist = track.get("artists", "Unknown")[:20]
            duration = track.get("duration", "")
            buttons.append([
                InlineKeyboardButton(
                    f"{i}. {title} - {artist} ({duration})",
                    callback_data=f"platform_{message.from_user.id}_{i-1}"
                )
            ])
        
        buttons.append([
            InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_{message.from_user.id}")
        ])
        
        await status.edit_text(
            f"🎵 **New Platform Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")
```

### Step 5: Update Documentation
```markdown
# README.md
Add platform to list

# PLATFORMS.md
Add detailed platform documentation

# .env.example
Add configuration example
```

### Step 6: Test
```bash
# Test search
/newplatform Test Song

# Test playback
# Select song from results

# Test error handling
/newplatform
```

---

## 🧪 Testing / टेस्टिंग

### Manual Testing
```bash
# Start bot
python bot.py

# Test commands
/start
/help
/newplatform Test Song
/search Test Song
```

### Unit Testing (Optional)
```python
# tests/test_newplatform.py

import asyncio
import pytest
from helpers.newplatform import newplatform_api

@pytest.mark.asyncio
async def test_search():
    results = await newplatform_api.search("Test Song", 5)
    assert len(results) > 0
    assert results[0]['name'] is not None

@pytest.mark.asyncio
async def test_get_download_url():
    results = await newplatform_api.search("Test Song", 1)
    if results:
        url = await newplatform_api.get_download_url(results[0]['id'])
        assert url is not None
```

---

## 📤 Pull Request Process / पुल रिक्वेस्ट प्रोसेस

### 1. Commit Changes
```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "Add NewPlatform music integration"

# या detailed message
git commit -m "feat: Add NewPlatform music integration

- Add NewPlatform API helper
- Add search and download functionality
- Add command handler
- Update documentation
- Add configuration options"
```

### 2. Push to Fork
```bash
git push origin feature/new-platform
```

### 3. Create Pull Request
1. GitHub पर अपने fork पर जाएं
2. "Compare & pull request" button click करें
3. Clear title और description लिखें
4. Changes का summary दें
5. Screenshots add करें (if applicable)
6. "Create pull request" click करें

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Changes Made
- Added NewPlatform integration
- Updated configuration
- Added documentation

## Testing
- [ ] Tested locally
- [ ] All commands working
- [ ] Error handling tested

## Screenshots (if applicable)
Add screenshots here

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Tested thoroughly
```

---

## 🐛 Bug Reports / बग रिपोर्ट्स

### Bug Report Template
```markdown
**Describe the bug**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What you expected to happen

**Screenshots**
If applicable, add screenshots

**Environment:**
- OS: [e.g. Ubuntu 20.04]
- Python version: [e.g. 3.9]
- Bot version: [e.g. 1.0.0]

**Additional context**
Any other context about the problem
```

---

## 💡 Feature Requests / फीचर रिक्वेस्ट्स

### Feature Request Template
```markdown
**Is your feature request related to a problem?**
Clear description of the problem

**Describe the solution you'd like**
Clear description of what you want

**Describe alternatives you've considered**
Alternative solutions you've thought about

**Additional context**
Any other context or screenshots
```

---

## 📜 Code of Conduct / आचार संहिता

### Our Standards
- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

---

## 📞 Contact / संपर्क

- **GitHub Issues:** For bugs and features
- **Discussions:** For questions and ideas
- **Email:** [Your Email]

---

## 🙏 Recognition / मान्यता

Contributors will be:
- Listed in README.md
- Mentioned in release notes
- Given credit in documentation

---

**Thank you for contributing! / योगदान के लिए धन्यवाद!** 🎉

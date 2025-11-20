"""
Audiomack Music Platform Integration
Free music streaming - Optional API key
Works without API key with basic features
"""

import aiohttp
import asyncio
from typing import List, Dict, Optional
from config import Config

class AudiomackAPI:
    def __init__(self):
        self.base_url = "https://api.audiomack.com/v1"
        self.api_key = Config.AUDIOMACK_API_KEY
        self.session = None
    
    async def get_session(self):
        if self.session is None or self.session.closed:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            self.session = aiohttp.ClientSession(headers=headers)
        return self.session
    
    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()
    
    def format_duration(self, seconds: int) -> str:
        """Convert seconds to MM:SS format"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"
    
    async def search(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for songs on Audiomack
        Returns list of tracks with metadata
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/search"
            params = {
                "q": query,
                "type": "song",
                "limit": limit
            }
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            async with session.get(url, params=params, headers=headers) as response:
                if response.status != 200:
                    return []
                
                data = await response.json()
                
                if not data.get("results"):
                    return []
                
                tracks = []
                for song in data["results"][:limit]:
                    track = {
                        "id": song.get("id", ""),
                        "name": song.get("title", "Unknown"),
                        "artists": song.get("artist", "Unknown"),
                        "album": song.get("album", "Single"),
                        "duration": self.format_duration(int(song.get("duration", 0))),
                        "duration_seconds": int(song.get("duration", 0)),
                        "image": song.get("image", ""),
                        "url": song.get("url", ""),
                        "plays": song.get("plays", 0),
                        "platform": "audiomack"
                    }
                    tracks.append(track)
                
                return tracks
                
        except Exception as e:
            print(f"Audiomack search error: {e}")
            return []
    
    async def get_song_details(self, song_id: str) -> Optional[Dict]:
        """
        Get detailed information about a song
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/music/{song_id}"
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return None
                
                song = await response.json()
                
                return {
                    "id": song.get("id", ""),
                    "name": song.get("title", "Unknown"),
                    "artists": song.get("artist", "Unknown"),
                    "album": song.get("album", "Single"),
                    "duration": self.format_duration(int(song.get("duration", 0))),
                    "duration_seconds": int(song.get("duration", 0)),
                    "image": song.get("image_large", ""),
                    "url": song.get("url", ""),
                    "download_url": song.get("stream_url", ""),
                    "plays": song.get("plays", 0),
                    "platform": "audiomack"
                }
                
        except Exception as e:
            print(f"Audiomack get song details error: {e}")
            return None
    
    async def get_download_url(self, song_id: str) -> Optional[str]:
        """
        Get direct download URL for a song
        """
        song_details = await self.get_song_details(song_id)
        if song_details:
            return song_details.get("download_url")
        return None


# Global instance
audiomack_api = AudiomackAPI()

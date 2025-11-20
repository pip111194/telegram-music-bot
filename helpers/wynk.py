"""
Wynk Music Platform Integration
Free API - No authentication required!
"""

import aiohttp
import asyncio
from typing import List, Dict, Optional

class WynkAPI:
    def __init__(self):
        self.base_url = "https://wynk.in/music/api"
        self.session = None
    
    async def get_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session
    
    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()
    
    def format_duration(self, milliseconds: int) -> str:
        """Convert milliseconds to MM:SS format"""
        seconds = milliseconds // 1000
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"
    
    async def search(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for songs on Wynk Music
        Returns list of tracks with metadata
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/search/v1"
            params = {
                "q": query,
                "type": "song",
                "limit": limit
            }
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "x-bsy-date": "1",
                "x-bsy-utkn": "1"
            }
            
            async with session.get(url, params=params, headers=headers) as response:
                if response.status != 200:
                    return []
                
                data = await response.json()
                
                if not data.get("items"):
                    return []
                
                tracks = []
                for song in data["items"][:limit]:
                    track = {
                        "id": song.get("id", ""),
                        "name": song.get("title", "Unknown"),
                        "artists": ", ".join([a.get("name", "") for a in song.get("artists", [])]) or "Unknown",
                        "album": song.get("album", {}).get("title", "Unknown"),
                        "duration": self.format_duration(int(song.get("duration", 0))),
                        "duration_seconds": int(song.get("duration", 0)) // 1000,
                        "image": song.get("image", ""),
                        "url": f"https://wynk.in/music/song/{song.get('id', '')}",
                        "language": song.get("language", ""),
                        "platform": "wynk"
                    }
                    tracks.append(track)
                
                return tracks
                
        except Exception as e:
            print(f"Wynk search error: {e}")
            return []
    
    async def get_song_details(self, song_id: str) -> Optional[Dict]:
        """
        Get detailed information about a song
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/song/v1/{song_id}"
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "x-bsy-date": "1",
                "x-bsy-utkn": "1"
            }
            
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return None
                
                song = await response.json()
                
                return {
                    "id": song.get("id", ""),
                    "name": song.get("title", "Unknown"),
                    "artists": ", ".join([a.get("name", "") for a in song.get("artists", [])]) or "Unknown",
                    "album": song.get("album", {}).get("title", "Unknown"),
                    "duration": self.format_duration(int(song.get("duration", 0))),
                    "duration_seconds": int(song.get("duration", 0)) // 1000,
                    "image": song.get("image_large", ""),
                    "url": f"https://wynk.in/music/song/{song.get('id', '')}",
                    "download_url": song.get("stream_url", ""),
                    "language": song.get("language", ""),
                    "platform": "wynk"
                }
                
        except Exception as e:
            print(f"Wynk get song details error: {e}")
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
wynk_api = WynkAPI()

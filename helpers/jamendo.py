"""
Jamendo Music Platform Integration
Free Creative Commons Music - Optional API key
Works without API key with rate limits
"""

import aiohttp
import asyncio
from typing import List, Dict, Optional
from config import Config

class JamendoAPI:
    def __init__(self):
        self.base_url = "https://api.jamendo.com/v3.0"
        self.client_id = Config.JAMENDO_CLIENT_ID or "56d30c95"  # Default public key
        self.session = None
    
    async def get_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
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
        Search for songs on Jamendo
        Returns list of tracks with metadata
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/tracks"
            params = {
                "client_id": self.client_id,
                "format": "json",
                "limit": limit,
                "search": query,
                "include": "musicinfo",
                "audioformat": "mp32"
            }
            
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    return []
                
                data = await response.json()
                
                if not data.get("results"):
                    return []
                
                tracks = []
                for song in data["results"][:limit]:
                    track = {
                        "id": str(song.get("id", "")),
                        "name": song.get("name", "Unknown"),
                        "artists": song.get("artist_name", "Unknown"),
                        "album": song.get("album_name", "Unknown"),
                        "duration": self.format_duration(int(song.get("duration", 0))),
                        "duration_seconds": int(song.get("duration", 0)),
                        "image": song.get("album_image", ""),
                        "url": song.get("shareurl", ""),
                        "download_url": song.get("audio", ""),
                        "license": song.get("license_ccurl", "CC BY-SA"),
                        "platform": "jamendo"
                    }
                    tracks.append(track)
                
                return tracks
                
        except Exception as e:
            print(f"Jamendo search error: {e}")
            return []
    
    async def get_song_details(self, track_id: str) -> Optional[Dict]:
        """
        Get detailed information about a song
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/tracks"
            params = {
                "client_id": self.client_id,
                "format": "json",
                "id": track_id,
                "include": "musicinfo+licenses",
                "audioformat": "mp32"
            }
            
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    return None
                
                data = await response.json()
                
                if not data.get("results"):
                    return None
                
                song = data["results"][0]
                
                return {
                    "id": str(song.get("id", "")),
                    "name": song.get("name", "Unknown"),
                    "artists": song.get("artist_name", "Unknown"),
                    "album": song.get("album_name", "Unknown"),
                    "duration": self.format_duration(int(song.get("duration", 0))),
                    "duration_seconds": int(song.get("duration", 0)),
                    "image": song.get("album_image", ""),
                    "url": song.get("shareurl", ""),
                    "download_url": song.get("audio", ""),
                    "license": song.get("license_ccurl", "CC BY-SA"),
                    "platform": "jamendo"
                }
                
        except Exception as e:
            print(f"Jamendo get song details error: {e}")
            return None
    
    async def get_download_url(self, track_id: str) -> Optional[str]:
        """
        Get direct download URL for a song
        """
        song_details = await self.get_song_details(track_id)
        if song_details:
            return song_details.get("download_url")
        return None


# Global instance
jamendo_api = JamendoAPI()

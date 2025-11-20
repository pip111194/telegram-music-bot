"""
JioSaavn Music Platform Integration
Free API - No authentication required!
"""

import aiohttp
import asyncio
from typing import List, Dict, Optional

class JioSaavnAPI:
    def __init__(self):
        self.base_url = "https://www.jiosaavn.com/api.php"
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
        Search for songs on JioSaavn
        Returns list of tracks with metadata
        """
        try:
            session = await self.get_session()
            
            params = {
                "__call": "autocomplete.get",
                "_format": "json",
                "_marker": "0",
                "cc": "in",
                "includeMetaTags": "1",
                "query": query
            }
            
            async with session.get(self.base_url, params=params) as response:
                if response.status != 200:
                    return []
                
                data = await response.json()
                
                if not data.get("songs", {}).get("data"):
                    return []
                
                tracks = []
                for song in data["songs"]["data"][:limit]:
                    track = {
                        "id": song.get("id", ""),
                        "name": song.get("title", "Unknown"),
                        "artists": song.get("more_info", {}).get("singers", "Unknown"),
                        "album": song.get("more_info", {}).get("album", "Unknown"),
                        "duration": self.format_duration(int(song.get("more_info", {}).get("duration", "0"))),
                        "duration_seconds": int(song.get("more_info", {}).get("duration", "0")),
                        "image": song.get("image", ""),
                        "url": song.get("perma_url", ""),
                        "year": song.get("more_info", {}).get("year", ""),
                        "language": song.get("more_info", {}).get("language", ""),
                        "platform": "jiosaavn"
                    }
                    tracks.append(track)
                
                return tracks
                
        except Exception as e:
            print(f"JioSaavn search error: {e}")
            return []
    
    async def get_song_details(self, song_id: str) -> Optional[Dict]:
        """
        Get detailed information about a song
        """
        try:
            session = await self.get_session()
            
            params = {
                "__call": "song.getDetails",
                "_format": "json",
                "cc": "in",
                "pids": song_id
            }
            
            async with session.get(self.base_url, params=params) as response:
                if response.status != 200:
                    return None
                
                data = await response.json()
                
                if not data or not isinstance(data, dict):
                    return None
                
                song = data.get(song_id, {})
                
                return {
                    "id": song.get("id", ""),
                    "name": song.get("song", "Unknown"),
                    "artists": song.get("singers", "Unknown"),
                    "album": song.get("album", "Unknown"),
                    "duration": self.format_duration(int(song.get("duration", "0"))),
                    "duration_seconds": int(song.get("duration", "0")),
                    "image": song.get("image", "").replace("150x150", "500x500"),
                    "url": song.get("perma_url", ""),
                    "download_url": song.get("media_preview_url", ""),
                    "year": song.get("year", ""),
                    "language": song.get("language", ""),
                    "platform": "jiosaavn"
                }
                
        except Exception as e:
            print(f"JioSaavn get song details error: {e}")
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
jiosaavn_api = JioSaavnAPI()

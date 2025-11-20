"""
Gaana Music Platform Integration
Free API - No authentication required!
"""

import aiohttp
import asyncio
from typing import List, Dict, Optional

class GaanaAPI:
    def __init__(self):
        self.base_url = "https://api.gaana.com"
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
        Search for songs on Gaana
        Returns list of tracks with metadata
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/search/tracks"
            params = {
                "query": query,
                "limit": limit
            }
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            async with session.get(url, params=params, headers=headers) as response:
                if response.status != 200:
                    return []
                
                data = await response.json()
                
                if not data.get("tracks"):
                    return []
                
                tracks = []
                for song in data["tracks"][:limit]:
                    track = {
                        "id": song.get("track_id", ""),
                        "name": song.get("title", "Unknown"),
                        "artists": ", ".join([a.get("name", "") for a in song.get("artist", [])]) or "Unknown",
                        "album": song.get("album_title", "Unknown"),
                        "duration": self.format_duration(int(song.get("duration", 0))),
                        "duration_seconds": int(song.get("duration", 0)),
                        "image": song.get("artwork", ""),
                        "url": song.get("seokey", ""),
                        "language": song.get("language", ""),
                        "platform": "gaana"
                    }
                    tracks.append(track)
                
                return tracks
                
        except Exception as e:
            print(f"Gaana search error: {e}")
            return []
    
    async def get_song_details(self, track_id: str) -> Optional[Dict]:
        """
        Get detailed information about a song
        """
        try:
            session = await self.get_session()
            
            url = f"{self.base_url}/track/{track_id}"
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return None
                
                song = await response.json()
                
                return {
                    "id": song.get("track_id", ""),
                    "name": song.get("title", "Unknown"),
                    "artists": ", ".join([a.get("name", "") for a in song.get("artist", [])]) or "Unknown",
                    "album": song.get("album_title", "Unknown"),
                    "duration": self.format_duration(int(song.get("duration", 0))),
                    "duration_seconds": int(song.get("duration", 0)),
                    "image": song.get("artwork_large", ""),
                    "url": song.get("seokey", ""),
                    "download_url": song.get("stream_url", ""),
                    "language": song.get("language", ""),
                    "platform": "gaana"
                }
                
        except Exception as e:
            print(f"Gaana get song details error: {e}")
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
gaana_api = GaanaAPI()

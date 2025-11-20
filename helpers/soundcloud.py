import aiohttp
from typing import Optional, List, Dict
import os

class SoundCloudHelper:
    def __init__(self):
        self.client_id = os.getenv("SOUNDCLOUD_CLIENT_ID", "")
        self.base_url = "https://api-v2.soundcloud.com"
    
    async def search_track(self, query: str, limit: int = 10) -> Optional[List[Dict]]:
        """Search for tracks on SoundCloud"""
        params = {
            "q": query,
            "client_id": self.client_id,
            "limit": limit,
            "offset": 0
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/search/tracks", params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                results = []
                
                for track in data.get("collection", []):
                    results.append({
                        "id": track.get("id"),
                        "title": track.get("title"),
                        "artist": track.get("user", {}).get("username"),
                        "duration_ms": track.get("duration"),
                        "duration": self._format_duration(track.get("duration", 0)),
                        "genre": track.get("genre"),
                        "artwork": track.get("artwork_url", "").replace("large", "t500x500") if track.get("artwork_url") else None,
                        "playback_count": track.get("playback_count", 0),
                        "likes_count": track.get("likes_count", 0),
                        "permalink_url": track.get("permalink_url"),
                        "created_at": track.get("created_at")
                    })
                
                return results
    
    async def get_track(self, track_id: int) -> Optional[Dict]:
        """Get track details by ID"""
        params = {"client_id": self.client_id}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/tracks/{track_id}", params=params) as resp:
                if resp.status != 200:
                    return None
                
                track = await resp.json()
                return {
                    "id": track.get("id"),
                    "title": track.get("title"),
                    "artist": track.get("user", {}).get("username"),
                    "duration": self._format_duration(track.get("duration", 0)),
                    "genre": track.get("genre"),
                    "artwork": track.get("artwork_url", "").replace("large", "t500x500") if track.get("artwork_url") else None,
                    "playback_count": track.get("playback_count", 0),
                    "likes_count": track.get("likes_count", 0),
                    "permalink_url": track.get("permalink_url"),
                    "description": track.get("description")
                }
    
    async def search_playlist(self, query: str, limit: int = 10) -> Optional[List[Dict]]:
        """Search for playlists on SoundCloud"""
        params = {
            "q": query,
            "client_id": self.client_id,
            "limit": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/search/playlists", params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                results = []
                
                for playlist in data.get("collection", []):
                    results.append({
                        "id": playlist.get("id"),
                        "title": playlist.get("title"),
                        "creator": playlist.get("user", {}).get("username"),
                        "track_count": playlist.get("track_count"),
                        "duration": self._format_duration(playlist.get("duration", 0)),
                        "artwork": playlist.get("artwork_url"),
                        "permalink_url": playlist.get("permalink_url")
                    })
                
                return results
    
    def _format_duration(self, ms: int) -> str:
        """Format duration from milliseconds to MM:SS"""
        if not ms:
            return "Unknown"
        seconds = ms // 1000
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"

soundcloud = SoundCloudHelper()

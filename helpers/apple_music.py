import aiohttp
from typing import Optional, List, Dict

class AppleMusicHelper:
    def __init__(self):
        self.base_url = "https://api.music.apple.com/v1"
        # Apple Music uses iTunes Search API for public access
        self.itunes_url = "https://itunes.apple.com/search"
    
    async def search_track(self, query: str, limit: int = 10) -> Optional[List[Dict]]:
        """Search for tracks on Apple Music via iTunes API"""
        params = {
            "term": query,
            "media": "music",
            "entity": "song",
            "limit": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.itunes_url, params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                results = []
                
                for track in data.get("results", []):
                    results.append({
                        "id": track.get("trackId"),
                        "name": track.get("trackName"),
                        "artists": track.get("artistName"),
                        "album": track.get("collectionName"),
                        "duration_ms": track.get("trackTimeMillis", 0),
                        "duration": self._format_duration(track.get("trackTimeMillis", 0)),
                        "preview_url": track.get("previewUrl"),
                        "artwork": track.get("artworkUrl100", "").replace("100x100", "600x600"),
                        "release_date": track.get("releaseDate"),
                        "genre": track.get("primaryGenreName"),
                        "price": track.get("trackPrice"),
                        "country": track.get("country")
                    })
                
                return results
    
    async def search_album(self, query: str, limit: int = 10) -> Optional[List[Dict]]:
        """Search for albums on Apple Music"""
        params = {
            "term": query,
            "media": "music",
            "entity": "album",
            "limit": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.itunes_url, params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                results = []
                
                for album in data.get("results", []):
                    results.append({
                        "id": album.get("collectionId"),
                        "name": album.get("collectionName"),
                        "artists": album.get("artistName"),
                        "track_count": album.get("trackCount"),
                        "release_date": album.get("releaseDate"),
                        "artwork": album.get("artworkUrl100", "").replace("100x100", "600x600"),
                        "genre": album.get("primaryGenreName"),
                        "price": album.get("collectionPrice")
                    })
                
                return results
    
    async def get_album_tracks(self, album_id: int) -> Optional[List[Dict]]:
        """Get tracks from an album"""
        params = {
            "id": album_id,
            "entity": "song"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get("https://itunes.apple.com/lookup", params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                results = []
                
                for track in data.get("results", [])[1:]:  # Skip first item (album info)
                    results.append({
                        "name": track.get("trackName"),
                        "artists": track.get("artistName"),
                        "duration": self._format_duration(track.get("trackTimeMillis", 0)),
                        "track_number": track.get("trackNumber"),
                        "preview_url": track.get("previewUrl")
                    })
                
                return results
    
    def _format_duration(self, ms: int) -> str:
        """Format duration from milliseconds to MM:SS"""
        if not ms:
            return "Unknown"
        seconds = ms // 1000
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes}:{seconds:02d}"

apple_music = AppleMusicHelper()

import aiohttp
from typing import Optional, List, Dict

class DeezerHelper:
    def __init__(self):
        self.base_url = "https://api.deezer.com"
    
    async def search_track(self, query: str, limit: int = 10) -> Optional[List[Dict]]:
        """Search for tracks on Deezer"""
        params = {
            "q": query,
            "limit": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/search", params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                results = []
                
                for track in data.get("data", []):
                    results.append({
                        "id": track.get("id"),
                        "title": track.get("title"),
                        "artist": track.get("artist", {}).get("name"),
                        "album": track.get("album", {}).get("title"),
                        "duration": self._format_duration(track.get("duration", 0)),
                        "preview_url": track.get("preview"),
                        "artwork": track.get("album", {}).get("cover_xl"),
                        "link": track.get("link"),
                        "rank": track.get("rank")
                    })
                
                return results
    
    async def get_track(self, track_id: int) -> Optional[Dict]:
        """Get track details by ID"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/track/{track_id}") as resp:
                if resp.status != 200:
                    return None
                
                track = await resp.json()
                return {
                    "id": track.get("id"),
                    "title": track.get("title"),
                    "artist": track.get("artist", {}).get("name"),
                    "album": track.get("album", {}).get("title"),
                    "duration": self._format_duration(track.get("duration", 0)),
                    "preview_url": track.get("preview"),
                    "artwork": track.get("album", {}).get("cover_xl"),
                    "link": track.get("link"),
                    "release_date": track.get("release_date"),
                    "bpm": track.get("bpm"),
                    "gain": track.get("gain")
                }
    
    async def get_album(self, album_id: int) -> Optional[Dict]:
        """Get album details"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/album/{album_id}") as resp:
                if resp.status != 200:
                    return None
                
                album = await resp.json()
                tracks = []
                
                for track in album.get("tracks", {}).get("data", []):
                    tracks.append({
                        "title": track.get("title"),
                        "artist": track.get("artist", {}).get("name"),
                        "duration": self._format_duration(track.get("duration", 0)),
                        "track_position": track.get("track_position")
                    })
                
                return {
                    "title": album.get("title"),
                    "artist": album.get("artist", {}).get("name"),
                    "release_date": album.get("release_date"),
                    "tracks": tracks,
                    "artwork": album.get("cover_xl"),
                    "genre": album.get("genres", {}).get("data", [{}])[0].get("name") if album.get("genres", {}).get("data") else None
                }
    
    async def get_playlist(self, playlist_id: int) -> Optional[Dict]:
        """Get playlist details"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/playlist/{playlist_id}") as resp:
                if resp.status != 200:
                    return None
                
                playlist = await resp.json()
                tracks = []
                
                for track in playlist.get("tracks", {}).get("data", []):
                    tracks.append({
                        "title": track.get("title"),
                        "artist": track.get("artist", {}).get("name"),
                        "duration": self._format_duration(track.get("duration", 0))
                    })
                
                return {
                    "title": playlist.get("title"),
                    "creator": playlist.get("creator", {}).get("name"),
                    "tracks": tracks,
                    "artwork": playlist.get("picture_xl"),
                    "fans": playlist.get("fans")
                }
    
    async def search_artist(self, query: str, limit: int = 10) -> Optional[List[Dict]]:
        """Search for artists on Deezer"""
        params = {
            "q": query,
            "limit": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/search/artist", params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                results = []
                
                for artist in data.get("data", []):
                    results.append({
                        "id": artist.get("id"),
                        "name": artist.get("name"),
                        "picture": artist.get("picture_xl"),
                        "nb_album": artist.get("nb_album"),
                        "nb_fan": artist.get("nb_fan"),
                        "link": artist.get("link")
                    })
                
                return results
    
    def _format_duration(self, seconds: int) -> str:
        """Format duration from seconds to MM:SS"""
        if not seconds:
            return "Unknown"
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"

deezer = DeezerHelper()

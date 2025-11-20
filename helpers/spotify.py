import aiohttp
import base64
from typing import Optional, List, Dict
import os

class SpotifyHelper:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")
        self.base_url = "https://api.spotify.com/v1"
        self.token_url = "https://accounts.spotify.com/api/token"
        self.access_token = None
    
    async def get_access_token(self) -> str:
        """Get Spotify access token"""
        if self.access_token:
            return self.access_token
        
        auth_str = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_str.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
        
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = {"grant_type": "client_credentials"}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.token_url, headers=headers, data=data) as resp:
                result = await resp.json()
                self.access_token = result.get("access_token")
                return self.access_token
    
    async def search_track(self, query: str, limit: int = 10) -> Optional[List[Dict]]:
        """Search for tracks on Spotify"""
        token = await self.get_access_token()
        
        headers = {"Authorization": f"Bearer {token}"}
        params = {
            "q": query,
            "type": "track",
            "limit": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/search", headers=headers, params=params) as resp:
                if resp.status != 200:
                    return None
                
                data = await resp.json()
                tracks = data.get("tracks", {}).get("items", [])
                
                results = []
                for track in tracks:
                    results.append({
                        "id": track["id"],
                        "name": track["name"],
                        "artists": ", ".join([artist["name"] for artist in track["artists"]]),
                        "album": track["album"]["name"],
                        "duration_ms": track["duration_ms"],
                        "duration": self._format_duration(track["duration_ms"]),
                        "preview_url": track.get("preview_url"),
                        "external_url": track["external_urls"]["spotify"],
                        "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
                        "isrc": track.get("external_ids", {}).get("isrc")
                    })
                
                return results
    
    async def get_track(self, track_id: str) -> Optional[Dict]:
        """Get track details by ID"""
        token = await self.get_access_token()
        
        headers = {"Authorization": f"Bearer {token}"}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/tracks/{track_id}", headers=headers) as resp:
                if resp.status != 200:
                    return None
                
                track = await resp.json()
                return {
                    "id": track["id"],
                    "name": track["name"],
                    "artists": ", ".join([artist["name"] for artist in track["artists"]]),
                    "album": track["album"]["name"],
                    "duration_ms": track["duration_ms"],
                    "duration": self._format_duration(track["duration_ms"]),
                    "preview_url": track.get("preview_url"),
                    "external_url": track["external_urls"]["spotify"],
                    "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
                    "isrc": track.get("external_ids", {}).get("isrc")
                }
    
    async def get_playlist(self, playlist_id: str) -> Optional[Dict]:
        """Get playlist details"""
        token = await self.get_access_token()
        
        headers = {"Authorization": f"Bearer {token}"}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/playlists/{playlist_id}", headers=headers) as resp:
                if resp.status != 200:
                    return None
                
                playlist = await resp.json()
                tracks = []
                
                for item in playlist["tracks"]["items"]:
                    track = item["track"]
                    if track:
                        tracks.append({
                            "name": track["name"],
                            "artists": ", ".join([artist["name"] for artist in track["artists"]]),
                            "duration": self._format_duration(track["duration_ms"]),
                            "isrc": track.get("external_ids", {}).get("isrc")
                        })
                
                return {
                    "name": playlist["name"],
                    "description": playlist.get("description", ""),
                    "total_tracks": playlist["tracks"]["total"],
                    "tracks": tracks,
                    "image": playlist["images"][0]["url"] if playlist["images"] else None
                }
    
    async def get_album(self, album_id: str) -> Optional[Dict]:
        """Get album details"""
        token = await self.get_access_token()
        
        headers = {"Authorization": f"Bearer {token}"}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/albums/{album_id}", headers=headers) as resp:
                if resp.status != 200:
                    return None
                
                album = await resp.json()
                tracks = []
                
                for track in album["tracks"]["items"]:
                    tracks.append({
                        "name": track["name"],
                        "artists": ", ".join([artist["name"] for artist in track["artists"]]),
                        "duration": self._format_duration(track["duration_ms"])
                    })
                
                return {
                    "name": album["name"],
                    "artists": ", ".join([artist["name"] for artist in album["artists"]]),
                    "release_date": album["release_date"],
                    "total_tracks": album["total_tracks"],
                    "tracks": tracks,
                    "image": album["images"][0]["url"] if album["images"] else None
                }
    
    def _format_duration(self, ms: int) -> str:
        """Format duration from milliseconds to MM:SS"""
        seconds = ms // 1000
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes}:{seconds:02d}"

spotify = SpotifyHelper()

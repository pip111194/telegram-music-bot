from typing import Optional, List, Dict
from helpers.spotify import spotify
from helpers.apple_music import apple_music
from helpers.soundcloud import soundcloud
from helpers.deezer import deezer
from helpers.ytdl import ytdl

class MusicPlatformManager:
    """Unified manager for all music platforms"""
    
    def __init__(self):
        self.platforms = {
            "spotify": spotify,
            "apple": apple_music,
            "soundcloud": soundcloud,
            "deezer": deezer,
            "youtube": ytdl
        }
    
    async def search_all_platforms(self, query: str, limit: int = 5) -> Dict[str, List]:
        """Search across all platforms"""
        results = {}
        
        # Spotify
        try:
            spotify_results = await spotify.search_track(query, limit)
            if spotify_results:
                results["spotify"] = spotify_results
        except Exception as e:
            print(f"Spotify search error: {e}")
        
        # Apple Music
        try:
            apple_results = await apple_music.search_track(query, limit)
            if apple_results:
                results["apple_music"] = apple_results
        except Exception as e:
            print(f"Apple Music search error: {e}")
        
        # SoundCloud
        try:
            soundcloud_results = await soundcloud.search_track(query, limit)
            if soundcloud_results:
                results["soundcloud"] = soundcloud_results
        except Exception as e:
            print(f"SoundCloud search error: {e}")
        
        # Deezer
        try:
            deezer_results = await deezer.search_track(query, limit)
            if deezer_results:
                results["deezer"] = deezer_results
        except Exception as e:
            print(f"Deezer search error: {e}")
        
        # YouTube
        try:
            youtube_results = await ytdl.search(query, limit)
            if youtube_results:
                results["youtube"] = youtube_results
        except Exception as e:
            print(f"YouTube search error: {e}")
        
        return results
    
    async def search_platform(self, platform: str, query: str, limit: int = 10) -> Optional[List]:
        """Search specific platform"""
        if platform not in self.platforms:
            return None
        
        try:
            if platform == "youtube":
                return await ytdl.search(query, limit)
            elif platform == "spotify":
                return await spotify.search_track(query, limit)
            elif platform == "apple":
                return await apple_music.search_track(query, limit)
            elif platform == "soundcloud":
                return await soundcloud.search_track(query, limit)
            elif platform == "deezer":
                return await deezer.search_track(query, limit)
        except Exception as e:
            print(f"Platform {platform} search error: {e}")
            return None
    
    async def get_download_url(self, platform: str, track_info: Dict) -> Optional[str]:
        """Get downloadable URL from track info"""
        try:
            if platform == "youtube":
                return track_info.get("link")
            
            elif platform == "spotify":
                # Search YouTube with Spotify track info
                search_query = f"{track_info.get('name')} {track_info.get('artists')}"
                youtube_results = await ytdl.search(search_query, limit=1)
                if youtube_results:
                    return youtube_results[0].get("link")
            
            elif platform == "apple_music":
                # Search YouTube with Apple Music track info
                search_query = f"{track_info.get('name')} {track_info.get('artists')}"
                youtube_results = await ytdl.search(search_query, limit=1)
                if youtube_results:
                    return youtube_results[0].get("link")
            
            elif platform == "soundcloud":
                # SoundCloud tracks need special handling
                # For now, search on YouTube
                search_query = f"{track_info.get('title')} {track_info.get('artist')}"
                youtube_results = await ytdl.search(search_query, limit=1)
                if youtube_results:
                    return youtube_results[0].get("link")
            
            elif platform == "deezer":
                # Search YouTube with Deezer track info
                search_query = f"{track_info.get('title')} {track_info.get('artist')}"
                youtube_results = await ytdl.search(search_query, limit=1)
                if youtube_results:
                    return youtube_results[0].get("link")
            
        except Exception as e:
            print(f"Get download URL error: {e}")
            return None
    
    def get_platform_emoji(self, platform: str) -> str:
        """Get emoji for platform"""
        emojis = {
            "spotify": "🟢",
            "apple_music": "🍎",
            "soundcloud": "🟠",
            "deezer": "🔵",
            "youtube": "🔴"
        }
        return emojis.get(platform, "🎵")
    
    def get_platform_name(self, platform: str) -> str:
        """Get display name for platform"""
        names = {
            "spotify": "Spotify",
            "apple_music": "Apple Music",
            "soundcloud": "SoundCloud",
            "deezer": "Deezer",
            "youtube": "YouTube"
        }
        return names.get(platform, platform.title())

music_manager = MusicPlatformManager()

from typing import Optional, List, Dict
from config import Config

# Import existing platforms
from helpers.spotify import spotify
from helpers.apple_music import apple_music
from helpers.soundcloud import soundcloud
from helpers.deezer import deezer
from helpers.ytdl import ytdl

# Import new free platforms
from helpers.jiosaavn import jiosaavn_api
from helpers.gaana import gaana_api
from helpers.wynk import wynk_api
from helpers.jamendo import jamendo_api
from helpers.audiomack import audiomack_api

class MusicPlatformManager:
    """Unified manager for all music platforms - Free & Paid"""
    
    def __init__(self):
        # All available platforms
        self.platforms = {
            # Existing platforms
            "spotify": spotify,
            "apple": apple_music,
            "soundcloud": soundcloud,
            "deezer": deezer,
            "youtube": ytdl,
            
            # New free platforms (No API key needed!)
            "jiosaavn": jiosaavn_api,
            "gaana": gaana_api,
            "wynk": wynk_api,
            "jamendo": jamendo_api,
            "audiomack": audiomack_api
        }
        
        # Platform enable/disable settings
        self.enabled_platforms = self._get_enabled_platforms()
    
    def _get_enabled_platforms(self) -> List[str]:
        """Get list of enabled platforms from config"""
        enabled = []
        
        if Config.ENABLE_SPOTIFY:
            enabled.append("spotify")
        if Config.ENABLE_APPLE_MUSIC:
            enabled.append("apple")
        if Config.ENABLE_SOUNDCLOUD:
            enabled.append("soundcloud")
        if Config.ENABLE_DEEZER:
            enabled.append("deezer")
        if Config.ENABLE_YOUTUBE:
            enabled.append("youtube")
        if Config.ENABLE_JIOSAAVN:
            enabled.append("jiosaavn")
        if Config.ENABLE_GAANA:
            enabled.append("gaana")
        if Config.ENABLE_WYNK:
            enabled.append("wynk")
        if Config.ENABLE_JAMENDO:
            enabled.append("jamendo")
        if Config.ENABLE_AUDIOMACK:
            enabled.append("audiomack")
        
        return enabled
    
    async def search_all_platforms(self, query: str, limit: int = 5) -> Dict[str, List]:
        """Search across all enabled platforms"""
        results = {}
        
        # Search each enabled platform
        for platform in self.enabled_platforms:
            try:
                platform_results = await self.search_platform(platform, query, limit)
                if platform_results:
                    results[platform] = platform_results
            except Exception as e:
                print(f"{platform} search error: {e}")
        
        return results
    
    async def search_platform(self, platform: str, query: str, limit: int = 10) -> Optional[List]:
        """Search specific platform"""
        if platform not in self.platforms:
            return None
        
        if platform not in self.enabled_platforms:
            return None
        
        try:
            # YouTube
            if platform == "youtube":
                return await ytdl.search(query, limit)
            
            # Spotify
            elif platform == "spotify":
                return await spotify.search_track(query, limit)
            
            # Apple Music
            elif platform == "apple":
                return await apple_music.search_track(query, limit)
            
            # SoundCloud
            elif platform == "soundcloud":
                return await soundcloud.search_track(query, limit)
            
            # Deezer
            elif platform == "deezer":
                return await deezer.search_track(query, limit)
            
            # JioSaavn (Free!)
            elif platform == "jiosaavn":
                return await jiosaavn_api.search(query, limit)
            
            # Gaana (Free!)
            elif platform == "gaana":
                return await gaana_api.search(query, limit)
            
            # Wynk (Free!)
            elif platform == "wynk":
                return await wynk_api.search(query, limit)
            
            # Jamendo (Free!)
            elif platform == "jamendo":
                return await jamendo_api.search(query, limit)
            
            # Audiomack (Free!)
            elif platform == "audiomack":
                return await audiomack_api.search(query, limit)
            
        except Exception as e:
            print(f"Platform {platform} search error: {e}")
            return None
    
    async def get_download_url(self, platform: str, track_info: Dict) -> Optional[str]:
        """Get downloadable URL from track info"""
        try:
            # Direct download platforms
            if platform in ["jiosaavn", "gaana", "wynk", "jamendo", "audiomack"]:
                track_id = track_info.get("id")
                if track_id:
                    if platform == "jiosaavn":
                        return await jiosaavn_api.get_download_url(track_id)
                    elif platform == "gaana":
                        return await gaana_api.get_download_url(track_id)
                    elif platform == "wynk":
                        return await wynk_api.get_download_url(track_id)
                    elif platform == "jamendo":
                        return await jamendo_api.get_download_url(track_id)
                    elif platform == "audiomack":
                        return await audiomack_api.get_download_url(track_id)
            
            # YouTube direct
            elif platform == "youtube":
                return track_info.get("link")
            
            # Platforms that need YouTube fallback
            elif platform in ["spotify", "apple", "soundcloud", "deezer"]:
                # Build search query
                if platform == "spotify" or platform == "apple":
                    search_query = f"{track_info.get('name')} {track_info.get('artists')}"
                else:
                    search_query = f"{track_info.get('title')} {track_info.get('artist')}"
                
                # Search YouTube
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
            "apple": "🍎",
            "soundcloud": "🟠",
            "deezer": "🔵",
            "youtube": "🔴",
            "jiosaavn": "🎵",
            "gaana": "🎶",
            "wynk": "🎧",
            "jamendo": "🎼",
            "audiomack": "🎤"
        }
        return emojis.get(platform, "🎵")
    
    def get_platform_name(self, platform: str) -> str:
        """Get display name for platform"""
        names = {
            "spotify": "Spotify",
            "apple": "Apple Music",
            "soundcloud": "SoundCloud",
            "deezer": "Deezer",
            "youtube": "YouTube",
            "jiosaavn": "JioSaavn",
            "gaana": "Gaana",
            "wynk": "Wynk Music",
            "jamendo": "Jamendo",
            "audiomack": "Audiomack"
        }
        return names.get(platform, platform.title())
    
    def is_platform_enabled(self, platform: str) -> bool:
        """Check if platform is enabled"""
        return platform in self.enabled_platforms
    
    def get_enabled_platforms_list(self) -> List[str]:
        """Get list of enabled platforms"""
        return self.enabled_platforms.copy()

music_manager = MusicPlatformManager()

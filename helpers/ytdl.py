import yt_dlp
from youtubesearchpython import VideosSearch
import asyncio

class YTDLHelper:
    def __init__(self):
        self.opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
            "extract_flat": False,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    
    async def download(self, url: str):
        loop = asyncio.get_event_loop()
        with yt_dlp.YoutubeDL(self.opts) as ydl:
            info = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=True))
            filename = ydl.prepare_filename(info)
            return filename, info
    
    async def search(self, query: str, limit: int = 5):
        try:
            loop = asyncio.get_event_loop()
            search = await loop.run_in_executor(None, lambda: VideosSearch(query, limit=limit))
            result = await loop.run_in_executor(None, search.result)
            
            if result and "result" in result and result["result"]:
                return result["result"]
            return None
        except Exception as e:
            print(f"Search error: {e}")
            return None
    
    async def get_info(self, url: str):
        loop = asyncio.get_event_loop()
        with yt_dlp.YoutubeDL(self.opts) as ydl:
            info = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))
            
            duration_str = self._format_duration(info.get("duration", 0))
            
            return {
                "title": info.get("title", "Unknown"),
                "duration": info.get("duration", 0),
                "duration_str": duration_str,
                "thumbnail": info.get("thumbnail", ""),
                "url": info.get("webpage_url", url),
                "uploader": info.get("uploader", "Unknown"),
                "views": info.get("view_count", 0)
            }
    
    def _format_duration(self, seconds: int) -> str:
        if not seconds:
            return "Unknown"
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"

ytdl = YTDLHelper()

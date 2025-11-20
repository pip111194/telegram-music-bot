import yt_dlp
from youtubesearchpython import VideosSearch

class YTDLHelper:
    def __init__(self):
        self.opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
        }
    
    async def download(self, url: str):
        with yt_dlp.YoutubeDL(self.opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info), info
    
    async def search(self, query: str, limit: int = 1):
        search = VideosSearch(query, limit=limit)
        result = search.result()
        if result and result["result"]:
            return result["result"]
        return None
    
    async def get_info(self, url: str):
        with yt_dlp.YoutubeDL(self.opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title"),
                "duration": info.get("duration"),
                "thumbnail": info.get("thumbnail"),
                "url": info.get("webpage_url"),
                "uploader": info.get("uploader")
            }

ytdl = YTDLHelper()

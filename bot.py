import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
from config import Config
from helpers.decorators import authorized_users_only
from helpers.filters import command
from handlers import music, admin, misc

load_dotenv()

class MusicBot(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="handlers")
        )
    
    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"🎵 Music Bot Started: @{me.username}")
        
    async def stop(self):
        await super().stop()
        print("🛑 Music Bot Stopped")

if __name__ == "__main__":
    bot = MusicBot()
    bot.run()

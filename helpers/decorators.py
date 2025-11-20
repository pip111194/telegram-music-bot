from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from config import Config

def authorized_users_only(func: Callable) -> Callable:
    async def wrapper(client: Client, message: Message):
        if message.from_user.id == Config.OWNER_ID:
            return await func(client, message)
        
        if message.chat.type == "private":
            return await func(client, message)
        
        user = await message.chat.get_member(message.from_user.id)
        if user.status in ["creator", "administrator"]:
            return await func(client, message)
        
        await message.reply_text("❌ Only admins can use this command!")
    
    return wrapper

def errors(func: Callable) -> Callable:
    async def wrapper(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply_text(f"❌ Error: {str(e)}")
            print(f"Error in {func.__name__}: {e}")
    
    return wrapper

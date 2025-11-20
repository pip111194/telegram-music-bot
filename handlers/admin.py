from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.decorators import errors
from helpers.filters import command
from helpers.database import db
from config import Config

@Client.on_message(command("broadcast") & filters.user(Config.OWNER_ID))
@errors
async def broadcast(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("❌ Reply to a message to broadcast!")
    
    chats = await db.get_all_chats()
    success = 0
    failed = 0
    
    status = await message.reply_text("📡 Broadcasting...")
    
    for chat in chats:
        try:
            await message.reply_to_message.copy(chat["chat_id"])
            success += 1
        except:
            failed += 1
    
    await status.edit_text(
        f"✅ Broadcast completed!\n\n"
        f"**Success:** {success}\n"
        f"**Failed:** {failed}"
    )

@Client.on_message(command("stats") & filters.user(Config.OWNER_ID))
@errors
async def stats(client: Client, message: Message):
    chats = await db.get_all_chats()
    users = await db.get_all_users()
    
    await message.reply_text(
        f"📊 **Bot Statistics:**\n\n"
        f"**Total Chats:** {len(chats)}\n"
        f"**Total Users:** {len(users)}"
    )

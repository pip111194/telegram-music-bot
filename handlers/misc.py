from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import errors
from helpers.filters import command
from helpers.database import db

@Client.on_message(command("start") & filters.private)
@errors
async def start(client: Client, message: Message):
    await db.add_user(message.from_user.id, message.from_user.username or "")
    
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        f"I'm a Music Bot that can play songs in voice chats.\n\n"
        f"**Commands:**\n"
        f"• /play - Play a song\n"
        f"• /pause - Pause current song\n"
        f"• /resume - Resume playback\n"
        f"• /skip - Skip to next song\n"
        f"• /stop - Stop playback\n"
        f"• /queue - Show queue\n"
        f"• /help - Show help",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")]
        ])
    )

@Client.on_message(command("help"))
@errors
async def help_command(client: Client, message: Message):
    await message.reply_text(
        "📚 **Music Bot Help**\n\n"
        "**Basic Commands:**\n"
        "• `/play <song name>` - Play a song\n"
        "• `/play <youtube url>` - Play from URL\n"
        "• `/pause` - Pause current song\n"
        "• `/resume` - Resume playback\n"
        "• `/skip` - Skip to next song\n"
        "• `/stop` - Stop playback\n"
        "• `/queue` - Show current queue\n\n"
        "**Admin Commands:**\n"
        "• `/broadcast` - Broadcast message (Owner only)\n"
        "• `/stats` - Show bot statistics (Owner only)\n\n"
        "**Note:** Admin commands work only in groups and require admin privileges."
    )

@Client.on_message(filters.new_chat_members)
@errors
async def new_chat(client: Client, message: Message):
    for member in message.new_chat_members:
        if member.id == (await client.get_me()).id:
            await db.add_chat(message.chat.id, message.chat.title)
            await message.reply_text(
                f"👋 Thanks for adding me to **{message.chat.title}**!\n\n"
                f"Use /help to see available commands."
            )

@Client.on_message(filters.left_chat_member)
@errors
async def left_chat(client: Client, message: Message):
    if message.left_chat_member.id == (await client.get_me()).id:
        await db.remove_chat(message.chat.id)

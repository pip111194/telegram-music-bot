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
        f"I'm a Multi-Platform Music Bot that can play songs from:\n"
        f"🟢 Spotify\n"
        f"🍎 Apple Music\n"
        f"🟠 SoundCloud\n"
        f"🔵 Deezer\n"
        f"🔴 YouTube\n\n"
        f"**Quick Commands:**\n"
        f"• /play - Play from YouTube\n"
        f"• /spotify - Play from Spotify\n"
        f"• /apple - Play from Apple Music\n"
        f"• /soundcloud - Play from SoundCloud\n"
        f"• /deezer - Play from Deezer\n"
        f"• /search - Search all platforms\n"
        f"• /help - Show all commands",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")],
            [InlineKeyboardButton("📚 Help", callback_data="help_callback")]
        ])
    )

@Client.on_message(command("help"))
@errors
async def help_command(client: Client, message: Message):
    await message.reply_text(
        "📚 **Multi-Platform Music Bot Help**\n\n"
        "**🎵 Platform Commands:**\n"
        "• `/play <song>` - Play from YouTube\n"
        "• `/spotify <song>` or `/sp <song>` - Play from Spotify\n"
        "• `/apple <song>` or `/am <song>` - Play from Apple Music\n"
        "• `/soundcloud <song>` or `/sc <song>` - Play from SoundCloud\n"
        "• `/deezer <song>` or `/dz <song>` - Play from Deezer\n"
        "• `/search <song>` or `/s <song>` - Search all platforms\n\n"
        "**🎛️ Playback Controls:**\n"
        "• `/pause` - Pause current song\n"
        "• `/resume` - Resume playback\n"
        "• `/skip` - Skip to next song\n"
        "• `/stop` - Stop playback\n"
        "• `/queue` - Show current queue\n\n"
        "**📥 Download:**\n"
        "• `/song <name>` - Download song as audio file\n\n"
        "**👑 Admin Commands:**\n"
        "• `/broadcast` - Broadcast message (Owner only)\n"
        "• `/stats` - Show bot statistics (Owner only)\n\n"
        "**💡 Examples:**\n"
        "• `/spotify Kesariya` - Search Kesariya on Spotify\n"
        "• `/search Tum Hi Ho` - Search across all platforms\n"
        "• `/play https://youtube.com/...` - Play YouTube URL\n\n"
        "**🎯 Features:**\n"
        "✅ Multi-platform search\n"
        "✅ Interactive song selection\n"
        "✅ Queue management\n"
        "✅ High-quality audio\n"
        "✅ Admin controls"
    )

@Client.on_callback_query(filters.regex("help_callback"))
@errors
async def help_callback(client: Client, callback):
    await callback.message.edit_text(
        "📚 **Multi-Platform Music Bot Help**\n\n"
        "**🎵 Platform Commands:**\n"
        "• `/play <song>` - Play from YouTube\n"
        "• `/spotify <song>` - Play from Spotify\n"
        "• `/apple <song>` - Play from Apple Music\n"
        "• `/soundcloud <song>` - Play from SoundCloud\n"
        "• `/deezer <song>` - Play from Deezer\n"
        "• `/search <song>` - Search all platforms\n\n"
        "**🎛️ Playback Controls:**\n"
        "• `/pause` - Pause current song\n"
        "• `/resume` - Resume playback\n"
        "• `/skip` - Skip to next song\n"
        "• `/stop` - Stop playback\n"
        "• `/queue` - Show current queue\n\n"
        "**💡 Tip:** Use `/search` to find songs across all platforms!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="start_callback")]
        ])
    )

@Client.on_callback_query(filters.regex("start_callback"))
@errors
async def start_callback(client: Client, callback):
    await callback.message.edit_text(
        f"👋 Hello {callback.from_user.mention}!\n\n"
        f"I'm a Multi-Platform Music Bot that can play songs from:\n"
        f"🟢 Spotify\n"
        f"🍎 Apple Music\n"
        f"🟠 SoundCloud\n"
        f"🔵 Deezer\n"
        f"🔴 YouTube\n\n"
        f"**Quick Commands:**\n"
        f"• /play - Play from YouTube\n"
        f"• /spotify - Play from Spotify\n"
        f"• /search - Search all platforms\n"
        f"• /help - Show all commands",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")],
            [InlineKeyboardButton("📚 Help", callback_data="help_callback")]
        ])
    )

@Client.on_message(filters.new_chat_members)
@errors
async def new_chat(client: Client, message: Message):
    for member in message.new_chat_members:
        if member.id == (await client.get_me()).id:
            await db.add_chat(message.chat.id, message.chat.title)
            await message.reply_text(
                f"👋 Thanks for adding me to **{message.chat.title}**!\n\n"
                f"🎵 I can play music from multiple platforms:\n"
                f"🟢 Spotify • 🍎 Apple Music • 🟠 SoundCloud\n"
                f"🔵 Deezer • 🔴 YouTube\n\n"
                f"Use /help to see all commands!"
            )

@Client.on_message(filters.left_chat_member)
@errors
async def left_chat(client: Client, message: Message):
    if message.left_chat_member.id == (await client.get_me()).id:
        await db.remove_chat(message.chat.id)

@Client.on_message(command("platforms"))
@errors
async def platforms_info(client: Client, message: Message):
    """Show supported platforms"""
    await message.reply_text(
        "🎵 **Supported Music Platforms:**\n\n"
        "🟢 **Spotify**\n"
        "Command: `/spotify <song>` or `/sp <song>`\n"
        "Features: High-quality metadata, album info\n\n"
        "🍎 **Apple Music**\n"
        "Command: `/apple <song>` or `/am <song>`\n"
        "Features: iTunes catalog, preview URLs\n\n"
        "🟠 **SoundCloud**\n"
        "Command: `/soundcloud <song>` or `/sc <song>`\n"
        "Features: Independent artists, remixes\n\n"
        "🔵 **Deezer**\n"
        "Command: `/deezer <song>` or `/dz <song>`\n"
        "Features: International catalog\n\n"
        "🔴 **YouTube**\n"
        "Command: `/play <song>`\n"
        "Features: Largest catalog, direct playback\n\n"
        "💡 **Pro Tip:** Use `/search <song>` to search all platforms at once!"
    )

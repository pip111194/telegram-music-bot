from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command
from helpers.music_platforms import music_manager
from helpers.ytdl import ytdl
from helpers.call_manager import call_manager
import os

# Store platform search results
platform_results = {}

@Client.on_message(command(["spotify", "sp"]) & filters.group)
@authorized_users_only
@errors
async def spotify_search(client: Client, message: Message):
    """Search and play from Spotify"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/spotify Kesariya`")
    
    status = await message.reply_text("🟢 Searching on Spotify...")
    
    try:
        results = await music_manager.search_platform("spotify", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on Spotify!")
        
        platform_results[message.from_user.id] = {
            "platform": "spotify",
            "results": results
        }
        
        buttons = []
        for i, track in enumerate(results[:5], 1):
            title = track.get("name", "Unknown")[:35]
            artist = track.get("artists", "Unknown")[:20]
            duration = track.get("duration", "")
            buttons.append([
                InlineKeyboardButton(
                    f"{i}. {title} - {artist} ({duration})",
                    callback_data=f"platform_{message.from_user.id}_{i-1}"
                )
            ])
        
        buttons.append([InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_{message.from_user.id}")])
        
        await status.edit_text(
            f"🟢 **Spotify Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

@Client.on_message(command(["apple", "am"]) & filters.group)
@authorized_users_only
@errors
async def apple_music_search(client: Client, message: Message):
    """Search and play from Apple Music"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/apple Kesariya`")
    
    status = await message.reply_text("🍎 Searching on Apple Music...")
    
    try:
        results = await music_manager.search_platform("apple", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on Apple Music!")
        
        platform_results[message.from_user.id] = {
            "platform": "apple_music",
            "results": results
        }
        
        buttons = []
        for i, track in enumerate(results[:5], 1):
            title = track.get("name", "Unknown")[:35]
            artist = track.get("artists", "Unknown")[:20]
            duration = track.get("duration", "")
            buttons.append([
                InlineKeyboardButton(
                    f"{i}. {title} - {artist} ({duration})",
                    callback_data=f"platform_{message.from_user.id}_{i-1}"
                )
            ])
        
        buttons.append([InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_{message.from_user.id}")])
        
        await status.edit_text(
            f"🍎 **Apple Music Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

@Client.on_message(command(["soundcloud", "sc"]) & filters.group)
@authorized_users_only
@errors
async def soundcloud_search(client: Client, message: Message):
    """Search and play from SoundCloud"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/soundcloud Kesariya`")
    
    status = await message.reply_text("🟠 Searching on SoundCloud...")
    
    try:
        results = await music_manager.search_platform("soundcloud", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on SoundCloud!")
        
        platform_results[message.from_user.id] = {
            "platform": "soundcloud",
            "results": results
        }
        
        buttons = []
        for i, track in enumerate(results[:5], 1):
            title = track.get("title", "Unknown")[:35]
            artist = track.get("artist", "Unknown")[:20]
            duration = track.get("duration", "")
            buttons.append([
                InlineKeyboardButton(
                    f"{i}. {title} - {artist} ({duration})",
                    callback_data=f"platform_{message.from_user.id}_{i-1}"
                )
            ])
        
        buttons.append([InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_{message.from_user.id}")])
        
        await status.edit_text(
            f"🟠 **SoundCloud Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

@Client.on_message(command(["deezer", "dz"]) & filters.group)
@authorized_users_only
@errors
async def deezer_search(client: Client, message: Message):
    """Search and play from Deezer"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/deezer Kesariya`")
    
    status = await message.reply_text("🔵 Searching on Deezer...")
    
    try:
        results = await music_manager.search_platform("deezer", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on Deezer!")
        
        platform_results[message.from_user.id] = {
            "platform": "deezer",
            "results": results
        }
        
        buttons = []
        for i, track in enumerate(results[:5], 1):
            title = track.get("title", "Unknown")[:35]
            artist = track.get("artist", "Unknown")[:20]
            duration = track.get("duration", "")
            buttons.append([
                InlineKeyboardButton(
                    f"{i}. {title} - {artist} ({duration})",
                    callback_data=f"platform_{message.from_user.id}_{i-1}"
                )
            ])
        
        buttons.append([InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_{message.from_user.id}")])
        
        await status.edit_text(
            f"🔵 **Deezer Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

@Client.on_message(command(["search", "s"]) & filters.group)
@authorized_users_only
@errors
async def search_all_platforms(client: Client, message: Message):
    """Search across all platforms"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/search Kesariya`")
    
    status = await message.reply_text("🔍 Searching across all platforms...")
    
    try:
        results = await music_manager.search_all_platforms(query, limit=3)
        
        if not results:
            return await status.edit_text("❌ No results found on any platform!")
        
        text = f"🎵 **Search Results for:** `{query}`\n\n"
        
        for platform, tracks in results.items():
            emoji = music_manager.get_platform_emoji(platform)
            platform_name = music_manager.get_platform_name(platform)
            text += f"\n{emoji} **{platform_name}:**\n"
            
            for i, track in enumerate(tracks[:3], 1):
                if platform == "youtube":
                    title = track.get("title", "Unknown")[:40]
                    duration = track.get("duration", "")
                elif platform == "soundcloud":
                    title = track.get("title", "Unknown")[:40]
                    artist = track.get("artist", "Unknown")
                    duration = track.get("duration", "")
                    title = f"{title} - {artist}"
                elif platform == "deezer":
                    title = track.get("title", "Unknown")[:40]
                    artist = track.get("artist", "Unknown")
                    duration = track.get("duration", "")
                    title = f"{title} - {artist}"
                else:
                    title = track.get("name", "Unknown")[:40]
                    artist = track.get("artists", "Unknown")
                    duration = track.get("duration", "")
                    title = f"{title} - {artist}"
                
                text += f"{i}. {title} ({duration})\n"
        
        text += f"\n💡 Use platform-specific commands:\n"
        text += f"• `/spotify {query}` - Search Spotify\n"
        text += f"• `/apple {query}` - Search Apple Music\n"
        text += f"• `/soundcloud {query}` - Search SoundCloud\n"
        text += f"• `/deezer {query}` - Search Deezer\n"
        text += f"• `/play {query}` - Search YouTube"
        
        await status.edit_text(text)
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

@Client.on_callback_query(filters.regex(r"^platform_"))
@errors
async def platform_callback(client: Client, callback: CallbackQuery):
    """Handle platform search result selection"""
    data = callback.data.split("_")
    user_id = int(data[1])
    index = int(data[2])
    
    if callback.from_user.id != user_id:
        return await callback.answer("❌ This is not for you!", show_alert=True)
    
    if user_id not in platform_results:
        return await callback.answer("❌ Search expired! Please search again.", show_alert=True)
    
    platform_data = platform_results[user_id]
    platform = platform_data["platform"]
    track = platform_data["results"][index]
    
    await callback.message.edit_text("🔍 Finding download source...")
    
    try:
        # Get YouTube URL for download
        download_url = await music_manager.get_download_url(platform, track)
        
        if not download_url:
            return await callback.message.edit_text("❌ Could not find download source!")
        
        await callback.message.edit_text("⬇️ Downloading...")
        
        # Download from YouTube
        file_path, _ = await ytdl.download(download_url)
        
        await callback.message.edit_text("▶️ Playing...")
        await call_manager.start_call(callback.message.chat.id, file_path)
        
        # Get track info
        if platform == "youtube":
            title = track.get("title")
            artist = track.get("uploader", "Unknown")
            duration = track.get("duration", "Unknown")
        elif platform in ["soundcloud", "deezer"]:
            title = track.get("title")
            artist = track.get("artist", "Unknown")
            duration = track.get("duration", "Unknown")
        else:
            title = track.get("name")
            artist = track.get("artists", "Unknown")
            duration = track.get("duration", "Unknown")
        
        emoji = music_manager.get_platform_emoji(platform)
        platform_name = music_manager.get_platform_name(platform)
        
        await callback.message.reply_text(
            f"🎵 **Now Playing:**\n\n"
            f"**Platform:** {emoji} {platform_name}\n"
            f"**Title:** {title}\n"
            f"**Artist:** {artist}\n"
            f"**Duration:** {duration}\n"
            f"**Requested by:** {callback.from_user.mention}"
        )
        
        await callback.message.delete()
        del platform_results[user_id]
        
    except Exception as e:
        await callback.message.edit_text(f"❌ Error: {str(e)}")
        print(f"Platform callback error: {e}")

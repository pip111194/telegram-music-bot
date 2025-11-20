"""
Free Music Platform Handlers
JioSaavn, Gaana, Wynk, Jamendo, Audiomack
"""

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command
from helpers.music_platforms import music_manager
from helpers.ytdl import ytdl
from helpers.call_manager import call_manager

# Store platform search results (shared with platforms.py)
from handlers.platforms import platform_results

@Client.on_message(command(["jiosaavn", "jio", "js"]) & filters.group)
@authorized_users_only
@errors
async def jiosaavn_search(client: Client, message: Message):
    """Search and play from JioSaavn (Free!)"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/jiosaavn Kesariya`")
    
    status = await message.reply_text("🎵 Searching on JioSaavn...")
    
    try:
        results = await music_manager.search_platform("jiosaavn", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on JioSaavn!")
        
        platform_results[message.from_user.id] = {
            "platform": "jiosaavn",
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
            f"🎵 **JioSaavn Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")


@Client.on_message(command(["gaana", "gn"]) & filters.group)
@authorized_users_only
@errors
async def gaana_search(client: Client, message: Message):
    """Search and play from Gaana (Free!)"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/gaana Kesariya`")
    
    status = await message.reply_text("🎶 Searching on Gaana...")
    
    try:
        results = await music_manager.search_platform("gaana", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on Gaana!")
        
        platform_results[message.from_user.id] = {
            "platform": "gaana",
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
            f"🎶 **Gaana Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")


@Client.on_message(command(["wynk", "wk"]) & filters.group)
@authorized_users_only
@errors
async def wynk_search(client: Client, message: Message):
    """Search and play from Wynk Music (Free!)"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/wynk Kesariya`")
    
    status = await message.reply_text("🎧 Searching on Wynk Music...")
    
    try:
        results = await music_manager.search_platform("wynk", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on Wynk Music!")
        
        platform_results[message.from_user.id] = {
            "platform": "wynk",
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
            f"🎧 **Wynk Music Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")


@Client.on_message(command(["jamendo", "jm"]) & filters.group)
@authorized_users_only
@errors
async def jamendo_search(client: Client, message: Message):
    """Search and play from Jamendo (Free Creative Commons!)"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/jamendo Chill Music`")
    
    status = await message.reply_text("🎼 Searching on Jamendo...")
    
    try:
        results = await music_manager.search_platform("jamendo", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on Jamendo!")
        
        platform_results[message.from_user.id] = {
            "platform": "jamendo",
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
            f"🎼 **Jamendo Results for:** `{query}`\n\n"
            f"🆓 Free Creative Commons Music\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")


@Client.on_message(command(["audiomack", "am"]) & filters.group)
@authorized_users_only
@errors
async def audiomack_search(client: Client, message: Message):
    """Search and play from Audiomack (Free!)"""
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/audiomack Hip Hop`")
    
    status = await message.reply_text("🎤 Searching on Audiomack...")
    
    try:
        results = await music_manager.search_platform("audiomack", query, limit=5)
        if not results:
            return await status.edit_text("❌ No results found on Audiomack!")
        
        platform_results[message.from_user.id] = {
            "platform": "audiomack",
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
            f"🎤 **Audiomack Results for:** `{query}`\n\n"
            f"Select a song to play:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

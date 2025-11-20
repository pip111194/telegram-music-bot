from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command
from helpers.ytdl import ytdl
from helpers.call_manager import call_manager
import os

# Store search results temporarily
search_results = {}

@Client.on_message(command("play") & filters.group)
@authorized_users_only
@errors
async def play_song(client: Client, message: Message):
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name or YouTube URL!\n\nExample: `/play Kesariya`")
    
    status = await message.reply_text("🔍 Searching...")
    
    try:
        # Check if it's a direct URL
        if "youtube.com" in query or "youtu.be" in query:
            url = query
            info = await ytdl.get_info(url)
        else:
            # Search for the song
            results = await ytdl.search(query, limit=5)
            if not results:
                return await status.edit_text("❌ No results found! Try a different search term.")
            
            # Show search results
            search_results[message.from_user.id] = results
            
            buttons = []
            for i, result in enumerate(results[:5], 1):
                duration = result.get("duration", "Unknown")
                title = result.get("title", "Unknown")[:40]
                buttons.append([
                    InlineKeyboardButton(
                        f"{i}. {title} ({duration})",
                        callback_data=f"play_{message.from_user.id}_{i-1}"
                    )
                ])
            
            buttons.append([InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_{message.from_user.id}")])
            
            return await status.edit_text(
                f"🔍 **Search Results for:** `{query}`\n\n"
                f"Select a song to play:",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        
        # Download and play
        await status.edit_text("⬇️ Downloading...")
        file_path, _ = await ytdl.download(url)
        
        await status.edit_text("▶️ Playing...")
        await call_manager.start_call(message.chat.id, file_path)
        
        await message.reply_text(
            f"🎵 **Now Playing:**\n\n"
            f"**Title:** {info['title']}\n"
            f"**Duration:** {info['duration_str']}\n"
            f"**Uploader:** {info['uploader']}\n"
            f"**Requested by:** {message.from_user.mention}"
        )
        
        await status.delete()
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")
        print(f"Play error: {e}")

@Client.on_callback_query(filters.regex(r"^play_"))
@errors
async def play_callback(client: Client, callback: CallbackQuery):
    data = callback.data.split("_")
    user_id = int(data[1])
    index = int(data[2])
    
    if callback.from_user.id != user_id:
        return await callback.answer("❌ This is not for you!", show_alert=True)
    
    if user_id not in search_results:
        return await callback.answer("❌ Search expired! Please search again.", show_alert=True)
    
    result = search_results[user_id][index]
    url = result.get("link")
    
    await callback.message.edit_text("⬇️ Downloading...")
    
    try:
        info = await ytdl.get_info(url)
        file_path, _ = await ytdl.download(url)
        
        await callback.message.edit_text("▶️ Playing...")
        await call_manager.start_call(callback.message.chat.id, file_path)
        
        await callback.message.reply_text(
            f"🎵 **Now Playing:**\n\n"
            f"**Title:** {info['title']}\n"
            f"**Duration:** {info['duration_str']}\n"
            f"**Uploader:** {info['uploader']}\n"
            f"**Requested by:** {callback.from_user.mention}"
        )
        
        await callback.message.delete()
        del search_results[user_id]
        
    except Exception as e:
        await callback.message.edit_text(f"❌ Error: {str(e)}")
        print(f"Callback play error: {e}")

@Client.on_callback_query(filters.regex(r"^cancel_"))
@errors
async def cancel_callback(client: Client, callback: CallbackQuery):
    data = callback.data.split("_")
    user_id = int(data[1])
    
    if callback.from_user.id != user_id:
        return await callback.answer("❌ This is not for you!", show_alert=True)
    
    if user_id in search_results:
        del search_results[user_id]
    
    await callback.message.delete()
    await callback.answer("✅ Cancelled!")

@Client.on_message(command("pause") & filters.group)
@authorized_users_only
@errors
async def pause_song(client: Client, message: Message):
    await call_manager.pause_call(message.chat.id)
    await message.reply_text("⏸ Paused!")

@Client.on_message(command("resume") & filters.group)
@authorized_users_only
@errors
async def resume_song(client: Client, message: Message):
    await call_manager.resume_call(message.chat.id)
    await message.reply_text("▶️ Resumed!")

@Client.on_message(command("stop") & filters.group)
@authorized_users_only
@errors
async def stop_song(client: Client, message: Message):
    await call_manager.stop_call(message.chat.id)
    call_manager.clear_queue(message.chat.id)
    await message.reply_text("⏹ Stopped!")

@Client.on_message(command("skip") & filters.group)
@authorized_users_only
@errors
async def skip_song(client: Client, message: Message):
    queue = call_manager.get_queue(message.chat.id)
    if queue:
        next_song = queue.pop(0)
        await call_manager.start_call(message.chat.id, next_song["file_path"])
        await message.reply_text(f"⏭ Skipped! Now playing: {next_song['title']}")
    else:
        await call_manager.stop_call(message.chat.id)
        await message.reply_text("⏭ Skipped! Queue is empty.")

@Client.on_message(command("queue") & filters.group)
@errors
async def show_queue(client: Client, message: Message):
    queue = call_manager.get_queue(message.chat.id)
    if not queue:
        return await message.reply_text("📭 Queue is empty!")
    
    text = "📋 **Current Queue:**\n\n"
    for i, song in enumerate(queue, 1):
        text += f"{i}. {song['title']}\n"
    
    await message.reply_text(text)

@Client.on_message(command("song") & filters.group)
@errors
async def download_song(client: Client, message: Message):
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name!\n\nExample: `/song Kesariya`")
    
    status = await message.reply_text("🔍 Searching...")
    
    try:
        results = await ytdl.search(query, limit=1)
        if not results:
            return await status.edit_text("❌ No results found!")
        
        url = results[0]["link"]
        info = await ytdl.get_info(url)
        
        await status.edit_text("⬇️ Downloading...")
        file_path, _ = await ytdl.download(url)
        
        await status.edit_text("📤 Uploading...")
        
        await message.reply_audio(
            audio=file_path,
            title=info['title'],
            performer=info['uploader'],
            duration=info['duration'],
            thumb=info['thumbnail'] if info['thumbnail'] else None,
            caption=f"🎵 **{info['title']}**\n\n**Duration:** {info['duration_str']}\n**Uploader:** {info['uploader']}"
        )
        
        await status.delete()
        
        # Clean up
        if os.path.exists(file_path):
            os.remove(file_path)
            
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")
        print(f"Download error: {e}")

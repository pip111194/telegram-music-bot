from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command
from helpers.ytdl import ytdl
from helpers.call_manager import call_manager
import os

@Client.on_message(command("play") & filters.group)
@authorized_users_only
@errors
async def play_song(client: Client, message: Message):
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    if not query:
        return await message.reply_text("❌ Please provide a song name or YouTube URL!")
    
    status = await message.reply_text("🔍 Searching...")
    
    try:
        if "youtube.com" in query or "youtu.be" in query:
            url = query
        else:
            results = await ytdl.search(query)
            if not results:
                return await status.edit_text("❌ No results found!")
            url = results[0]["link"]
        
        info = await ytdl.get_info(url)
        await status.edit_text("⬇️ Downloading...")
        
        file_path, _ = await ytdl.download(url)
        
        await status.edit_text("▶️ Playing...")
        await call_manager.start_call(message.chat.id, file_path)
        
        await message.reply_text(
            f"🎵 **Now Playing:**\n\n"
            f"**Title:** {info['title']}\n"
            f"**Duration:** {info['duration']}s\n"
            f"**Requested by:** {message.from_user.mention}"
        )
        
        await status.delete()
        
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)}")

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

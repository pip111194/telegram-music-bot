from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped, Update
from pytgcalls.types.stream import StreamAudioEnded
from typing import Dict
import asyncio

class CallManager:
    def __init__(self):
        self.calls: Dict[int, PyTgCalls] = {}
        self.queues: Dict[int, list] = {}
    
    def get_call(self, chat_id: int) -> PyTgCalls:
        if chat_id not in self.calls:
            from bot import MusicBot
            self.calls[chat_id] = PyTgCalls(MusicBot())
        return self.calls[chat_id]
    
    async def start_call(self, chat_id: int, file_path: str):
        call = self.get_call(chat_id)
        await call.play(
            chat_id,
            AudioPiped(file_path)
        )
    
    async def stop_call(self, chat_id: int):
        if chat_id in self.calls:
            await self.calls[chat_id].leave_group_call(chat_id)
    
    async def pause_call(self, chat_id: int):
        if chat_id in self.calls:
            await self.calls[chat_id].pause_stream(chat_id)
    
    async def resume_call(self, chat_id: int):
        if chat_id in self.calls:
            await self.calls[chat_id].resume_stream(chat_id)
    
    def add_to_queue(self, chat_id: int, song_info: dict):
        if chat_id not in self.queues:
            self.queues[chat_id] = []
        self.queues[chat_id].append(song_info)
    
    def get_queue(self, chat_id: int):
        return self.queues.get(chat_id, [])
    
    def clear_queue(self, chat_id: int):
        if chat_id in self.queues:
            self.queues[chat_id] = []

call_manager = CallManager()

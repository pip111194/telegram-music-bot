from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(Config.MONGO_DB_URI)
        self.db = self.client.MusicBot
        self.chats = self.db.chats
        self.users = self.db.users
        
    async def add_chat(self, chat_id: int, chat_name: str):
        chat = await self.chats.find_one({"chat_id": chat_id})
        if not chat:
            await self.chats.insert_one({
                "chat_id": chat_id,
                "chat_name": chat_name,
                "is_active": True
            })
    
    async def remove_chat(self, chat_id: int):
        await self.chats.delete_one({"chat_id": chat_id})
    
    async def get_all_chats(self):
        chats = []
        async for chat in self.chats.find({"is_active": True}):
            chats.append(chat)
        return chats
    
    async def add_user(self, user_id: int, username: str):
        user = await self.users.find_one({"user_id": user_id})
        if not user:
            await self.users.insert_one({
                "user_id": user_id,
                "username": username
            })
    
    async def get_all_users(self):
        users = []
        async for user in self.users.find():
            users.append(user)
        return users

db = Database()

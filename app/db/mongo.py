import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.admin_dashboard
user_collection = db.users
permission_collection = db.permissions
sells_collection = db.sells_data
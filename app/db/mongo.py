import os
from dotenv import load_dotenv

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document
import inspect

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document
import importlib
import pkgutil
import app.db.models
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

def get_all_document_models():
    document_models = []
    for _, module_name, _ in pkgutil.iter_modules(app.db.models.__path__):
        module = importlib.import_module(f"app.db.models.{module_name}")
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, Document) and attr is not Document:
                document_models.append(attr)
    return document_models


async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    models = get_all_document_models()
    await init_beanie(database=client[DB_NAME], document_models=models)


import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from umongo.frameworks import MotorAsyncIOInstance
from src.settings import settings
from typing import Optional

async def startup_connect_mongodb(database_name: str):     
    MONGO_URI = f'mongodb://{settings.MONGODB_HOST}:{settings.MONGODB_PORT}/'
    client = AsyncIOMotorClient(MONGO_URI)[database_name]
    client.get_io_loop = asyncio.get_running_loop
    umongo_cnx = MotorAsyncIOInstance(client)
    return umongo_cnx


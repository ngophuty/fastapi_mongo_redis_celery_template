# -*- coding: utf-8 -*-
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from umongo.frameworks import MotorAsyncIOInstance

from src.app_settings import settings 


def startup_connect_mongodb(database_name: str):
    MONGO_URI = f"mongodb://{settings.MONGODB_USERNAME}:{settings.MONGODB_PASSWORD}@{settings.MONGODB_HOST}:{settings.MONGODB_PORT}/"
    client = AsyncIOMotorClient(MONGO_URI)[database_name]
    client.get_io_loop = asyncio.get_running_loop
    umongo_cnx = MotorAsyncIOInstance(client)
    return umongo_cnx

umongo_cnx = startup_connect_mongodb(settings.MONGODB_NAME)
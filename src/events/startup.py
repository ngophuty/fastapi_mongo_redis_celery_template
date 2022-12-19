from src.database import startup_connect_mongodb, starup_connect_redis
from src.settings import settings


async def event_01_connect_mongodb():
    await startup_connect_mongodb(settings.MONGODB_NAME)
    print(50*'-'+'connected to the mongodb'+ 50*'-')
    pass


async def event_02_connect_redis():
    await starup_connect_redis()
    print(50*'-'+'connected to the redis'+ 50*'-')
    pass


async def event_03_connect_celery():
    pass


startup_event = [v for k,v in locals().items() if k.startswith('event_')]

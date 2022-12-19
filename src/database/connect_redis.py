from redis import Redis
from src.settings import settings


async def starup_connect_redis():
    redis_db = Redis(
        host=settings.REDIS_HOST,
        port=int(settings.REDIS_PORT), 
        password=settings.REDIS_PASSWORD
        )
    return redis_db
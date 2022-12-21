from celery import Celery
from typing import Any
from src.app_settings import settings


async def setup_celery_app():
    celery_app = Celery(
        'app',
        backend=settings.CELERY_RESULT_BACKEND,
        broker= settings.CELERY_BROKER_URL
    )
    return celery_app
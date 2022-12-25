# -*- coding: utf-8 -*-
from celery import Celery
from src.app_settings import settings
from datetime import datetime
from celery.schedules import crontab

celery_app = Celery(
        "app",
        backend=settings.CELERY_RESULT_BACKEND,
        broker=settings.CELERY_BROKER_URL,
    )

@celery_app.task(name='register')
def write_log(username, email):
    with open("register.log", mode="w") as log:
            content = f"registered user account name is:{username} at{datetime.utcnow()} with {email}"
            log.write(content)
    return

@celery_app.task(name='login')
def write_log_login(username):
    with open("register.log", mode="w") as log:
            content = f"{username} just logged in at {datetime.utcnow()}"
            log.write(content)


@celery_app.task(name='wellcome')
def wellcome():
    print('well come to app')


celery_app.conf.beat_schedule = {
    'wellcome': {
        'task': 'src.celery.setup_celery.wellcome',
        'schedule': crontab()
    },
}
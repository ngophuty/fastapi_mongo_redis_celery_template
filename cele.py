from celery import Celery
from time import sleep
from celery.schedules import crontab

celery_app = Celery(
        "celery_app",
        backend='redis://:hello_exam@172.27.230.25:6026/7',
        broker='redis://:hello_exam@172.27.230.25:6026/7'
    )

@celery_app.task
def hello():
    print('well come to app')


celery_app.conf.beat_schedule = {
    'this_is': {
        'task': 'cele.hello',
        'schedule': crontab()
    },
}
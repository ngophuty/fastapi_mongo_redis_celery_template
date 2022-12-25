from celery.schedules import crontab
from.setup_celery import celery_app


celery_app.conf.beat_schedule = {
    'wellcome': {
        'task': 'src.celery.celery_tasks.wellcome',
        'schedule': crontab()
    },
}

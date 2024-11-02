import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

app = Celery('cfehome')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'populate_temperature': {
        'task': 'sensors.tasks.populate_temperature_values',
        'schedule': 5,
    }
}

app.conf.beat_schedule = CELERY_BEAT_SCHEDULE

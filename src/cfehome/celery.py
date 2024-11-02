import os

from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

app = Celery('cfehome')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Setting up individual queue and beat schedule for each node.
CELERY_TASK_QUEUES = []
CELERY_BEAT_SCHEDULE = {}

nodes = ['node-1', 'node-2']
for node in nodes:
    CELERY_TASK_QUEUES.append(Queue(node, Exchange(node), routing_key=node))
    CELERY_BEAT_SCHEDULE[f'populate_temperature_{node}'] = {
        'task': 'sensors.tasks.populate_temperature_values',
        'schedule': 5,
        'options': {
            'queue': node,
        },
    }

app.conf.task_queues = CELERY_TASK_QUEUES
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE

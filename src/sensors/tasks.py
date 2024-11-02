from celery import shared_task
from django.apps import apps
from django.utils import timezone

import helpers

from . import collect


@shared_task
def populate_temperature_values() -> None:
    """Abstract function to populate temperature values for a sensor or node."""
    metric_model = apps.get_model('sensors', 'Metric')

    time = timezone.now()
    node_id = helpers.config('NODE_ID', default=0)
    temperature = collect.generate_random_temperature_value()
    temperature = round(temperature, 4)
    metric_model.objects.create(time=time, node_id=node_id, temperature=temperature)

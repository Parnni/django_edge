from django.db import models
from timescale.db.models import models as timescale_models


class Metric(timescale_models.TimescaleModel):
    """Sensor data model."""

    node_id = models.IntegerField(default=0)
    temperature = models.FloatField()

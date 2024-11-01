from django.contrib import admin

from .models import Metric


class MetricAdmin(admin.ModelAdmin):
    """Admin view for Metric model."""

    list_display = ('node_id', 'temperature', 'time')


admin.site.register(Metric, MetricAdmin)

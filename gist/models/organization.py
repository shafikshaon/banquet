from django.db import models

from gist.models import TimeLog, Activity, Key

__author__ = 'Shafikur Rahman'


class Organization(TimeLog, Activity, Key):
    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField()

    class Meta:
        app_label = 'gist'
        db_table = 'banquet_organization'
        ordering = ['-add_at']
        verbose_name = "organization"
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.name

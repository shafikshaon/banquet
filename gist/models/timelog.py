from django.db import models

from gist.models.base import Base

__author__ = 'Shafikur Rahman'


class TimeLog(Base):
    add_at = models.DateTimeField(auto_now_add=True, editable=False)
    change_at = models.DateTimeField(auto_now=True, editable=False)
    delete_at = models.DateTimeField(null=True, blank=True, editable=False)
    active_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
    deactivate_at = models.DateTimeField(null=True, blank=True, editable=False)
    publish_at = models.DateTimeField(auto_now_add=True, editable=False)
    unpublished_at = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        abstract = True

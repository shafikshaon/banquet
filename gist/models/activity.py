from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from gist.models.base import Base

__author__ = 'Shafikur Rahman'


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Activity(Base):
    is_active = models.BooleanField(default=True, null=False, blank=False)
    is_publish = models.BooleanField(default=True, null=False, blank=False)
    is_delete = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        abstract = True

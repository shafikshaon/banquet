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
    add_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name='%(app_label)s_%(class)s_add_by',
        null=True
    )
    change_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name='%(app_label)s_%(class)s_change_by',
        null=True
    )
    delete_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name='%(app_label)s_%(class)s_delete_by',
        null=True
    )
    active_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name='%(app_label)s_%(class)s_active_by',
        null=True
    )
    deactivate_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name='%(app_label)s_%(class)s_deactivate_by',
        null=True
    )
    publish_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name='%(app_label)s_%(class)s_publish_by',
        null=True
    )

    unpublished_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name='%(app_label)s_%(class)s_unpublished_by',
        null=True
    )

    class Meta:
        abstract = True

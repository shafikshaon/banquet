from django.conf import settings
from django.db import models

from gist.models import Base
from gist.models.activity import get_sentinel_user


class Actor(Base):
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

__author__ = 'Shafikur Rahman'

from django.db import models


class GistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)

    def count_active(self):
        return super().get_queryset().filter(is_active=True)

    def count_inactive(self):
        return super().get_queryset().filter(is_active=False)

    def count_delete(self):
        return super().get_queryset().filter(is_delete=True)

    def count_non_delete(self):
        return super().get_queryset().filter(is_delete=False)

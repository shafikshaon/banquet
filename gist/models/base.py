from django.db import models

from gist.manager import GistManager

__author__ = 'Shafikur Rahman'


class Base(models.Model):
    base_objects = models.Manager()
    objects = GistManager()

    @classmethod
    def get_order_by_columns(cls):
        """
        This is used in list view ordering
        :return: list of field name
        """
        return []

    @classmethod
    def get_searchable_columns(cls):
        """
        This is used in list view searching
        :return: list of field name
        """
        return []

    class Meta:
        abstract = True

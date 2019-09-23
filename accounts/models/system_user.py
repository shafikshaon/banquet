from django.contrib.auth.models import AbstractUser
from django.db import models

from gist.models import TimeLog, Activity, Key, Organization, Actor

__author__ = 'Shafikur Rahman'


class SystemUser(AbstractUser, TimeLog, Activity, Key, Actor):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True
    )
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        app_label = 'accounts'
        db_table = 'banquet_accounts'
        ordering = ['-add_at']
        verbose_name = "account"
        verbose_name_plural = 'accounts'

    def __str__(self):
        return self.username

    @classmethod
    def page_title(cls):
        return 'User(s)'

    @classmethod
    def page_headline(cls):
        return 'User(s)'

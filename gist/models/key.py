import uuid

from django.db import models

from gist.models.base import Base
from gist.utils.generate_random_number import generate_random_number

__author__ = 'Shafikur Rahman'


class Key(Base):
    id = models.BigAutoField(primary_key=True)
    main_key = models.BigIntegerField(unique=True, default=generate_random_number, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        abstract = True

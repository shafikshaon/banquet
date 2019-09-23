from django.db import models

from gist.models import TimeLog, Activity, Key

__author__ = 'Shafikur Rahman'


class MealConfig(TimeLog, Activity, Key):
    breakfast = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
        help_text='This will consider as meal unit i.e. for breakfast if value set to 0.5 then breakfast consider as '
                  'half(0.5)'
    )

    lunch = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
        help_text='This will consider as meal unit i.e. for lunch if value set to 1 then lunch consider as half(0.5)'
    )

    dinner = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
        help_text='This will consider as meal unit i.e. for dinner if value set to 1 then dinner consider as half(0.5)'
    )

    class Meta:
        app_label = 'configuration'
        db_table = 'banquet_meal_config'
        ordering = ['-add_at']
        verbose_name = "meal_config"
        verbose_name_plural = 'meal_configs'

    def __str__(self):
        return self.code

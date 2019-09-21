from django.db import models

from accounts.models import SystemUser
from gist.models import TimeLog, Activity, Key

BREAKFAST_MEAL_COUNT = (
    (0, '0'),
    (0.5, '0.5'),
    (1, '1'),
    (1.5, '1.5'),
    (2, '2'),
    (2.5, '2.5'),
    (3, '3'),
    (3.5, '3.5'),
    (4, '4'),
    (4.5, '4.5'),
    (5, '5'),
)

LUNCH_DINNER_MEAL_COUNT = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Meal(TimeLog, Activity, Key):
    member = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    meal_date = models.DateField(blank=False, null=False)
    breakfast = models.FloatField(choices=BREAKFAST_MEAL_COUNT, default=0.5)
    lunch = models.FloatField(choices=LUNCH_DINNER_MEAL_COUNT, default=1)
    dinner = models.FloatField(choices=LUNCH_DINNER_MEAL_COUNT, default=1)

    class Meta:
        app_label = "meals"
        db_table = "banquet_meals"
        verbose_name = "meal"
        verbose_name_plural = "meals"

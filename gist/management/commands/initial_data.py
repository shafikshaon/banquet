import calendar
import datetime
import random

from django.core.management import BaseCommand

from accounts.models import SystemUser
from meals.models import Meal


def combine(date_list):
    a = []
    for i in date_list:
        if type(i) == list:
            a.extend(i)
        else:
            a.append(i)
    return a


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Data generating...\n')
        self.generate_user()
        self.generate_meal()

    @staticmethod
    def generate_user():
        core_user = SystemUser.objects.filter(username='coreuser')
        if not core_user:
            user = SystemUser(
                first_name='Core',
                last_name='User',
                username='coreuser',
                is_staff=True,
                is_superuser=True,
                email='coreuser@gmail.com'
            )
            user.set_password('1234')
            user.save()
            user_pk = str(user.pk).zfill(4)
            user.code = 'SU-{0}'.format(user_pk)
            user.save()

        first_name = ['Moriah', 'Ashlee', 'Kesha', 'Sherrie', 'Lavonna']
        last_name = ['Seguin', 'Temples', 'Feucht', 'Cash', 'Spielman']

        for i in range(5):
            fname = first_name[i]
            lname = last_name[i]
            uname = fname.lower() + lname.lower()
            email = uname + '@email.com'
            core_user = SystemUser.objects.filter(username=uname)
            if not core_user:
                user = SystemUser(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    email=email
                )
                user.set_password('1234')
                user.save()
                user_pk = str(user.pk).zfill(4)
                user.code = 'SU-{0}'.format(user_pk)
                user.save()

        print('User generated successfully.')

    @staticmethod
    def generate_meal():
        users = SystemUser.objects.all()
        for user in users:
            current_month = datetime.datetime.now().month
            current_year = datetime.datetime.now().year
            date_list = calendar.monthcalendar(current_year, current_month)

            dates = list(filter(lambda num: num != 0, combine(date_list)))

            for date in dates:
                meal = Meal(
                    member=user,
                    meal_date=datetime.date(current_year, current_month, date),
                    breakfast=random.choice([0, 0.5, 1]),
                    lunch=random.choice([0, 1, 2]),
                    dinner=random.choice([0, 1, 2]),
                )

                meal.save()
                meal_pk = str(meal.pk).zfill(4)
                meal.code = 'M-{0}'.format(meal_pk)
                meal.save()
        print('Meal generated successfully.')

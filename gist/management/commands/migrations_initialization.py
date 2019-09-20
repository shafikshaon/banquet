import os
from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand

__author__ = 'Shafikur Rahman'


class Command(BaseCommand):
    @staticmethod
    def init_file_generate(app_path, migration):
        _init_file = Path(app_path + migration + '/__init__.py')
        _init_file.touch(exist_ok=True)
        _init_file_write = open(_init_file, 'r+')
        _init_file_write.write('__author__ = "Shafikur Rahman"\n')
        _init_file_write.close()

    def handle(self, *args, **options):
        installed_custom_app = [app for app in settings.CUSTOM_APPS]

        _migration = '/migrations'
        for app in installed_custom_app:
            app_path = os.path.join(os.getcwd(), app)
            if not os.path.exists(app + _migration):
                os.makedirs(app_path + _migration)
                self.init_file_generate(app_path=app_path, migration=_migration)
            if not os.path.exists(app + _migration + '/__init__.py'):
                self.init_file_generate(app_path=app_path, migration=_migration)

        self.stdout.write(self.style.SUCCESS('Migrations initialized.'))

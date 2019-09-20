__author__ = 'Shafikur Rahman'

import datetime
import os
from pathlib import Path

from django.core.management.base import BaseCommand

_init_data = \
"""
__author__ = "Shafikur Rahman"


from .urls import *
"""

_urls_data = \
"""
__author__ = "Shafikur Rahman"
from django.urls import path


urlpatterns = [
]
"""


class Command(BaseCommand):
    help = 'Create django app'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The app name')

    def handle(self, *args, **kwargs):

        app_name = kwargs['app_name']

        if not os.path.exists(app_name):
            # created app directory
            os.makedirs(app_name)
            # created app directory path
            app_path = os.path.join(os.getcwd(), app_name)
            # make 'views', 'models', 'urls', 'migrations', 'management' folder inside app directory
            os.makedirs(app_path + '/views')
            os.makedirs(app_path + '/urls')
            os.makedirs(app_path + '/models')
            os.makedirs(app_path + '/migrations')
            os.makedirs(app_path + '/tests')
            os.makedirs(app_path + '/forms')
            os.makedirs(app_path + '/serializers')
            os.makedirs(app_path + '/managers')
            os.makedirs(app_path + '/management/commands')

            for directory in os.listdir(app_path):
                _current_directory = os.path.join('', directory)
                if _current_directory == 'urls':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _urls_file = Path(app_path + '/' + _current_directory + '/urls.py')

                    _init_file.touch(exist_ok=True)
                    _urls_file.touch(exist_ok=True)

                    _init_file_write = open(_init_file, 'r+')
                    _urls_file_write = open(_urls_file, 'r+')

                    _init_file_write.write(_init_data)
                    _urls_file_write.write(_urls_data)

                    _init_file_write.close()
                    _urls_file_write.close()
                if _current_directory == 'views':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()
                if _current_directory == 'models':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()
                if _current_directory == 'tests':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()
                if _current_directory == 'migrations':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()
                if _current_directory == 'forms':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()
                if _current_directory == 'serializers':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()
                if _current_directory == 'managers':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()
                if _current_directory == 'management':
                    _init_file = Path(app_path + '/' + _current_directory + '/__init__.py')
                    _init_file.touch(exist_ok=True)
                    _init_file_write = open(_init_file, 'r+')
                    _init_file_write.write('__author__ = "Shafikur Rahman"\n')
                    _init_file_write.close()

                # generate app label init file
                _app_label_init_file = Path(app_path + '/__init__.py')
                _app_label_init_file.touch(exist_ok=True)
                _app_label_init_file = open(_app_label_init_file, 'r+')
                _app_label_init_file.write("""
# Generated on: {0}
__author__ = "Shafikur Rahman"\n""".format(datetime.datetime.now().strftime('%d/%m/%Y %H:%m'))
                                           )
                _app_label_init_file.close()

                # generate app label urls.py
                _app_label_admin_file = Path(app_path + '/urls.py')
                _app_label_admin_file.touch(exist_ok=True)
                _app_label_admin_file = open(_app_label_admin_file, 'r+')
                _app_label_admin_file.write('__author__ = "Shafikur Rahman"\n')
                _app_label_admin_file.close()

                # generate app label enum.py
                _app_label_enum_file = Path(app_path + '/enum.py')
                _app_label_enum_file.touch(exist_ok=True)
                _app_label_enum_file = open(_app_label_enum_file, 'r+')
                _app_label_enum_file.write('__author__ = "Shafikur Rahman"\n')
                _app_label_enum_file.close()

                # generate app label apps.py
                if app_name.__contains__('_'):
                    separated_app_name = app_name.split('_')
                    app_name = [word.capitalize() for word in separated_app_name]
                else:
                    app_name = app_name[0].upper() + app_name[1:]
                _app_label_apps_file = Path(app_path + '/apps.py')
                _app_label_apps_file.touch(exist_ok=True)
                _app_label_apps_file = open(_app_label_apps_file, 'r+')
                _app_label_apps_file.write(
                    """
__author__ = "Shafikur Rahman"
from django.apps import AppConfig


class %sConfig(AppConfig):
    name = '%s'\n""" % (app_name, app_name.lower())
                )
                _app_label_apps_file.close()

            self.stdout.write(self.style.SUCCESS('App created successfully.'))

        else:
            self.stdout.write(self.style.ERROR('App already added with this name.'))

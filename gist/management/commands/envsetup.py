__author__ = 'Shafikur Rahman'
import os
import sys

import django
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


def is_env_exits():
    if os.path.exists('.env'):
        return True
    return False


def make_env_file(self=None):
    sys.stdout.write(self.style.SUCCESS('Creating new .env file.\n'))
    open('.env', 'w+')


def set_postgres_data_conf(self):
    database_name = str(input(self.style.SUCCESS("Database name? (default: 'db'): ")))
    database_user_name = str(input(self.style.SUCCESS("Database username? (default: 'postgres'): ")))
    database_host = str(input(self.style.SUCCESS("Database host? (default: 'localhost'): ")))
    database_port = str(input(self.style.SUCCESS("Database port? (default: '5432'): ")))
    database_password = str(input(self.style.SUCCESS("Database password? (default: 'postgres'): ")))

    database_engine = 'django.db.backends.postgresql_psycopg2'
    if not database_name:
        database_name = 'db'
    if not database_user_name:
        database_user_name = 'postgres'
    if not database_host:
        database_host = 'localhost'
    if not database_port:
        database_port = '5432'
    if not database_password:
        database_password = 'postgres'

    return {
        "DB_ENGINE": database_engine,
        "DB_NAME": database_name,
        "DB_USER": database_user_name,
        "DB_HOST": database_host,
        "DB_PORT": database_port,
        "DB_PASSWORD": database_password
    }


def set_mysql_data_conf(self):
    database_name = str(input(self.style.SUCCESS("Database name? (default: 'db'): ")))
    database_user_name = str(input(self.style.SUCCESS("Database username? (default: 'root'): ")))
    database_host = str(input(self.style.SUCCESS("Database host? (default: 'localhost'): ")))
    database_port = str(input(self.style.SUCCESS("Database port? (default: '3306'): ")))
    database_password = str(input(self.style.SUCCESS("Database password? (default: 'root'): ")))

    database_engine = 'django.db.backends.mysql'
    if not database_name:
        database_name = 'db'
    if not database_user_name:
        database_user_name = 'root'
    if not database_host:
        database_host = 'localhost'
    if not database_port:
        database_port = '3306'
    if not database_password:
        database_password = 'root'

    return {
        "DB_ENGINE": database_engine,
        "DB_NAME": database_name,
        "DB_USER": database_user_name,
        "DB_HOST": database_host,
        "DB_PORT": database_port,
        "DB_PASSWORD": database_password
    }


def set_oracle_data_conf(self):
    database_name = str(input(self.style.SUCCESS("Database name? (default: 'db'): ")))
    database_user_name = str(input(self.style.SUCCESS("Database username? (default: 'general'): ")))
    database_host = str(input(self.style.SUCCESS("Database host? (default: '127.0.0.1'): ")))
    database_port = str(input(self.style.SUCCESS("Database port? (default: '1521'): ")))
    database_password = str(input(self.style.SUCCESS("Database password? (default: 'oracle'): ")))

    database_engine = 'django.db.backends.oracle'
    if not database_name:
        database_name = 'db'
    if not database_user_name:
        database_user_name = 'general'
    if not database_host:
        database_host = '127.0.0.1'
    if not database_port:
        database_port = '1521'
    if not database_password:
        database_password = 'oracle'

    return {
        "DB_ENGINE": database_engine,
        "DB_NAME": database_name,
        "DB_USER": database_user_name,
        "DB_HOST": database_host,
        "DB_PORT": database_port,
        "DB_PASSWORD": database_password
    }


def set_database_conf(self):
    preferred_database = input(self.style.NOTICE(
        "Preferred database? "
        + "\n"
        + "1. PostgreSQL"
        + "\n"
        + "2. MySQL"
        + "\n"
        + "3. Oracle"
        + "\n"
        + "4. SQLite"
        + "\n"
    ))

    try:
        preferred_database = int(preferred_database)
    except:
        preferred_database = 0

    if preferred_database == 1:
        return set_postgres_data_conf(self)
    elif preferred_database == 2:
        return set_mysql_data_conf(self)
    elif preferred_database == 3:
        return set_oracle_data_conf(self)
    else:
        str(input(self.style.ERROR("Wrong choice! Please run 'python manage.py setup' again.")))


def set_basic_conf(self):
    secret_key = get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
    time_zone = str(input(self.style.SUCCESS("Timezone? (default: 'UTC'): ")))
    debug = str(input(self.style.SUCCESS("Debug? (default: 'True'): ")))
    is_development = str(input(self.style.SUCCESS("Is development? (default: 'True'): ")))

    if not time_zone:
        time_zone = 'UTC'
    if not debug:
        debug = True
    if not is_development:
        is_development = True

    return {
        "SECRET_KEY": secret_key,
        "TIME_ZONE": time_zone,
        "DEBUG": debug,
        "IS_DEVELOPMENT": is_development
    }


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Python %s on %s' % (sys.version, sys.platform)))
        self.stdout.write(self.style.NOTICE('Django version: %s \n' % django.get_version()))

        if is_env_exits():
            self.stdout.write(self.style.WARNING('Remove existing .env file.'))
            os.remove('.env')
            make_env_file(self)
        else:
            make_env_file(self)

        final_conf = {}
        basic_conf = set_basic_conf(self)
        database_conf = set_database_conf(self)

        if database_conf is None:
            return

        final_conf.update(basic_conf)
        final_conf.update(database_conf)

        env_text = ''
        for key, value in final_conf.items():
            env_text += str(key)
            env_text += '='
            env_text += str(value) + '\n'

        with open('.env', 'w') as file:
            file.write(env_text)
            file.close()

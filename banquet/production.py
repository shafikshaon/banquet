from .config import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_cool_paginator'
]

INSTALLED_APPS += THIRD_PARTY_APPS

INTERNAL_IPS = ['127.0.0.1', 'localhost']

# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
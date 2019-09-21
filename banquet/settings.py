import os

from decouple import config
from django.contrib import messages

if config('IS_DEVELOPMENT'):
    from .development import *
else:
    from .production import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ROOT_URLCONF = 'banquet.urls'

WSGI_APPLICATION = 'banquet.wsgi.application'

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

AUTH_USER_MODEL = 'accounts.SystemUser'

APPEND_SLASH = True

# built-in Message framework
MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

AUTHENTICATION_BACKENDS = (
    'accounts.authentication.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

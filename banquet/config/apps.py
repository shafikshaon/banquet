# Applications

DJANGO_DEFAULT_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'gist',
    'accounts',
    'meals',
    'configuration',
]

SITE_ID = 1

INSTALLED_APPS = DJANGO_DEFAULT_APPS + CUSTOM_APPS

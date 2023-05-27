from core.settings.base import *

SECRET_KEY = 'django-insecure-!j#6ecz2j+2q1&o@#+x+m$48!x8^ztapaq0m+a!l#a+j#1snu0'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOW_ALL_ORIGINS = True

from .common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "smant",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    },
}

ALLOWED_HOSTS = ['www.sangmoonpark.com', 'sangmoonpark.com']

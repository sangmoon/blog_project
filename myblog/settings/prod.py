from .common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "mac",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    },
}

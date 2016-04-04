from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# Running on production App Engine, so use a Google Cloud SQL database.
# This does not work
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'soamgrdb',
        'USER': 'root',
        'PASSWORD': 'dummypa%%',
        'HOST': '/cloudsql/soa-manager-dgv:soa-manager',  # This is an SQL First Generation instance; the IPv4 costs $0.01/hour
    }
}

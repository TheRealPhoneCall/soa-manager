from .base import *


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# Parse database configuration from $DATABASE_URL (12factor)
import dj_database_url
DATABASES = {'default': dj_database_url.config()}


# Do this only on development
INSTALLED_APPS += [
    'django_extensions',  # django_extensions, to get shell_plus
]

from .base import *


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# Parse database configuration from $DATABASE_URL (12factor)
import dj_database_url
DATABASES = {'default': dj_database_url.config()}


# See here: https://devcenter.heroku.com/articles/getting-started-with-django#django-settings

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

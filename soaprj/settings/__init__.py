import logging
import os


logger = logging.getLogger(__name__)

DEPLOY_ENV = os.environ.get('DEPLOY_ENV', 'gae')
logger.info('Running on %s environment', DEPLOY_ENV)

if DEPLOY_ENV == 'local':
    from .local import *
elif DEPLOY_ENV == 'heroku':
    from .heroku import *
elif DEPLOY_ENV == 'gae':
    from .gae import *
else:
    raise ValueError('Please setup the DEPLOY_ENV environment variable. Current value is %s. Allowed are: local, heroku or gae' % (DEPLOY_ENV,))

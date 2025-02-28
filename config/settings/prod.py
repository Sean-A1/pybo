import environ
from .base import *

ALLOWED_HOSTS = ['43.201.231.69', 'tukcappybo.xyz']
STATIC_ROOT = BASE_DIR / 'pybo/static/'
STATICFILES_DIRS = []
DEBUG = False

# django.contrib.sites 사용을 위한 Site ID
# local 은 1, Operating Environment는 2
SITE_ID = 2

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}
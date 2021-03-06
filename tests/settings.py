import os

import environ

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': env.db(default='sqlite:///django-freeradius.db'),
}

SECRET_KEY = 'fn)t*+$)ugeyip6-#txyy$5wf2ervc0d2n#h)qb)y5@ly$t*@w'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_freeradius',
    'rest_framework'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TIME_ZONE = 'Europe/Rome'
LANGUAGE_CODE = 'en-gb'
USE_TZ = True
USE_I18N = False
USE_L10N = False
STATIC_URL = '/static/'
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

if os.environ.get('SAMPLE_APP', False):
    INSTALLED_APPS.append('sample_radius')
    DJANGO_FREERADIUS_RADIUSREPLY_MODEL = "sample_radius.RadiusReply"
    DJANGO_FREERADIUS_RADIUSGROUPREPLY_MODEL = "sample_radius.RadiusGroupReply"
    DJANGO_FREERADIUS_RADIUSCHECK_MODEL = "sample_radius.RadiusCheck"
    DJANGO_FREERADIUS_RADIUSGROUPCHECK_MODEL = "sample_radius.RadiusGroupCheck"
    DJANGO_FREERADIUS_RADIUSACCOUNTING_MODEL = "sample_radius.RadiusAccounting"
    DJANGO_FREERADIUS_NAS_MODEL = "sample_radius.Nas"
    DJANGO_FREERADIUS_RADIUSGROUPUSERS_MODEL = "sample_radius.RadiusGroupUsers"
    DJANGO_FREERADIUS_RADIUSUSERGROUP_MODEL = "sample_radius.RadiusUserGroup"
    DJANGO_FREERADIUS_RADIUSPOSTAUTH_MODEL = "sample_radius.RadiusPostAuth"
    DJANGO_FREERADIUS_RADIUSGROUP_MODEL = "sample_radius.RadiusGroup"

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from local_settings import *
except ImportError:
    pass

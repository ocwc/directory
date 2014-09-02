# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    ('Jure Cuhalev', 'jure@oeconsortium.org'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['www.oeconsortium.org']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'loginurl',
    'crispy_forms',
    'haystack',
    'email_obfuscator',

    'directory',
    'web',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'loginurl.backends.LoginUrlBackend',    
)

ROOT_URLCONF = 'directory.urls'
WSGI_APPLICATION = 'directory.wsgi.application'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/directory/edit/'
LOGIN_URL = '/directory/login/'

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 100

CRISPY_TEMPLATE_PACK = 'bootstrap3'

from .localsettings import *
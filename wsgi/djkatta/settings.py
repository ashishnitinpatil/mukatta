"""
Django settings for djkatta project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import urlparse
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%fkgg9)ca_tj+5ma&y4_0=4(vz20bwtv7-1jf_9_!9(%6rk35p' # Na, don't!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'mukatta-anp.rhcloud.com',
]

APPEND_SLASH = True

LOGIN_URL          = '/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_URL         = '/user/logout/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'djkatta.apkatta',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djkatta.urls'

WSGI_APPLICATION = 'djkatta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
 
DATABASES = {}
if 'OPENSHIFT_MYSQL_DB_URL' in os.environ:
    url = urlparse.urlparse(os.environ.get('OPENSHIFT_MYSQL_DB_URL'))
 
    DATABASES['default'] = {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
else:
    DATABASES['default'] = {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME': 'mukatta',
        'USER': 'mukatta',
        'PASSWORD': 'mukatta',
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

# Use Django-nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# Tell nose to measure coverage on only the mentioned apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-html-dir=coverage',
    '--cover-package=MkrSqr.accounts,MkrSqr.mkrsqr',
]
# Tests are much faster since django uses in-memory database
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

# Needed for django admin accounts
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Admin Settings
SERVER_EMAIL = 'mu.katta.anp@gmail.com'
EMAIL_SUBJECT_PREFIX = "[MuKatta Admin] "
ADMINS = (
("Ashish Patil", "ashishnitinpatil@gmail.com"),
)
MANAGERS = (
("Ashish Patil", "ashishnitinpatil@gmail.com"),
)
SEND_BROKEN_LINK_EMAILS = True
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mu.katta.anp@gmail.com'
EMAIL_HOST_PASSWORD = 'MuKatta.ANP' # Don't worry, this ain't the password
DEFAULT_FROM_EMAIL = 'mu.katta.anp@gmail.com'

# All secure (secrets, passwords, etc.) information goes into this file
# For security purposes, this file won't be found under the public git repo
import secrets

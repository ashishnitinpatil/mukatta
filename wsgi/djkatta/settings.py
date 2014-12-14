"""
Django settings for djkatta project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import urlparse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'mukatta-anp.rhcloud.com',
    '192.168.1.234', # local dev
]

APPEND_SLASH = True

LOGIN_URL          = '/user/login/'
LOGIN_REDIRECT_URL = '/cabshare/'
LOGOUT_URL         = '/user/logout/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'coverage',
    # 'django_nose',
    'bootstrap3',
    'djkatta.accounts',
    'djkatta.roomreq',
    'djkatta.cabshare',
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

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static_temp')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

# Use Django-nose to run all tests
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# Tell nose to measure coverage on only the mentioned apps
# NOSE_ARGS = [
    # '--with-coverage',
    # '--cover-erase',
    # '--cover-html',
    # '--cover-html-dir=coverage',
    # '--cover-package=djkatta.accounts',
# ]
# Tests are much faster since django uses in-memory database
# if 'test' in sys.argv:
    # DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

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

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
    # 'version': 1,
    # 'disable_existing_loggers': False,
    # 'handlers': {
        # 'mail_admins': {
            # 'level': 'ERROR',
            # 'class': 'django.utils.log.AdminEmailHandler'
        # }
    # },
    # 'loggers': {
        # 'django.request': {
            # 'handlers': ['mail_admins'],
            # 'level': 'ERROR',
            # 'propagate': True,
        # },
    # }
# }

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mu.katta.anp@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'mu.katta.anp@gmail.com'
# For development purposes (disable in production)
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# django Bootstrap3 settings
BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    # 'jquery_url': '//code.jquery.com/jquery.min.js',
    'jquery_url': '/static/jquery.min.js',

    # The Bootstrap base URL
    # 'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.2.0/',
    'base_url': '/static/bootstrap/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # Field class to use in horiozntal forms
    'horizontal_field_class': 'col-md-4',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}

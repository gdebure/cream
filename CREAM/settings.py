"""
Django settings for CREAM project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""



# import instance specific settings
# 1. create a file named instance_settings.py in the CREAM/CREAM folder
# 2. in this instance_settings.py file, set the correct value for each of the variables imported below
from instance_settings import DATABASES # Refer to https://docs.djangoproject.com/en/1.7/ref/settings/#databases
from instance_settings import TIME_ZONE # Refer to https://docs.djangoproject.com/en/1.7/ref/settings/#time-zone
from instance_settings import STATIC_ROOT # Refer to https://docs.djangoproject.com/en/1.7/ref/settings/#static-root
from instance_settings import EMAIL_HOST, EMAIL_PORT, EMAIL_SUBJECT_PREFIX # Refer to https://docs.djangoproject.com/en/1.7/topics/email/
from instance_settings import CURRENCY_SYMBOL, THOUSAND_SEPARATOR, DECIMAL_SEPARATOR # Set the currency symbol and separators



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6wlv-@ndmb-0x$jlt5y7p1feluvlk3pf77#8pou1fg+eum23=('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Use django-bower for managing required addons
    'djangobower',
    # Use django_nvd3 for displaying charts
    'django_nvd3',
    # Use django comments
    'django_comments',
    # Use guardian for per-object permissions
    'guardian',
    # Use reversion for data versioning
    'reversion',
    
    'core',
    'mailer',
    'users',
    'projects',
    'services',
    'qualifications',
    'reports',
    
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # We need this for reversion
    'django.middleware.transaction.TransactionMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

ROOT_URLCONF = 'CREAM.urls'

WSGI_APPLICATION = 'CREAM.wsgi.application'


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_FINDER = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    )

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap',
    'bootstrap-datepicker',
    'datatables',
    'd3',
    'fontawesome',
    'nvd3',
    'respond',
)

# Define additional information for users in the Employee model
AUTH_PROFILE_MODULE = 'users.Employee'

LOGIN_URL="/users/login/"
LOGIN_REDIRECT_URL="/"

# Guardian Backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

# Also needed for guardian
ANONYMOUS_USER_ID = -1

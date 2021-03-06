# -*- coding: utf-8 -*-



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.10/ref/settings/#secret-key
SECRET_KEY = 'Som35uper$ecretKey'



# Set your database settings here. Please refer to 
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# for details
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'some.host.name.or.ip',
        'NAME': 'cream_django',
        'USER': 'cream',
        'PASSWORD': 'Cr3amI$Gr8t',
     }
}


    
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'


# The absolute path to the directory where collectstatic will collect 
# static files for deployment. Please refer to 
# https://docs.djangoproject.com/en/1.10/ref/settings/#static-root
# for details
STATIC_ROOT = '/server/cream/static'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/server/cream/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/server/cream/media/'

# Email settings. Please refer to 
# https://docs.djangoproject.com/en/1.10/topics/email/
# for details
EMAIL_HOST = 'your.smtp.hostname.or.ip'
EMAIL_PORT= 5225
EMAIL_SUBJECT_PREFIX = '[CREAM]'



# Currency settings. If your currency symbol in non ascii, 
# remember to add an encoding statement at the beginning of this file
CURRENCY_SYMBOL = u"\u20AC" # This is the utf-8 code for the euro symbol
THOUSAND_SEPARATOR = ','
DECIMAL_SEPARATOR = '.'


# URL to user pictures will be built as an aggregation of
# user_picture_base_url, user.id, and user_picture_file_extension
USER_PICTURE_BASE_URL = 'http://base.url.to.user.picture'
USER_PICTURE_FILE_EXTENSION = '.jpg'
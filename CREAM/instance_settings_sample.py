# -*- coding: utf-8 -*-


# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.7/ref/settings/#secret-key
SECRET_KEY = 'Ee7vGi-ING6n02gkcJ-QLHg6vFw'


# Set your database settings here. Please refer to 
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
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
# https://docs.djangoproject.com/en/1.7/ref/settings/#static-root
# for details
STATIC_ROOT = '/server/cream/static'



# Email settings. Please refer to 
# https://docs.djangoproject.com/en/1.7/topics/email/
# for details
EMAIL_HOST = 'your.smtp.hostname.or.ip'
EMAIL_PORT= 5225
EMAIL_SUBJECT_PREFIX = '[CREAM]'



# Currency settings. If your currency symbol in non ascii, 
# remember to add an encoding statement at the beginning of this file
CURRENCY_SYMBOL = u"\u20AC" # This is the utf-8 code for the € symbol
THOUSAND_SEPARATOR = ','
DECIMAL_SEPARATOR = '.'
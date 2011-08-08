import os
import sys

sys.path.append('E:/Devel')
sys.path.append('E:/Devel/cream')

os.environ['DJANGO_SETTINGS_MODULE'] = 'cream.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
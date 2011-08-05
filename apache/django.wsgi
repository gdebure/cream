import os
import sys

path = 'E:/Devel/cream'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'cream.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
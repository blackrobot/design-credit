import os
import sys
import site

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['PYTHON_EGG_CACHE'] = '/var/www/django/.python-eggs'

sys.path.append('/var/www/django/src')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import os
import sys

sys.path = ['/home/spectrum/webapps/cycleworks', '/home/spectrum/webapps/cycleworks/lib/python2.5'] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
application = WSGIHandler()

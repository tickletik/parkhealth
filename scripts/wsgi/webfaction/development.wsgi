import os
import sys

sys.path = ['/home/parkadmin/webapps/django_development', '/home/parkadmin/webapps/django_development/lib/python2.5', '/home/parkadmin/webapps/django_development/lib/apps'] + sys.path

from django.core.handlers.wsgi import WSGIHandler


os.environ['DJANGO_SETTINGS_MODULE'] = 'parkhealth.settings'
application = WSGIHandler()

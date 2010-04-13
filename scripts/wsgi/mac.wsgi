import os
import sys
import django.core.handlers.wsgi

sys.path += ['/Users/ronny/Sites', '/opt/projects/django/parkhealth.git/apps', '/opt/projects/django/apps']
os.environ['DJANGO_SETTINGS_MODULE'] = 'parkhealth.settings'
application = django.core.handlers.wsgi.WSGIHandler()


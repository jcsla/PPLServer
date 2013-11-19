import os
import sys

sys.path.append('/home/crispin/ppl_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ppl_project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

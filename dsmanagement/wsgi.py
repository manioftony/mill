"""
WSGI config for dsmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dsmanagement.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

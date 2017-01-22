"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from decouple import config
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


if config('DEBUG', default=False, cast=bool):
    # Use Cling and staticfiles when DEBUG is true
    application = Cling(get_wsgi_application())
else:
    # Use git cdn when DEBUG is false
    application = get_wsgi_application()

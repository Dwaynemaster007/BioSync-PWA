"""ASGI config for the BioSync project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biosync.settings')

application = get_asgi_application()

"""
ASGI config for chat_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django

# Set Django settings and initialize Django before importing other components
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')
django.setup()

# Import other components after Django is set up
from django.core.asgi import get_asgi_application

# Create the ASGI application
application = get_asgi_application()

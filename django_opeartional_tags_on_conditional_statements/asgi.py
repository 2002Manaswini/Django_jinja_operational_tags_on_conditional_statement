"""
ASGI config for django_opeartional_tags_on_conditional_statements project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_opeartional_tags_on_conditional_statements.settings')

application = get_asgi_application()

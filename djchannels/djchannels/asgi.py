"""
WSGI config for djchannels project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.conf.urls import url
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chats.consumer import ChatConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djchannels.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"rooms/(?P<room_name>[\d+])/$", ChatConsumer.as_asgi())
                ]
            )
        )
    )
})
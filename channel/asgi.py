"""
ASGI config for channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import directmessage.routing
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel.settings')

application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            directmessage.routing.websocket_urlpatterns
        )
    ),
})

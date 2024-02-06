# your_app/routing.py

from django.urls import path
from .consumers import WebcamConsumer

from channels.routing import ProtocolTypeRouter, URLRouter
application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/webcam/", WebcamConsumer.as_asgi()),
    ]),
})

# websocket_urlpatterns = [
#     path("ws/webcam/", WebcamConsumer.as_asgi()),
# ]


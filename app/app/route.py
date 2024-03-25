import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app.chat.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application

# channels 라이브러리를 활용해서 Socket 연결하는 비동기 라우트 구현
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)  # ws://127.0.0.1:8000/ws/room
        ),
    }
)

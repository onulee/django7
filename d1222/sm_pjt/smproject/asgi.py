"""
ASGI config for smproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter 
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smproject.settings')

# 기존 WSGI → HTTP만 처리
# ASGI → HTTP + WebSocket + 기타 비동기 프로토콜 처리 가능
# 비동기 통신
application = ProtocolTypeRouter ({ 
    'http':get_asgi_application()
})

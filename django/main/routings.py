from django.urls import re_path
from notifications.consumers import AdminDashboardConsumer

websocket_urlpatterns = [
    re_path(r'ws/admin/dashboard/$', AdminDashboardConsumer.as_asgi()),
]

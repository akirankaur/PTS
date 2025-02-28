import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AdminDashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("admin_dashboard", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("admin_dashboard", self.channel_name)

    async def send_update(self, event):
        await self.send(text_data=json.dumps({"visitor_count": event["count"]}))

# Core
from django.contrib.auth import get_user_model

# Channels
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

# models
from .models import Messages, Room

# Utils/Heplers
import asyncio
import json
import datetime


class ChatConsumer(AsyncConsumer):
    """
        Consumers: https://channels.readthedocs.io/en/stable/topics/consumers.html#consumers
    """

    async def websocket_connect(self, event):
        """Executed when application tries to connect over the socket"""
        print("Connected", event)
        await self.send({
            "type": "websocket.accept",
        })
    
    async def websocket_receive(self, event):
        """Executed when a message is received from websocket"""
        print("Connected", event)
        form_text = event.get("text", None)

        if form_text:
            payload = json.loads(form_text)
            payload['time'] = str("12:20 AM")
            await self.send({
                "type": "websocket.send",
                "text": json.dumps(payload)
            })

    async def websocket_disconnect(self, event):
        """Executed when the socket disconnects"""
        print("Connected", event)
        await self.send({
            "type": "websocket.disconnect",
        })        
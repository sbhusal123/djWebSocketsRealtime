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

        # get room_id from url
        self.room_id = str(self.scope['url_route']['kwargs']['room_name'])

        # Add room id to the channel name
        await self.channel_layer.group_add(
            self.room_id,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept",
        })

        
    
    async def websocket_receive(self, event):
        """Executed when a message is received from websocket"""
        print("Received", event)
        form_text = event.get("text", None)

        if form_text:
            payload = json.loads(form_text)
            # Save Message on db
            new_message = await self.create_chat_message(payload['text'])
            payload['time'] = str(new_message.time.strftime('%b %d, %Y, %I:%M %P.'))

            # Event to be broad_casted accross channels. 
            newEvent = {
                "type": "chat_message", # handler, get's executed for every observer in channel
                "text": json.dumps(payload)
            }
            await self.channel_layer.group_send(
                self.room_id, # broadcasting queue
                newEvent
            )
            

    async def websocket_disconnect(self, event):
        """Executed when the socket disconnects"""
        await self.channel_layer.group_discard(
            self.room_id,
            self.channel_name
        )
        await self.send({
            "type": "websocket.disconnect",
        })

    async def chat_message(self, event):
        """Broad case handler. Don't do db write operations here. Gets executed for each connected sockets"""
        message = json.loads(event['text'])

        if(message['text'] != ""):
            # Send message to WebSocket
            await self.send({
                "type": "websocket.send",
                "text": json.dumps(message)
            })
    
    @database_sync_to_async
    def create_chat_message(self, msg):
        room_obj = Room.objects.get(id=self.room_id)
        user = self.scope['user']
        return Messages.objects.create(room=room_obj, user=user, message=msg)
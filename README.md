## Live Chat Messagging with Django Websockets

- Python Version: ``3.8.10``

## Architecture of Event Driven WebSocket based Application:

![Arch](https://miro.medium.com/max/1400/1*OjBd7k7l1LZ0dmpScoJbew.png)

## Prerequisite:

-   [Basics of WebSockets with Javascript](https://javascript.info/websocket)
-   [Django Channels](https://channels.readthedocs.io/en/stable/)

## Runing An Application:

This is a minimalistic chat application built with redis, django channels.

When a docker services are composed up, it create a two separate user with following credentials:

```sh
web-backend   | User1 Credentials
------------------------------------------------------------------------------------------------------------------------------------------------------
web-backend   | {'username': 'user1', 'email': 'user1@gmail.com', 'password': 'thepassword', 'is_staff': True, 'is_superuser': True}------------------------------------------------------------------------------------------------------------------------------------------------------


web-backend   | User2 Credentials
------------------------------------------------------------------------------------------------------------------------------------------------------
web-backend   | {'username': 'user2', 'email': 'user2@gmail.com', 'password': 'thepassword', 'is_staff': True, 'is_superuser': True}
------------------------------------------------------------------------------------------------------------------------------------------------------
```

Basically, user is logged in through the admin panel, as they are both a superuser. So, users are authenticated through django admin panel at:

```sh
http://localhost:8000/admin
```

To open up a chat window, navigate to:

```sh
http://localhost:8000/rooms/1
```

1 here is the room id and is associated with the two user groups on chat channel.


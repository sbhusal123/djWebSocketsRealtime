## Live Chat Messagging with Django Websockets

**Architecture of Event Driven WebSocket based Application**
![Arch](https://heroku-blog-files.s3.amazonaws.com/posts/1473343845-django-wsgi.png)

**Prerequisite**
[Basics of WebSockets with Javascript](https://javascript.info/websocket)
[Django Channels](https://channels.readthedocs.io/en/stable/)

**Spin up redis server:** `docker run -d --name <name> -p 6379:6379 redis`
**Execute inside redis container:** `docker exec -it <name> bash`

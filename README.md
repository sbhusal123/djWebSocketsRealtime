## Live Chat Messagging with Django Websockets

- Python Version: ``3.8.10``

**Architecture of Event Driven WebSocket based Application:**

![Arch](https://miro.medium.com/max/1400/1*OjBd7k7l1LZ0dmpScoJbew.png)

**Prerequisite:**

-   [Basics of WebSockets with Javascript](https://javascript.info/websocket)
-   [Django Channels](https://channels.readthedocs.io/en/stable/)

**Setting up application:**
-   **Create and activate venv:** `python3 -m venv env && source env/bin/activate`
-   **Install dep:** `pip install -r requirements.txt`
-   **Spin up redis server:** `docker run -d --name <name> -p 6379:6379 redis`
-   **Migrate:** `python manage.py migrate`
-   **Run server:** `python manage.py runserver`

**Redis commands**

-   **Execute inside redis container:** `docker exec -it <name> bash`

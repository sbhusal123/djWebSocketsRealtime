FROM python:3.8.10-slim-buster

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y \
    gcc libc-dev libffi-dev libssl-dev

RUN pip install -r requirements.txt


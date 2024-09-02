#!/bin/sh

cd djchannels && 
python manage.py migrate &&
python manage.py create_user_and_rooms &&
python manage.py runserver 0.0.0.0:8000

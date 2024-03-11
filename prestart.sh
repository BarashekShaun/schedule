#!/usr/bin/env bash

echo "Run migrations"
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

echo "Run app"
python -m uvicorn schedule.asgi:application --host 0.0.0.0 --port 8000


FROM python:3.9-alpine AS base
copy . /app
workdir /app
run pip install -r requirements.txt
expose $port
cmd gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app


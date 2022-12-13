FROM python:3.7
COPY ./app
workdir /app
run pip install -r requirements.txt
expose $port
cmd gunicorn --workers --bind 0.0.0.0:$port app:app
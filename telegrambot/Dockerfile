FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN apt-get update -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD sh -c 'gunicorn app.wsgi:application --bind 0.0.0.0:8000'
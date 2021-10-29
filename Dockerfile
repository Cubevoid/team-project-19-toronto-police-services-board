# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8000

# TODO: set up proper production webserver and set DEBUG to False
ENV DEBUG "True"

ENV BACKEND_URL "0.0.0.0:$PORT"
ENV FRONTEND_URL "localhost:3000"
ENV SECRET_KEY = "django-insecure-aqt+^z+i%uyjjc(d1u6k%es$=m^*8t+f(u9fni99ls30ic*(sw"

# obviously insecure, you should pass in a better password via environment variable
ARG DJANGO_SUPERUSER_PASSWORD=admin
ARG SUPERUSER_EMAIL=admin@example.com

RUN pip install pipenv

WORKDIR /src
COPY . ./
RUN pipenv install --system --deploy

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin --email $SUPERUSER_EMAIL --noinput
RUN python manage.py loaddata admin_interface_theme_TPSB.json

# runs the development server
CMD python manage.py runserver 0.0.0.0:$PORT

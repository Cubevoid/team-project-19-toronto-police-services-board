# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8000

# obviously insecure, you should pass in a better password via environment variable
ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV SUPERUSER_EMAIL=admin@example.com

RUN pip install pipenv

WORKDIR /src
COPY . ./
RUN pipenv install --system --deploy

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin --email $SUPERUSER_EMAIL --noinput

# runs the development server
CMD python manage.py runserver 0.0.0.0:$PORT

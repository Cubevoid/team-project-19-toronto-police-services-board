# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9-slim-bullseye
ENV PYTHONUNBUFFERED 1

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8000

# TODO: set up proper production webserver and set DEBUG to False
ENV DEBUG "True"

ARG BACKEND_URL "0.0.0.0:$PORT"
ARG FRONTEND_URL "localhost:3000"

# obviously insecure, you should pass in a better password via environment variable
ARG DJANGO_SUPERUSER_PASSWORD=admin
ARG SUPERUSER_EMAIL=admin@example.com

# For wkhtmltopdf, and install libreoffice
RUN apt update --assume-no
RUN apt-get install libreoffice-nogui wget -y --no-install-recommends

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb
RUN apt-get install ./wkhtmltox_0.12.6-1.buster_amd64.deb -y
RUN rm wkhtmltox_0.12.6-1.buster_amd64.deb

RUN pip install pipenv

WORKDIR /src
COPY . ./
RUN pipenv install --system --deploy

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin --email $SUPERUSER_EMAIL --noinput
RUN python manage.py loaddata meetings/fixtures/*.json

ENV BACKEND_URL ${BACKEND_URL}
ENV FRONTEND_URL ${FRONTEND_URL}

# runs the development server
CMD python manage.py test

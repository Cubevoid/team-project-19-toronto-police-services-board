# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM surnet/alpine-wkhtmltopdf:3.13.5-0.12.6-small
FROM python:3.9-alpine
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

# For wkhtmltopdf
RUN apk add --no-cache \
 libstdc++ \
 libx11 \
 libxrender \
 libxext \
 ca-certificates \
 fontconfig \
 freetype \
 ttf-dejavu \
 ttf-droid \
 ttf-freefont \
 ttf-liberation

# Copy patched wkhtmltopdf to current image
COPY --from=0 /bin/wkhtmltopdf /bin/wkhtmltopdf

RUN pip install pipenv

WORKDIR /src
COPY . ./
RUN pipenv install --system --deploy

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin --email $SUPERUSER_EMAIL --noinput
RUN python manage.py loaddata admin_interface_theme_TPSB.json

ENV BACKEND_URL ${BACKEND_URL}
ENV FRONTEND_URL ${FRONTEND_URL}

# runs the development server
CMD python manage.py runserver 0.0.0.0:$PORT

# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8000

# obviously insecure
ENV DJANGO_SUPERUSER_PASSWORD=admin
RUN pip install pipenv

WORKDIR /src
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY meetings/ ./meetings/
COPY tpsb/ ./tpsb/
COPY manage.py ./

RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin --email admin@example.com --noinput

# runs the development server
CMD python manage.py runserver 0.0.0.0:$PORT
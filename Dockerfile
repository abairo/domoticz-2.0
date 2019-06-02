FROM python:3.7.3-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
Run rm -rf /var/cache/apk/*
RUN pip install pipenv
RUN mkdir /code
WORKDIR /code
ADD Pipfile Pipfile.lock /code/
RUN pipenv install --deploy --system --verbose

ADD . /code/ 
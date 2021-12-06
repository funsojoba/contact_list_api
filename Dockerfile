FROM python:3.8-alpine
ENV PYTHONUNBUFFERED = 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

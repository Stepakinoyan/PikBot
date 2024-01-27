FROM python:3.11

WORKDIR /app


COPY . .


RUN pip install --upgrade -r requirements.txt
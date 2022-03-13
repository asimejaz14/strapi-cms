FROM python:3.7-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/


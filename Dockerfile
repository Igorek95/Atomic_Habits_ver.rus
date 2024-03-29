FROM python:3

WORKDIR /django

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .
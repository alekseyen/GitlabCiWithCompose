FROM python:3.9.7-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD url_shortener url_shortener

EXPOSE 8003

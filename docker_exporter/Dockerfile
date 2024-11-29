FROM python:3.9-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y curl

RUN python3 -m pip install --upgrade pip && \
    pip install  --no-cache-dir\ 
    prometheus_client \
    requests \
    flask \

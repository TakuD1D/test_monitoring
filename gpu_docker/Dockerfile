FROM python:3.9-slim

RUN apt update && \
    apt install -y python3-pip && \
    pip install prometheus-client && \
    apt install -y curl
WORKDIR /workspace

# ENTRYPOINT ["python3","filename"]



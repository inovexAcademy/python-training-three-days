FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

WORKDIR /workspace

COPY requirements.txt .

ENV POETRY_VERSION=1.8.3
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install poetry==$POETRY_VERSION
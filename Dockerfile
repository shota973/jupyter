FROM python:3.13.7-slim-bookworm

WORKDIR /app

RUN pip install --upgrade pip
RUN python -m pip install jupyterlab


COPY . .

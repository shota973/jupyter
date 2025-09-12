FROM python:3.13.7-slim-trixie

WORKDIR /app

RUN pip install --upgrade pip
RUN python -m pip install jupyterlab


COPY . .

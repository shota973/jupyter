FROM python:3.13.7-slim-bookworm

WORKDIR /src

RUN pip install --upgrade pip
RUN python -m pip install jupyterlab


COPY . .

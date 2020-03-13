FROM python:3.6

RUN apt-get update && \
    apt-get install -y --no-install-recommends

WORKDIR /work-at-olist
COPY . /work-at-olist

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=libstore-db
ENV POSTGRES_PORT=5432
ENV POSTGRES_HOST=libstore-db

RUN pip install --no-cache-dir -r requirements.txt
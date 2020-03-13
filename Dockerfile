FROM python:3.6

RUN apt-get update && \
    apt-get install -y --no-install-recommends

WORKDIR /work-at-olist
COPY . /work-at-olist

RUN pip install --no-cache-dir -r requirements.txt
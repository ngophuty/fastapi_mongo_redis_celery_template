FROM python:3.10-bullseye

ENV HTTP_PROXY="http://proxy.fpt.vn:80"
ENV http_proxy="http://proxy.fpt.vn:80"
ENV no_proxy=localhost,127.0.0.1,::1,172.24.222.112

WORKDIR /fastapi_mongo_redis_celery_template
COPY . /fastapi_mongo_redis_celery_template

# install debug tool
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    mime-support \
    telnet \
    iputils-ping \
    curl \
    htop \
    vim \
    procps \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip \
    && pip3 install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --proxy http://proxy.fpt.vn:80
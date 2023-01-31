FROM python:3.10-bullseye
WORKDIR /fastapi_mongo_redis_celery_template
COPY . /fastapi_mongo_redis_celery_template
RUN pip3 install poetry \
    poetry install

ENV HTTP_PROXY="http://proxy.fpt.vn:80"
ENV http_proxy="http://proxy.fpt.vn:80"

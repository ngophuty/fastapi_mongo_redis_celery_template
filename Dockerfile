FROM python3.10
WORKDIR /fastapi_mongo_redis_celery_template
COPY . .
# RUN source venv/bin/activate
CMD [python, run_app.py]
EXPOSE 8000
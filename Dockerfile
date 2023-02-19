FROM python:3.10-bullseye

WORKDIR /app
COPY . /app


RUN apt-get update -y
RUN apt-get install -y


RUN pip3 install --upgrade pip \ 
    && pip3 install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install



EXPOSE 8000


CMD ["poetry","run", "python","run_app.py"]
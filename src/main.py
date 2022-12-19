from fastapi import FastAPI
from src.events import startup_event, shutdown_event


app = FastAPI(
    on_startup=startup_event,
    on_shutdown=shutdown_event
)
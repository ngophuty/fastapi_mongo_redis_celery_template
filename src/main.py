from fastapi import FastAPI
from src.events import startup_event, shutdown_event
from src.middlewares import middleware



app = FastAPI(
    middleware=middleware,
    on_startup=startup_event,
    on_shutdown=shutdown_event
)
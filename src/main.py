# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from celery import Celery
from src.events import shutdown_event, startup_event
from src.middlewares import middleware

from .exceptions import ErrorResponseException
from .routers import list_router
from src.celery.setup_celery import celery_app

app = FastAPI(
    middleware=middleware,
    on_startup=startup_event,
    on_shutdown=shutdown_event,
    celery = celery_app
)

app.include_router(list_router)


@app.exception_handler(ErrorResponseException)
async def response_exception_handler(request: Request, exc: ErrorResponseException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "is_success": exc.is_success,
            "data": exc.data,
            "length_data": exc.length_data,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)


@app.get('/')
async def index():
    return {'well come to app'}

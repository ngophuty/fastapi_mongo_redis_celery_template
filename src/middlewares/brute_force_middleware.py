from fastapi import Request
from typing import Any
from fastapi.responses import PlainTextResponse
from src.database.connect_redis import starup_connect_redis
from starlette.types import ASGIApp


class BruteForceDefenderMiddleware:

    def __init__(
        self,
        app: ASGIApp,
        request_time_limit: int = 60,
        number_request_in_minute: int = 30,
    ) -> None:
        self.app = app
        self.request_time_limit = request_time_limit
        self.number_request_in_minute = number_request_in_minute

    @staticmethod
    async def get_ip(request: Request):
        ip_client = request.client.host
        return ip_client
        

    async def  __call__(self, request: Request) -> Any:
        redis_cache = await starup_connect_redis()
        client_host = await self.get_ip(request)
        check_client = redis_cache.get(client_host)
        if not check_client:
            redis_cache.set(client_host, value = self.number_request_in_minute, ex=self.request_time_limit)
        count_request = redis_cache.incr(client_host)
        if int(count_request) > self.number_request_in_minute:
            return PlainTextResponse(content='You are blocked, Try again later', status_code=403)
        return


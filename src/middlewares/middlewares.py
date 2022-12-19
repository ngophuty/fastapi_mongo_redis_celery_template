from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
import redis

async def get_ip_client(request: Request):
    client_host = request.client.host
    return client_host


class BurteForceDefenderMiddleWares:
    def __init__(
        self,
        time_limit,
        request_limit

    ) -> None:
        self.time_limit = time_limit
        self.request_limit = request_limit 
              

    async def count_request(request: Request, call_next):
        response = await call_next(request)
        client_host = request.client.host
        check_client = redis_db.get(client_host)
        if not check_client:
            redis_db.set(client_host, value=0, ex=60)
        count = redis_db.incr(client_host)
        if int(count) > 30:
            return JSONResponse(content= {'mess': 'to many request'})
        return response
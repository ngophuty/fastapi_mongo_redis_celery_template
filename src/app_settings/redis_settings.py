# -*- coding: utf-8 -*-
from pydantic import BaseSettings


class RedisSettings(BaseSettings):

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

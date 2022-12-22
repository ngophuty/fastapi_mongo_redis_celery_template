# -*- coding: utf-8 -*-
from .base_settings import BaseSettingsMixin
from .celery_settings import CelerySettings
from .fastapi_settings import FastApiSettings
from .mongodb_settings import MongoDBSettings
from .proxy_settings import ProxySettings
from .redis_settings import RedisSettings


class AppSettings(
    FastApiSettings,
    MongoDBSettings,
    RedisSettings,
    BaseSettingsMixin,
    ProxySettings,
    CelerySettings,
):
    class Config:
        case_sensitive = True
        validate_assignment = True


settings = AppSettings(_env_file=".env")
settings.setup_proxy()

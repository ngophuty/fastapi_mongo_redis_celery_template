# -*- coding: utf-8 -*-
from . import FastApiSettings, MongoDBSettings, RedisSettings
from .base_settings import BaseSettingsMixin
from .celery_settings import CelerySettings
from .proxy_settings import ProxySettings


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

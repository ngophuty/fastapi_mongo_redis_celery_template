from . import FastApiSettings, MongoDBSettings, RedisSettings
from .base_settings import BaseSettingsMixin
from .proxy_settings import ProxySettings
from .celery_settings import CelerySettings

class AppSettings(
    FastApiSettings,
    MongoDBSettings,
    RedisSettings,
    BaseSettingsMixin,
    ProxySettings,
    CelerySettings
):

    class Config:
        case_sensitive = True
        validate_assignment = True 


settings = AppSettings(_env_file='.env')
settings.setup_proxy()
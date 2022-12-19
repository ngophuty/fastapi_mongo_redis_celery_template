
from . import FastApiSettings, MongoDBSettings, RedisSettings


class AppSettings(
    FastApiSettings,
    MongoDBSettings,
    RedisSettings
):

    class Config:
        validate_assignment = True 


settings = AppSettings(_env_file='.env')
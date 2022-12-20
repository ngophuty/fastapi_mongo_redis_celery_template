from . import FastApiSettings, MongoDBSettings, RedisSettings


class AppSettings(
    FastApiSettings,
    MongoDBSettings,
    RedisSettings,
    # BaseSettingsMixin
):

    class Config:
        case_sensitive = True
        validate_assignment = True 


settings = AppSettings(_env_file='.env')
# settings.setup_proxy()
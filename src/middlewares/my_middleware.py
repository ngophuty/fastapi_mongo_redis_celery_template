from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from src.app_settings import settings
from src.middlewares import BruteForceDefenderMiddleware


middleware_controler = (
    {
        'enable': settings.FAPP_MIDDLEWARE_ENABLE_CORSMiddleware,
        'middleware': Middleware(
            CORSMiddleware,
            allow_origins = settings.FAPP_MIDDLEWARE_CORS_ALLOW_ORIGINS,
            allow_methods = settings.FAPP_MIDDLEWARE_CORS_ALLOW_METHODS,
            allow_headers = settings.FAPP_MIDDLEWARE_CORS_ALLOW_HEADERES,
            allow_credentials = False,
            allow_origin_regex = None,
            expose_headers = (),
            max_age = 600,

        )
    },
    {
        'enable': settings.FAPP_MIDDLEWARE_ENABLE_BurteMiddleware,
        'middleware': Middleware(BruteForceDefenderMiddleware)
    }

)

middleware = [config.get('middleware') for config in middleware_controler if config.get('enable')==True]
import os

SELECT_ENV_NAME = os.environ.get('APP_ENV_NAME')

class BaseSettingMixin:
    async def select_env(self) -> str:
        if SELECT_ENV_NAME in ('dev', 'stg', 'prod', 'local', 'redirect'):
            env_name = f'{SELECT_ENV_NAME}.env'
        else:
            env_name = '.env'
        return env_name
    
    async def setup_proxy(self):
        await self.add_custom_proxy()

    async def add_custom_proxy(self):
        if (
            not hasattr(self, 'APP_USE_PROXY')
            or not hasattr(self, 'APP_PROXY_ADD')
            or not hasattr(self, 'APP_NO_PROXY')
        ):
            print('Not found proxy configurations')
        
        if not getattr(self, 'APP_USE_PROXY'):
            return
        
        no_proxy = os.environ.get('no_proxy')
        
        if getattr(self, 'APP_USE_PROXY'):
            for i in ['http', 'https']:
                os.environ[i] = getattr(self, 'APP_USE_PROXY')
        if getattr(self, 'APP_NO_PROXY'):
            if no_proxy:
                os.environ['no_proxy'] = no_proxy + ',' + getattr(self, 'APP_NO_PROXY')
            else:
                os.environ['no_proxy'] = getattr(self, 'APP_NO_PROXY')
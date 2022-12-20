import uvicorn
from src.app_settings import settings

if __name__ == "__main__":
    uvicorn.run(
        'src.main:app',
        host = settings.FAPP_HOST,
        port = int(settings.FAPP_PORT),
        reload = settings.FAPP_RELOAD
    )


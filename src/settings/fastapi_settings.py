from typing import List, Optional

from pydantic import BaseSettings


class FastApiSettings(BaseSettings):

    FAPP_HOST: Optional[str] = 'localhost'
    FAPP_PORT: Optional[str] = '8000'
    FAPP_RELOAD: bool = False
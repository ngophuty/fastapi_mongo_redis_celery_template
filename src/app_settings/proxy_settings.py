# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseSettings


class ProxySettings(BaseSettings):

    APP_USE_PROXY: Optional[bool] = False
    APP_PROXY_ADD: Optional[str] = ""
    APP_NO_PROXY: Optional[str] = ""

    class Config:
        case_sensitive = True
        validate_assignment = True

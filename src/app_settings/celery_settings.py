# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel


class CelerySettings(BaseModel):
    CELERY_RESULT_BACKEND: Optional[str]
    CELERY_BROKER_URL: Optional[str]

from pydantic import BaseModel
from typing import Optional

class CelerySettings(BaseModel):
    CELERY_RESULT_BACKEND: Optional[str]
    CELERY_BROKER_URL: Optional[str]

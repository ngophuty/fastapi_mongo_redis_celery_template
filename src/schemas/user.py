from pydantic import BaseModel, validator
from typing import Optional
from fastapi.exceptions import HTTPException

class CreatUser(BaseModel):
    email: str
    username: str
    password: str
    re_password: str

    @validator('username')
    def validate_user_name(cls, value):
        if any(not c.isalnum() for c in value):
            raise HTTPException(
            detail="username must be not contain spaces or special characters",
            status_code= 400
            )

    @validator('re_password')
    def validate_password(cls, value, values):
        if len(values.get('password')) < 6 :
            raise HTTPException(
            detail="password at least 6 characters",
            status_code= 200
            )
        if value != values.get('password'):
            raise HTTPException(
            detail="password do not match",
            status_code= 200
            )

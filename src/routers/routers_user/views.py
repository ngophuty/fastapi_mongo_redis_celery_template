# -*- coding: utf-8 -*-
from fastapi import APIRouter
from src.schemas.user import CreatUser
from .utils import create_user

router = APIRouter(prefix="/app")


@router.post('/sign_in')
async def sign_in(user: CreatUser):
    create = await create_user(user)
    pass


@router.post('/login')
async def login():
    pass
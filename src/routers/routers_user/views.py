# -*- coding: utf-8 -*-
from fastapi import APIRouter
from src.schemas.user import CreateUser, UserLogin
from .utils import create_user, user_login

router = APIRouter(prefix="/app")


@router.post('/sign_in')
async def sign_in(user: CreateUser):
    create = await create_user(user)
    return create


@router.post('/login')
async def login(login: UserLogin):
    log = await user_login(login)
    return log
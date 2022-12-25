# -*- coding: utf-8 -*-
from fastapi import APIRouter
from src.schemas.user import CreateUser, UserLogin, RequestUserProfile, DeletetProfile
from .utils import create_user, user_login, get_profile, create_profile, update_profile, delete_profile

router = APIRouter(prefix="/app")


@router.post('/sign_in')
async def sign_in(user: CreateUser):
    create = await create_user(user)
    return create


@router.post('/login')
async def login(login: UserLogin):
    log = await user_login(login)
    return log


@router.post('/create_profile_user')
async def create_profile_user(request: RequestUserProfile):
    create = await create_profile(request)
    return create


@router.post('/get_profile_user')
async def get_profile_user():
    data = await get_profile()
    return data


@router.post('/update_profile_user')
async def update_profile_user(request: RequestUserProfile):
    update = await update_profile(request)
    return update


@router.post('/delete_profile_user')
async def delete_profile_user(request: DeletetProfile):
    await delete_profile(request)
    return
# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter(prefix="/app")


@router.post('/sign_in')
async def sign_in():
    pass
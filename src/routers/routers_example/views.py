# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter(prefix="/app")


@router.get("")
def well_come():
    return {"well come to app"}

from typing import Optional

from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request

from app.utils import logger

router = r = APIRouter()


@r.post("/")
async def google_auth(request: Request):
    try:
        data = await request.json()
        code = data['code'] if 'code' in data else None
        pass
        return JSONResponse('test')
    except Exception as e:
        logger.error('An exception occurred: %s' % e)
        return JSONResponse({'type': 'error', 'message': "Couldn't auth in google"})
    

__all__ = ["router"]

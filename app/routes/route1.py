from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException

from app.utils import logger

router = r = APIRouter()


@r.get("/")
async def route1(startDate: str, endDate: str):
    try:
        pass
        return JSONResponse('test')
    except HTTPException as http_error:
        logger.error(
            f"HTTP Error {http_error.status_code}: {http_error.detail}")
        return JSONResponse({'type': 'error', 'message': 'Unauthorized'}, status_code=401)
    except Exception as e:
        logger.error('An exception occurred: %s' % e)
        return JSONResponse({'type': 'error', 'message': 'An exception occurred'})


__all__ = ["router"]

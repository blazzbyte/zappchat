from fastapi import APIRouter

from . import route1, route2

router = APIRouter()

router.include_router(route2.router, prefix="/route1", tags=["test1"])
router.include_router(route1.router, prefix="/route2", tags=["test2"])

__all__ = ['router']

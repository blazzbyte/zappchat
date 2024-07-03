from fastapi import APIRouter

from . import products, route2

api_router = APIRouter()

api_router.include_router(route2.router, prefix="/route2", tags=["api"])
api_router.include_router(products.router, prefix="/products", tags=["api"])

__all__ = ['api_router']
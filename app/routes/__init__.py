from fastapi import APIRouter

from . import products

api_router = APIRouter()

api_router.include_router(products.router, prefix="/products", tags=["api"])

__all__ = ['api_router']

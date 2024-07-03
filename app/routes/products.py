from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException
from app.llm.stores import supabase_store
from app.utils import logger

router = r = APIRouter()


@r.post("/all")
async def add_all_products():
    try:
        data = supabase_store.add_products_from_path(
            'data/company/products.json', 'data/company/product_ids.json')
        return JSONResponse({'type': 'data', 'message': 'Products have been successfully added: %s' % data})
    except Exception as e:
        logger.error('An exception occurred adding products: %s' % e)
        return JSONResponse({'type': 'error', 'message': 'An exception occurred'})

__all__ = ["router"]

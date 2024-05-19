from fastapi import APIRouter
from di_container import get_container
from features.filter_products.ai_product_filterer import AiProductFilterer
from features.filter_products.product import Product


router = APIRouter()

@router.get("/api/products/{search_phrase}", tags=["products"], response_model=None)
async def filter_products(search_phrase: str) -> list[Product]:
    searcher: AiProductFilterer = get_container().get_service(AiProductFilterer)
    products = searcher.filter(search_phrase)
    return products
    
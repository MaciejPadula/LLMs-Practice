from fastapi import FastAPI
import uvicorn
from di_container import get_container
from features.filter_products.ai_product_filterer import AiProductFilterer
from features.filter_products.filter_product_endpoint import router as filter_product_router
from infrastructure.openai_product_filter import OpenAiProductFilter


app = FastAPI()
app.include_router(filter_product_router)

def bootstrap():
    services = get_container()
    services.register(AiProductFilterer, None, lambda: OpenAiProductFilter(""))

def main():
    bootstrap()
    uvicorn.run(app, port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()
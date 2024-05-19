import json
from features.filter_products.ai_product_filterer import AiProductFilterer
from features.filter_products.product import Product
from openai import OpenAI

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

class OpenAiProductFilter(AiProductFilterer):
    def __init__(self, openai_api_key: str):
        self.client = OpenAI(api_key=openai_api_key)

    def filter(self, search_phrase: str) -> list[Product]:
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "You have to search for a product by it's name. Here is an input provided from user.\nPlease provide a list of product names on which you can filter the products. Return as mauch as you can please :). Result should be a JSON list of strings!!!! And do not add json word at the beginning."
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": search_phrase
                    }
                ]
                }
            ],
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        result = response.choices[0].message.content
        
        filtering_keywords: list[str] = set(flatten_list(map(lambda x: x.lower().split(), json.loads(result))))
        
        filtered_result = filter(
            lambda x: x.name.lower() in filtering_keywords,    
            self.products
        )
        
        return list(filtered_result)
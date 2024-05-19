from features.filter_products.product import Product


class AiProductFilterer:
    products = [
        Product("Apple", 1.00),
        Product("Banana", 0.50),
        Product("Orange", 0.75),
        Product("Mango", 1.25),
        Product("Pineapple", 2.00),
        Product("Kiwi", 0.75),
        Product("Strawberry", 1.50),
        Product("Blueberry", 1.00),
        Product("Raspberry", 1.25),
        Product("Blackberry", 1.00),
        Product("Grape", 1.00),
        Product("Cherry", 1.25),
        Product("Watermelon", 3.00),
        Product("Cantaloupe", 2.50),
        Product("Honeydew", 2.50),
        Product("Cucumber", 5)
    ]

    def filter(self, search_phrase: str) -> list[Product]:
        raise NotImplemented
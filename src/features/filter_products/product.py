from decimal import Decimal


class Product:
    def __init__(self, name: str, price: Decimal):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
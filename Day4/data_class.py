from dataclasses import dataclass, field
from typing import List


@dataclass
class Products:
    name: str
    price: float


@dataclass
class Order:
    products: List[Products] = field(default_factory=list)

    def add_product(self, product: Products):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)


order = Order()
order.add_product(Products("Book", 12.99))
order.add_product(Products("Pen", 1.50))
order.add_product(Products("A4 sheet bundle", 15.50))
order.add_product(Products("Cello tape", 1.20))

print(order)
print("Total Price:", round(order.total_price(), 2))
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        if product_name in self.products:
            return product_name

    def remove(self, product_name):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)

    def __repr__(self):
        result = [f'{p.name}: {p.quantity}' for p in self.products]
        return '\n'.join(result)

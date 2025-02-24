from abc import ABC, abstractmethod

class Department(ABC):
    def __init__(self, name: str):
        self.name: str = name
        self.products: list = []

    def add_product(self, product: str):
        self.products.append(product)

    def remove_product(self, product_name: str):
        self.products = [product for product in self.products if product != product_name]

    @abstractmethod
    def department_info(self):
        pass

    def __str__(self):
        return f"Department: {self.name}, Products: {self.products}"

from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

from abc import ABC, abstractmethod

class IProductsService(ABC):
    @abstractmethod
    def add_stock(self, product):
        pass

    @abstractmethod
    def add_product(self, id: str, name: str, price: float, quantity: int = 0):
        pass

    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, id):
        pass
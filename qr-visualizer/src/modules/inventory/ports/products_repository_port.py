from abc import ABC, abstractmethod

class Product:
    id: str
    name: str
    price: float
    quantity: int

class IProductsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, id: str, product: Product):
        pass

    @abstractmethod
    def create(self, product: Product):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass
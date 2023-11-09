from abc import ABC, abstractmethod

class Product:
    pass

class IProductsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, id, product):
        pass

    @abstractmethod
    def create(self, product):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass
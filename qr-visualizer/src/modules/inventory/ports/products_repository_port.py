from abc import ABC, abstractmethod

class Product:
    pass

class IProductsRepository(ABC):
    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def update(self, id, product):
        pass

    @abstractmethod
    async def create(self, product):
        pass

    @abstractmethod
    async def get_by_id(self, id):
        pass
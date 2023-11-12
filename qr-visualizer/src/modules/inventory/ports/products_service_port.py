from abc import ABC, abstractmethod

class IProductsService(ABC):
    @abstractmethod
    async def add_stock(self, product):
        pass

    @abstractmethod
    async def add_product(self, id, name, price, quantity = 0):
        pass

    @abstractmethod
    async def get_products(self):
        pass

    @abstractmethod
    async def get_product_by_id(self, id):
        pass
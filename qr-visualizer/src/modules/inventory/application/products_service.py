from modules.inventory.ports.products_repository_port import Product
from modules.inventory.ports.products_service_port import IProductsService

class ProductsService(IProductsService):
    def __init__(self, products_repository):
        self.products_repository = products_repository

    async def get_products(self):
        return await self.products_repository.get_all()

    async def add_product(self, name, price, quantity = 0):
        new_product = Product()        
        new_product.productName = name
        new_product.description = name
        new_product.categoryId = 1
        new_product.supplierId = 1
        new_product.price = price
        new_product.quantityInStock = quantity

        return await self.products_repository.create(product=new_product)
    
    async def add_stock(self, product):
        updated_product = { 'quantity': 1 }
        await self.products_repository.update(str(product['id']), updated_product)

    async def get_product_by_id(self, id):
        return await self.products_repository.get_by_id(id=id)
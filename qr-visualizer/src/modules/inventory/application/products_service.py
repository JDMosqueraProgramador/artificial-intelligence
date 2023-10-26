
from modules.inventory.ports.products_repository_port import IProductsRepository, Product
from modules.inventory.ports.products_service_port import IProductsService

class ProductsService(IProductsService):
    def __init__(self, products_repository: IProductsRepository):
        self.products_repository = products_repository

    def get_products(self):
        return self.products_repository.get_all()

    def add_product(self, id: str, name: str, price: float, quantity: int = 0):
        new_product = Product()        
        new_product.id = id
        new_product.name = name
        new_product.price = price
        new_product.quantity = quantity

        return self.products_repository.create(product=new_product)
    
    def add_stock(self, product):
        updated_product = Product()
        print(product.quantity)
        updated_product.quantity = product.quantity + 1
        self.products_repository.update(product.id, updated_product)

    def get_product_by_id(self, id):
        return self.products_repository.get_by_id(id=id)
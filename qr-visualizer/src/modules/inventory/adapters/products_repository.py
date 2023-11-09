from modules.inventory.ports.products_repository_port import IProductsRepository

class ProductsRepository(IProductsRepository):
    products = []
    def __init__(self):
        pass

    def  get_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product

    def get_all(self):
        return self.products
    
    def update(self, id, product):
        for i, current_product in enumerate(self.products):
            if current_product.id == id:
                current_product.__dict__.update(product.__dict__)
                print("product name: ", current_product.quantity)
                self.products[i] = current_product
                break

    def create(self, product):
        self.products.append(product)
        return product
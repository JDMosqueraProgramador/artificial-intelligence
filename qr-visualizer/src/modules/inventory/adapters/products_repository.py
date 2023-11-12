import requests
import os
from modules.inventory.ports.products_repository_port import IProductsRepository

class ProductsRepository(IProductsRepository):
    def __init__(self):
        self.products_url = os.getenv('PRODUCTS_URL') 
        pass

    async def get_by_id(self, id):
        results = requests.get(self.products_url + id).json()
        return results

    async def get_all(self):
        results = requests.get(self.products_url).json()
        return results
    
    async def update(self, id, product):
        print("product id", id, product)
        results = requests.patch(self.products_url + "stock/" + id, json=product).json()
        return results

    async def create(self, product):
        results = requests.post(self.products_url, json=product.dict()).json()
        return results

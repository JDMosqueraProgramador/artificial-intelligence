from modules.camera.infrastructure.adapters.ocv_camera import Camera

class DroneScanner(Camera):
    def __init__(self, products_service):
        super().__init__()
        self.products_service = products_service

    async def decode_qrs(self, img):
        data = await super().decode_qrs(img)
        if data.__len__() > 0:
            print(data)

        for product_info in data:
            product = await self.products_service.get_product_by_id(id=product_info)

            if not product:
                product = await self.products_service.add_product( 
                    name=product_info, 
                    price=12, 
                    quantityInStock=1
                )

            await self.products_service.add_stock(product)
        
        return data


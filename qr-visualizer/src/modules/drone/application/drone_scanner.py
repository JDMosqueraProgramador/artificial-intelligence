from modules.camera.infrastructure.adapters.ocv_camera import Camera

class DroneScanner(Camera):
    def __init__(self, products_service):
        super().__init__()
        self.products_service = products_service

    def decode_qrs(self, img):
        data = super().decode_qrs(img)
        for product_info in data:
            product = self.products_service.get_product_by_id(id=product_info)

            if not product:
                product = self.products_service.add_product(
                    id=product_info, 
                    name=product_info, 
                    price=12, 
                    quantity=1
                )

            self.products_service.add_stock(product)
        
        return data

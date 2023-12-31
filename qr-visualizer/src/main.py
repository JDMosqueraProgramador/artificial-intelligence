import asyncio
from dotenv import load_dotenv
load_dotenv()
from modules.inventory.adapters.products_repository import ProductsRepository
from modules.inventory.application.products_service import ProductsService
from modules.drone.application.drone_scanner import DroneScanner

repo = ProductsRepository()
products_service = ProductsService(repo)

drone = DroneScanner(products_service)

asyncio.run(drone.read_camera())
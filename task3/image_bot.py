from api_client import APIClient
from image_service import ImageService
from handlers import Handlers
from config import Settings

class ImageBot():
    def __init__(self):
        self.token = Settings.BOT_TOKEN
        self.api_client = APIClient() 
        self.image_service = ImageService()
        self.handlers = Handlers(self.image_service)
from typing import Dict, Any
from supabase import Client

from app.utils import logger


class ProductService:
    def __init__(self, sb_client: Client):
        self.sb: Client = sb_client

    def add_product(self, product: Dict[str, Any]) -> Dict[str, Any]:
        response = self.sb.table('documents').insert(product).execute()
        if response.get('error'):
            logger.error(f"Error uploading product: {response['error']}")
        return response['data']

    def get_products(self):
        """
        Retrieves the list of products from the WhatsApp API.
        """
        pass

    def get_product(self, product_id: str):
        """
        Retrieves a specific product by its ID from the WhatsApp API.
        """
        pass

    def get_catalog(self):
        """
        Retrieves a catalog of products from the WhatsApp API.
        """
        pass

    def send_product(self, recipient: str, product_details: dict):
        """
        Sends the details of a product to a recipient via WhatsApp.
        """
        pass

    def send_catalog(self, recipient: str, catalog_items: list):
        """
        Sends a catalog of products to a recipient via WhatsApp.
        """
        pass

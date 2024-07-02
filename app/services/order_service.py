# services/orders/order_service.py

class OrderService:
    def __init__(self, wa):
        self.wa = wa

    def create_order(self, order_details: dict):
        """
        Creates a new order using the provided details.
        """
        pass

    def get_orders(self):
        """
        Retrieves the list of orders from the WhatsApp API.
        """
        pass

    def get_order(self, order_id: str):
        """
        Retrieves a specific order by its ID from the WhatsApp API.
        """
        pass

    def cancel_order(self, order_id: str):
        """
        Cancels a specific order by its ID.
        """
        pass

    def update_order_status(self, order_id: str, status: str):
        """
        Updates the status of a specific order.
        """
        pass
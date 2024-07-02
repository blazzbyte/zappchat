

class MessageService:
    def __init__(self):
        self.chat_history = {}

    def send_message(self, recipient_id: str, message: str):
        # Implementar lógica para enviar un mensaje a un destinatario
        pass

    def send_media(self, recipient_id: str, media_url: str, media_type: str):
        # Implementar lógica para enviar media (imagen, video, etc.)
        pass

    def send_template_message(self, recipient_id: str, template_name: str, template_data: dict):
        # Implementar lógica para enviar mensajes basados en plantillas
        pass

    def receive_message(self, message_id: str):
        # Implementar lógica para recibir un mensaje
        pass

    def receive_media(self, media_id: str):
        # Implementar lógica para recibir media (imagen, video, etc.)
        pass

    def receive_template_response(self, template_response_id: str):
        # Implementar lógica para recibir respuestas a plantillas
        pass

    def get_chat_history(self, sender_id: str):
        return self.chat_history.get(sender_id, [])
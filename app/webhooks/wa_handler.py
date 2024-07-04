from pywa import WhatsApp
from pywa.types import Message

from app.llm.agents.handle_agent import handle_message_agent
from app.utils import logger


def handle_message(client: WhatsApp, msg: Message):
    try:
        handle_message_agent(client, msg)
    except Exception as e:
        logger.error('An exception occurred %s' % e)
        msg.reply('Currently, I cannot respond to your message, a ticket has been opened, you will receive a response shortly.')

## Testing ##
# headers = {
#     "Authorization": f"Bearer {wa_token}",
#     "Content-Type": "application/json",
# }
# url = f"https://graph.facebook.com/v19.0/xxx/messages"
# recipient = msg.sender
# print(url, "tooo", recipient)
# data = {
#     "messaging_product": "whatsapp",
#     "recipient_type": "individual",
#     "to": recipient,
#     "type": "text",
#     "text": {"body": "Hello, World!"}
# }
# res = requests.post(
#     url=url,
#     headers=headers,
#     json=data
# )
# print(res.json())

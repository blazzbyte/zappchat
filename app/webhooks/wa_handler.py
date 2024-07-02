from pywa import WhatsApp
from pywa.types import Message, CallbackButton, CallbackSelection, MessageStatus, ChatOpened

from app.utils import logger

def handle_message(client: WhatsApp, msg: Message):
    try:
      response = 'call params: client and msg'
      client.get_business_phone_number()
    except Exception as e:
      logger.error('An exception occurred %s' % e)
      msg.reply('Currently, I cannot respond to your message, a ticket has been opened, you will receive a response shortly.')


def handle_callback_button(client: WhatsApp, clb: CallbackButton):
    pass


def handle_callback_selection(client: WhatsApp, selection: CallbackSelection):
    pass


def handle_message_status(client: WhatsApp, status: MessageStatus):
    pass


def handle_chat_opened(client: WhatsApp, chat: ChatOpened):
    pass

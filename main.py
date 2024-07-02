from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from pywa import WhatsApp
from pywa.types import Message, CallbackButton, CallbackSelection, MessageStatus, ChatOpened

from app.webhooks.wa_handler import handle_message, handle_callback_button, handle_callback_selection, handle_message_status, handle_chat_opened
from app.core import config

whatsapp_token = config.get_whatsapp_token()


app = FastAPI()

# ** Whatsapp Client **
wa = WhatsApp(
    phone_id='15556203053',
    token='EAAMmjtT0FgMBOyPRnvltuRJCSDzLMNKMZBqZCblsETIHCPlzYPlb9p452GVBEMetlbF2ycwvIxfO9gIY6XJGT43lY4SsbBxHEJGp9ZAVzLwgu2yLTfumwIs2qXjaOfxWJRnlsuZAkdNI9uOh7BxZAZB8LePelXmU3UUZBjZAr4MBIaHwjfZAjYkzokVtGtjL5ipLqkSdmWRNBgZAW9moZBDtQYZD',
    server=app,
    verify_token='75119826'
)


# ** Whatsapp WebHooks **
@wa.on_message()
def on_message_handler(client: WhatsApp, msg: Message):
    handle_message(client, msg)


@wa.on_callback_button()
def on_callback_button_handler(client: WhatsApp, clb: CallbackButton):
    handle_callback_button(client, clb)


@wa.on_callback_selection()
def on_callback_selection_handler(client: WhatsApp, selection: CallbackSelection):
    handle_callback_selection(client, selection)


@wa.on_message_status()
def on_message_status_handler(client: WhatsApp, status: MessageStatus):
    handle_message_status(client, status)


@wa.on_chat_opened()
def on_chat_opened_handler(client: WhatsApp, chat: ChatOpened):
    handle_chat_opened(client, chat)
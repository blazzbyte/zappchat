from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from pywa import WhatsApp
from pywa.types import Message, CallbackButton, CallbackSelection, MessageStatus, ChatOpened

from app.routes import api_router
from app.webhooks.wa_handler import handle_message, handle_callback_button, handle_callback_selection, handle_message_status, handle_chat_opened
from app.core import config

app = FastAPI()

# ** Middlewares **
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# ** Routes **
@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(api_router, prefix="/api")

# ** -------- WHATSAPP ------- **
wa_token = config.get_wa_token()
wa_phone_id = config.get_wa_phone_id()
wa_verify_token = config.get_wa_verify_id()

# ** Whatsapp Client **
wa = WhatsApp(
    phone_id=wa_phone_id,
    token=wa_token,
    server=app,
    verify_token=wa_verify_token
)

# ** Whatsapp WebHooks **
@wa.on_message()
def on_message_handler(client: WhatsApp, msg: Message):
    handle_message(client, msg.reply)

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

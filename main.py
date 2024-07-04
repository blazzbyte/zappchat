from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pywa import WhatsApp
from pywa.handlers import MessageHandler

from app.webhooks.wa_handler import handle_message
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

# app.include_router(api_router, prefix="/api")

# ** -------- WHATSAPP ------- **
wa_token = config.get_wa_token()
wa_phone_id = config.get_wa_phone_id()
wa_verify_token = config.get_wa_verify_id()

# ** Whatsapp Client **
wa = WhatsApp(
    phone_id=wa_phone_id,
    token=wa_token,
    server=app,
    verify_token=wa_verify_token,
    api_version=19.0
)

# ** Whatsapp WebHooks **
wa.add_handlers(MessageHandler(handle_message))

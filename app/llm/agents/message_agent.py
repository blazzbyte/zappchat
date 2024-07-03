from ..stores import supabase_store

from pywa import WhatsApp
from pywa.types import Message

def agent(client: WhatsApp, msg: Message):
    msg.reply_catalog()

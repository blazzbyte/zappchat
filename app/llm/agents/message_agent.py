from ..stores import supabase_store

from pywa import WhatsApp
from pywa.types import Message

from app.llm.agents.agent import Agent

def agent(client: WhatsApp, msg: Message):
    msg.reply_catalog()

    agent = Agent()

    agent.invoke({"input": "hi, im bob", "datehour": 'The current date is Wednesday, July 03, 2024 and the current time in 24h format is 23:56:49'})
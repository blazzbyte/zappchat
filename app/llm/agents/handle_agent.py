from __future__ import annotations

from pywa import WhatsApp
from pywa.types import Message, MessageType

from .agent_message import agent_message
from ..utils.message import extract_message_content

from app.core import config

# Define a dictionary that maps message types to their string representations
MESSAGE_TYPES = {
    MessageType.TEXT: "text",
    MessageType.IMAGE: "image",
    MessageType.VIDEO: "video",
    MessageType.AUDIO: "audio",
    MessageType.DOCUMENT: "document",
    MessageType.STICKER: "sticker",
    MessageType.LOCATION: "location",
    MessageType.CONTACTS: "contacts",
    MessageType.ORDER: "order",
    MessageType.SYSTEM: "system",
    MessageType.REACTION: "reaction",
}


def handle_message_agent(_: WhatsApp, msg: Message):
    """
    This function processes incoming WhatsApp messages and generates a response using an LLM agent.

    Args:
        client: The WhatsApp client.
        msg: The incoming WhatsApp message.
    """

    ## ** Extract relevant information from message ** ##
    message_type = MESSAGE_TYPES.get(msg.type, "unknown")
    message_content = extract_message_content(msg)

    user_message = (
        f"User sent a {message_type} message: {message_content}"
        if message_content
        else f"User sent a {message_type} message."
    )

    ## ** LLM Agent ** ##
    agent = agent_message()

    response = agent.invoke(
        {"input": user_message,
         "datehour": 'The current date is Wednesday, July 04, 2024 and the current time in 24h format is 23:56:49'}
    )

    if (isinstance(response, dict) and "type" in response):
        if (response["output"]["type"] == "location"):
            msg.reply_location()
        elif (response["output"]["type"] == "product"):
            products = response["output"]["metadatas"]
            product_ids = [product["id"] for product in products]
            print(product_ids)
            catalog_id = config.get_wa_catalog_id()
            msg.reply_product(
                catalog_id=catalog_id,
                sku=product_ids[0],
                body="The product that best matches your search is this one."
            )

    else:
        msg.reply_text(text=response["output"])

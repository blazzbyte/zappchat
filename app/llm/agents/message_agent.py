from __future__ import annotations

from typing import Any

from pywa import WhatsApp
from pywa.types import Message, MessageType

from langchain_core.tools import StructuredTool
from langchain.pydantic_v1 import BaseModel, Field

from app.llm.agents.agent import Agent
  
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


def agent(client: WhatsApp, msg: Message):
    """
    This function processes incoming WhatsApp messages and generates a response using an LLM agent.

    Args:
        client: The WhatsApp client.
        msg: The incoming WhatsApp message.
    """
    # Extract relevant information from the message
    message_type = MESSAGE_TYPES.get(msg.type, "unknown")
    message_content = extract_message_content(msg)
    user_message = (
        f"User sent a {message_type} message: {message_content}"
        if message_content
        else f"User sent a {message_type} message."
    )
    
    class MapsInput(BaseModel):
        a: bool = Field(description="Order to send the location")


    def send_location(a: bool, b: Message = msg) -> int:
        """Send the location of the store to user"""
        b.reply_location()


    Map_tool = StructuredTool.from_function(
        func=send_location,
        name="Location",
        description="Sends the maps location of the store",
        args_schema=MapsInput,
        return_direct=True,
    )

    # Initialize the LLM agent
    agent = Agent(tooles=Map_tool)

    response = agent.invoke({"input": "hi, im bob", "datehour": 'The current date is Wednesday, July 03, 2024 and the current time in 24h format is 23:56:49'})

    # Handle the agent's response
    handle_agent_response(client, msg, response)


def extract_message_content(msg: Message) -> str | None:
    """
    This function extracts the content from different message types.

    Args:
        msg: The incoming WhatsApp message.

    Returns:
        The content of the message as a string, or None if the message type is not supported.
    """
    if msg.type == MessageType.TEXT:
        return msg.text
    elif msg.type == MessageType.IMAGE:
        return msg.image.download()
    elif msg.type == MessageType.VIDEO:
        return msg.video.download()
    elif msg.type == MessageType.AUDIO:
        return msg.audio.download()
    elif msg.type == MessageType.DOCUMENT:
        return msg.document.download()
    elif msg.type == MessageType.LOCATION:
        return f"Latitude: {msg.location.latitude}, Longitude: {msg.location.longitude}"
    elif msg.type == MessageType.CONTACTS:
        return ", ".join([contact.name.formatted_name for contact in msg.contacts])
    elif msg.type == MessageType.ORDER:
        return f"Order for {len(msg.order.products)} products"
    elif msg.type == MessageType.SYSTEM:
        return msg.system.body
    elif msg.type == MessageType.REACTION:
        return msg.reaction.emoji
    else:
        return None


def handle_agent_response(client: WhatsApp, msg: Message, response: Any) -> None:
    """
    This function handles the LLM agent's response and sends it back to the user.

    Args:
        client: The WhatsApp client.
        msg: The incoming WhatsApp message.
        response: The LLM agent's response.
    """
    # Example: Send the agent's response as a text message
    client.send_message(to=msg.from_user.wa_id, text=response["output"])

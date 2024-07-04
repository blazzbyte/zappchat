from __future__ import annotations

import os
import base64
from typing import Any

from pywa import WhatsApp
from pywa.types import Message, MessageType

from langchain_google_vertexai import ChatVertexAI, HarmBlockThreshold, HarmCategory
from langchain_core.messages import HumanMessage
from langchain_core.tools import StructuredTool
from langchain.pydantic_v1 import BaseModel, Field

from app.core import config
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
        description="Sends the maps location of the store, when the user ask for it",
        args_schema=MapsInput,
        return_direct=True,
    )
    os.makedirs(os.path.join(os.getenv("ROOT_DIR"), "temp"), exist_ok=True)
    # Initialize the LLM agent
    agent = Agent(tooles=Map_tool)

    response = agent.invoke({"input": user_message, "datehour": 'The current date is Wednesday, July 04, 2024 and the current time in 24h format is 23:56:49'})

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
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }

    llm = ChatVertexAI(
        model_name= "gemini-1.5-pro-preview-0514",
        temperature= 0.0,
        max_retries= 5,
        max_tokens= 1024,
        project= config.get_google_project_id or os.getenv("VERTEXAI_PROJECT"),
        location= "asia-southeast1",
        safety_settings= safety_settings
    )


    if msg.type == MessageType.TEXT:
        return msg.text
    elif msg.type == MessageType.IMAGE:
        image_b64 = base64.b64encode(msg.image.download(path=os.path.join(os.getenv("ROOT_DIR"), "temp"),in_memory=True)).decode("utf-8")
        Ans = llm.invoke([
            HumanMessage(
                content=[
                    {"type": "text", "text": "Give me a Detail summary of the image in order to help a blind person to see"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
                    ]
                ),
            ])
        return Ans.content
    elif msg.type == MessageType.VIDEO:
        video_b64 = base64.b64encode(msg.video.download(path=os.path.join(os.getenv("ROOT_DIR"), "temp"),in_memory=True)).decode("utf-8")
        Ans = llm.invoke(
            [
                HumanMessage(
                    content=[
                        {"type": "text", "text": "Give me a Summary of video, for a blind person to be able to understand"},
                        {"type": "media", "mime_type": "video/mp4", "data": video_b64},
                    ]
                ),
            ]
        )
        return Ans.content
    elif msg.type == MessageType.AUDIO:
        audio_b64 = base64.b64encode(msg.audio.download(path=os.path.join(os.getenv("ROOT_DIR"), "temp"),in_memory=True)).decode("utf-8")
        Ans = llm.invoke(
            [
                HumanMessage(
                    content=[
                        {"type": "text", "text": "Give me a Summary of the audio, for a deaf person to be able to understand for what it is"},
                        {"type": "media", "mime_type": "audio/mp3", "data": audio_b64},
                    ]
                ),
            ]
        )
        return Ans.content
    elif msg.type == MessageType.LOCATION:
        return f"name of the location: {msg.location.name}, address of the location: {msg.location.address}"
    elif msg.type == MessageType.CONTACTS:
        return ", ".join([f"name: {contact.name.formatted_name}, phone_number/s: {contact.phones}" for contact in msg.contacts])
    elif msg.type == MessageType.ORDER:
        text = f"Order for {len(msg.order.products)} productsj, which total price is {msg.order.total_price}"
        text+= f"\nThe user message is: {msg.order.text}" if msg.order.text else ""
        return text
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

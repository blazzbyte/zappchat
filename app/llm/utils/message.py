import os
import base64
from pywa.types import Message, MessageType

from langchain_google_vertexai import ChatVertexAI, HarmBlockThreshold, HarmCategory
from langchain_core.messages import HumanMessage

from app.core import config


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
        model_name="gemini-1.5-pro-preview-0514",
        temperature=0.0,
        max_retries=5,
        max_tokens=1024,
        project=config.get_google_project_id(),
        location="asia-southeast1",
        safety_settings=safety_settings
    )

    media_dir = config.get_media_dir()

    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

    media_path = os.path.join(media_dir, "temp")

    if msg.type == MessageType.TEXT:
        return msg.text
    elif msg.type == MessageType.IMAGE:
        image_b64 = base64.b64encode(msg.image.download(
            path=media_path, in_memory=True)).decode("utf-8")
        Ans = llm.invoke([
            HumanMessage(
                content=[
                    {"type": "text", "text": "Give me a Detail summary of the image in order to help a blind person to see"},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpeg;base64,{image_b64}"}},
                ]
            ),
        ])
        return Ans.content
    elif msg.type == MessageType.VIDEO:
        video_b64 = base64.b64encode(msg.video.download(
            path=media_path, in_memory=True)).decode("utf-8")
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
        audio_b64 = base64.b64encode(msg.audio.download(
            path=media_path, in_memory=True)).decode("utf-8")
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
        text += f"\nThe user message is: {msg.order.text}" if msg.order.text else ""
        return text
    else:
        return None

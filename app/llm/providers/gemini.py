"""Module for initializing the Gemini LLM with fallback models."""
import os
from typing import List
from langchain_google_vertexai import ChatVertexAI, HarmBlockThreshold, HarmCategory

from app.core import config

def gemini_llm() -> ChatVertexAI:
    """
    Returns a Gemini LLM with fallback models.

    This function creates a ChatVertexAI instance configured with safety settings
    and fallback models across different Google Cloud regions.
    The fallback mechanism ensures the LLM remains accessible even if the primary
    region experiences issues.

    Returns:
        ChatVertexAI: An instance of the ChatVertexAI class configured with fallbacks.
    """

    locations: List[str] = [
        "northamerica-northeast1",
        "southamerica-east1",
        "us-east1",
        "us-east4",
        "us-east5",
        "us-south1",
        "us-west1",
        "us-west4",
        "asia-east1",
        "asia-east2",
        "asia-northeast1",
        "asia-northeast3",
        "asia-south1",
        "asia-southeast1",
        "australia-southeast1",
        "europe-central2",
        "europe-north1",
        "europe-southwest1",
        "europe-west1",
        "europe-west2",
        "europe-west3",
        "europe-west4",
        "europe-west6",
        "europe-west8",
        "europe-west9",
        "me-central1",
        "me-central2",
        "me-west1",
    ]

    safety_settings = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }

    project_id = config.get_google_project_id()

    parameters = {
        "model_name": "gemini-1.5-pro-preview-0514",
        "temperature": 0.0,
        "max_retries": 1,
        "max_tokens": 512,
        "project": project_id,
        "location": "us-central1",
        "safety_settings": safety_settings
    }

    gemini = ChatVertexAI(**parameters)

    fallbacks = []
    for location in locations:
        parameters.update({"location": location})
        fallbacks.append(ChatVertexAI(**parameters))

    gemini.with_fallbacks(fallbacks=fallbacks)

    return gemini
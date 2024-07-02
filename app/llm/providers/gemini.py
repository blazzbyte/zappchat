import os
from langchain.llms.openai import BaseOpenAI

from app.core import config


def gemini_llm() -> BaseOpenAI:
    """
    Returns a Gemini LLM with fallback models.

    This function creates an OpenAI model with safety settings and fallback models
    from the Gemini model list.

    Returns:
        BaseOpenAI: The Gemini LLM with fallback models.
    """

    model_list = [
        "gemini-1.5-flash-preview-0514",
        "gemini-1.5-pro-latest",
        "gemini-1.5-flash",
        "gemini-1.5-pro-1",
        "gemini-1.5-flash-1"
    ]

    api_key = config.get_litellm_api_key()  # Master Key from LiteLLM
    api_base = config.get_litellm_api_base_url()

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH",
        },
    ]

    parameters = {
        # Put public_name from model display in LiteLLM Proxy
        "model_name": "gemini-1.5-pro-preview-0514-0",
        "openai_api_base": api_base,
        "openai_api_key": api_key,
        "model_kwargs": {
            "safety_settings": safety_settings,
            # Put public_name from model display in LiteLLM Proxy
            "engine": 'gemini-1.5-pro-preview-0514-0',
            "fallbacks": model_list
        }
    }

    gemini = BaseOpenAI(**parameters)

    return gemini
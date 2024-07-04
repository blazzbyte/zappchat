import os
from typing import List
from langchain.chains.llm_math.base import LLMMathChain
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools import Tool
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_google_vertexai import VertexAI
from langchain_google_vertexai import HarmBlockThreshold, HarmCategory
from langchain.callbacks.manager import CallbackManagerForRetrieverRun

from app.core import config
from app.llm.stores import supabase_store

def basic_tools() -> List[Tool]:
    safety_settings = {
        HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }

    llm = VertexAI(model_name="gemini-1.0-pro-001",temperature=0, project=config.get_google_project_id or os.getenv("VERTEXAI_PROJECT"), safety_settings=safety_settings)

    math_tool = Tool(
            name="Calculator",
            description="Useful for when you need to answer questions about math.",
            func=LLMMathChain.from_llm(llm=llm).run,
            coroutine=LLMMathChain.from_llm(llm=llm).arun,
        )

    metadata_field_info = [
        AttributeInfo(
            name="name",
            description="the name of the product",
            type="string",
        ),
        AttributeInfo(
            name="price",
            description="the price of the product in $us or USD",
            type="integer",
        ),
        AttributeInfo(
            name="category",
            description="what type of accessory or product the user seek from the adidas brand",
            type="string",
        ),
    ]
    document_content_description = "Brief description of the Adidas product in a shopping online store bussiness"

    retriever = SelfQueryRetriever.from_llm(
        llm,
        supabase_store.store(),
        document_content_description,
        metadata_field_info,
    )

    retrv_tool = create_retriever_tool(
    retriever,
    "search_products_from_shopping_website",
    "Searches and returns information about products from a shopping website from the adidas brand.",
    )

    tools: List[Tool]=[math_tool, retrv_tool]
    return tools
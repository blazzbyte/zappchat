from typing import List

from langchain_core.tools import Tool

from langchain.chains.llm_math.base import LLMMathChain
from langchain.chains.query_constructor.base import AttributeInfo

from .retriever_tool import retriever_tool
from langchain.retrievers.self_query.base import SelfQueryRetriever

from langchain_google_vertexai import VertexAI
from langchain_google_vertexai import HarmBlockThreshold, HarmCategory

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

    project_id = config.get_google_project_id()

    llm = VertexAI(model_name="gemini-1.0-pro-001", temperature=0,
                   project=project_id, safety_settings=safety_settings)

    ## ** Math Tool ** ##
    math_tool = Tool(
        name="Calculator",
        description="Useful for when you need to answer questions about math.",
        func=LLMMathChain.from_llm(llm=llm).run,
        coroutine=LLMMathChain.from_llm(llm=llm).arun,
    )

    ## ** Query Retriever ** ##
    metadata_field_info = [
        AttributeInfo(
            name="name",
            description="Product Name",
            type="string",
        ),
        AttributeInfo(
            name="price",
            description="Product price in USD",
            type="integer",
        ),
        AttributeInfo(
            name="category",
            description="Clothes collection",
            type="string"
        ),
    ]

    document_description = "Products from a clothing store"

    retriever = SelfQueryRetriever.from_llm(
        llm,
        supabase_store.store(),
        document_description,
        metadata_field_info
    )

    retrv_tool = retriever_tool(
        retriever,
        "search_for_clothing_store_products",
        "Searches and returns information about products from the clothing store.",
    )

    ## ** Tools ** ##
    tools: List[Tool] = [math_tool, retrv_tool]

    return tools

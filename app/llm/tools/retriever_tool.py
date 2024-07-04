from typing import Optional
from functools import partial

from langchain_core.prompts import format_document, aformat_document, BasePromptTemplate, PromptTemplate
from langchain_core.retrievers import BaseRetriever

from langchain_core.tools import Tool, RetrieverInput


def _get_relevant_documents(
    query: str,
    retriever: BaseRetriever,
    document_prompt: BasePromptTemplate,
    document_separator: str,
) -> str:
    docs = retriever.invoke(query)
    return {
        "type": "product",
        "metadatas": [doc["metadata"] for doc in docs],
        "text": document_separator.join(
            format_document(doc, document_prompt) for doc in docs
        )
    }


async def _aget_relevant_documents(
    query: str,
    retriever: BaseRetriever,
    document_prompt: BasePromptTemplate,
    document_separator: str
) -> str:
    docs = await retriever.ainvoke(query)
    return {
        "type": "product",
        "metadatas": [doc["metadata"] for doc in docs],
        "text": document_separator.join(
            [await aformat_document(doc, document_prompt) for doc in docs]
        )
    }


def retriever_tool(
    retriever: BaseRetriever,
    name: str,
    description: str,
    *,
    document_prompt: Optional[BasePromptTemplate] = None,
    document_separator: str = "\n\n",
) -> Tool:
    """Create a tool to do retrieval of documents.

    Args:
        retriever: The retriever to use for the retrieval
        name: The name for the tool. This will be passed to the language model,
            so should be unique and somewhat descriptive.
        description: The description for the tool. This will be passed to the language
            model, so should be descriptive.

    Returns:
        Tool class to pass to an agent
    """
    document_prompt = document_prompt or PromptTemplate.from_template(
        "{page_content}")
    func = partial(
        _get_relevant_documents,
        retriever=retriever,
        document_prompt=document_prompt,
        document_separator=document_separator,
    )
    afunc = partial(
        _aget_relevant_documents,
        retriever=retriever,
        document_prompt=document_prompt,
        document_separator=document_separator,
    )

    return Tool(
        name=name,
        description=description,
        func=func,
        coroutine=afunc,
        args_schema=RetrieverInput,
        return_direct=True
    )

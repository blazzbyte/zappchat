from typing import List, Union
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain_core.runnables import RunnableLambda
from langchain.memory import ConversationBufferMemory
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor

from app.llm.utils.helpers import _format_chat_history, prompting
from app.llm.providers.gemini import gemini_llm
from app.llm.tools.tool import basic_tools

def Agent(tooles:Union[List[Tool]|Tool]) -> AgentExecutor:

    llm = gemini_llm()

    tools = basic_tools()

    if isinstance(tooles, Tool):
        tools.append(tooles)
    else:
        tools = tools + tooles

    llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

    agent = (
        {
            "input": lambda x: x["input"],
            "datehour": lambda x: x["datehour"],
            "chat_history": lambda x: _format_chat_history(x["chat_history"]),
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | RunnableLambda(prompting)
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    memory = ConversationBufferMemory(input_key='input', return_messages=True, memory_key="chat_history", output_key="output")

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        return_intermediate_steps=True,
        handle_parsing_errors=True
    )
    return agent_executor
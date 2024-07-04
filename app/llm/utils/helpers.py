from typing import List, Tuple
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompt_values import ChatPromptValue
from langchain_core.prompts import ChatPromptTemplate

from app.llm.prompts.agent_prompt import prompt

def _format_chat_history(chat_history: List[Tuple[str, str]]) -> List[HumanMessage | AIMessage]:
    """
    Format chat history into a list of HumanMessage and AIMessage objects.

    Args:
        chat_history (List[Tuple[str, str]]): List of tuples containing dialogue turns.

    Returns:
        List[HumanMessage | AIMessage]: Formatted list of HumanMessage and AIMessage objects.
    """
    buffer = []
    for dialogue_turn in chat_history:
        if isinstance(dialogue_turn, tuple) and len(dialogue_turn) == 2:
            human_message, ai_message = dialogue_turn
            buffer.append(HumanMessage(content=human_message))
            buffer.append(AIMessage(content=ai_message))
        elif isinstance(dialogue_turn, (HumanMessage, AIMessage)):
            buffer.append(dialogue_turn)
        else:
            print(f"Unexpected dialogue turn format: {dialogue_turn}")
    return buffer

def prompting(_data, prompt: ChatPromptTemplate = prompt) -> ChatPromptValue:
    """
    Generate a ChatPromptValue object with formatted input data.

    Args:
        _data (dict): Input data dictionary.
        prompt (ChatPromptTemplate, optional): Default prompt template. Defaults to prompt.

    Returns:
        ChatPromptValue: Formatted ChatPromptValue object.
    """
    instruction = prompt.format_prompt(**_data)
    input_data = _data.get("input", "")
    required_keywords = ["'image_url'", "{", "}", "'text'", "'type'"]

    # Check if all required keywords are present in the input data
    if all(keyword in input_data for keyword in required_keywords):
        try:
            # Find the index of the specific HumanMessage
            index = next(i for i, msg in enumerate(instruction.messages) if isinstance(msg, HumanMessage) and msg.content == str(input_data))

            # Update the content of the message at the found index
            instruction.messages[index].content = input_data
        except Exception as e:
            print(f"An error has occurred: {e}")

    return instruction
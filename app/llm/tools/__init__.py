from typing import List
from langchain_core.tools import Tool

from .basic_tools import basic_tools
from .map_tool import map_tool

tools: List[Tool] = basic_tools().append(map_tool)

__all__ = ['tools']

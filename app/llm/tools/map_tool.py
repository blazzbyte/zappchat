from langchain_core.tools import StructuredTool


def get_location():
    return {
        "type": "location",
        "default": True
    }


map_tool: StructuredTool = StructuredTool.from_function(
    func=get_location,
    name="Location",
    description="Gets the maps location of the store, when the user ask for it",
    return_direct=True
)

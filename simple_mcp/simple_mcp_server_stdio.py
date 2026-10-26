import logging
import sys

logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler(stream=sys.stderr))
# logger.addHandler(logging.FileHandler("file.log", mode="a"))
logger.setLevel(logging.DEBUG)




import httpx2
from mcp.server import MCPServer

mcp = MCPServer("Simple MCP Server")

@mcp.tool()
def get_greeting(name: str, salutation: str) -> str:
    """The tool that returns a greeting message."""
    logger.info(f"Get Greeting called with name: {name}")
    return f"{salutation}, {name}! Hai, All good!"


if __name__ == "__main__":
    mcp.run(transport="stdio")

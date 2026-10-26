import logging

logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

logger.info("Greet me with a morning joke")

# print("Greet me with a morning joke")


import httpx2
from mcp.server import MCPServer

mcp = MCPServer("Simple MCP Server")

@mcp.tool()
def get_greeting(name: str, salutation: str) -> str:
    """The tool that returns a greeting message."""
    logger.info(f"Get Greeting called with name: {name}")
    return f"{salutation}, {name}! Hai, All good!"


if __name__ == "__main__":
    mcp.run(host="127.0.0.1", port=8000, transport="streamable-http")

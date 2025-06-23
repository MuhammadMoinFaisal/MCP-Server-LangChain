from mcp.server.fastmcp import FastMCP

#Server Name
mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """Weather forecast for a given location"""
    return "The weather in California is Sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
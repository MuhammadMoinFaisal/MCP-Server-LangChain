from mcp.server.fastmcp import FastMCP

#Server name
mcp = FastMCP("Math")

#Create first tool inside the MCP Server
@mcp.tool()
def add(a:int, b:int) -> int:
    """_summary_
    This tool adds two numbers together
    """
    return a+b

#Create Second tool inside the MCP Server
@mcp.tool()
def multiply(a:int, b:int) -> int:
    """
    This tool multiplies two numbers together
    """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")
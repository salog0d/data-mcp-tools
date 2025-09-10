from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AWS Athena Tools")

@mcp.tool()
def query_db()->str:
    return
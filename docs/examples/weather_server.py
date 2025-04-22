# weather_server.py
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location. location is a string like "Beijing" "New York".
    """
    print(f"Fetching weather for {location}")
    return f"{location} is sunny with a high of 72F"

if __name__ == "__main__":
    mcp.run(transport="sse")  # HTTP with SSE（Server-Sent Events） 适用于远程通信 
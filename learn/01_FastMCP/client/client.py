import asyncio
from fastmcp import Client
from pprint import pprint

# client = Client("../server/my_server.py")
client = Client("../server/server.py")


async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        pprint(f"Result.data: {result.data}")
        result = await client.call_tool("add", {"a": 5, "b": 10})
        # pprint(result)
        pprint(f"Result.data: {result.data}")


asyncio.run(call_tool("Ford"))

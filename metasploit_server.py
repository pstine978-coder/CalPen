#!/usr/bin/env python3

import os
import sys
from pymetasploit3.msfrpc import MsfRpcClient
from mcp.server import Server
from mcp.types import Tool, TextContent
import asyncio

# Environment variables for MSF connection
MSF_PASSWORD = os.getenv('MSF_PASSWORD', 'yourpassword')
MSF_SERVER = os.getenv('MSF_SERVER', '127.0.0.1')
MSF_PORT = int(os.getenv('MSF_PORT', '55553'))
MSF_SSL = os.getenv('MSF_SSL', 'False').lower() == 'true'

server = Server("metasploit-server")

def get_client():
    try:
        client = MsfRpcClient(password=MSF_PASSWORD, server=MSF_SERVER, port=MSF_PORT, ssl=MSF_SSL)
        return client
    except Exception as e:
        raise Exception(f"Failed to connect to MSF: {str(e)}")

async def handle_list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_msf_version",
            description="Get the version of the connected Metasploit Framework instance",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="list_msf_modules",
            description="List Metasploit modules of a specific type",
            inputSchema={
                "type": "object",
                "properties": {
                    "module_type": {
                        "type": "string",
                        "enum": ["exploit", "auxiliary", "post", "payload", "encoder", "nop"],
                        "description": "Type of modules to list"
                    }
                },
                "required": ["module_type"]
            }
        ),
        Tool(
            name="connect_msf",
            description="Test connection to Metasploit RPC server",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]

async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        if name == "get_msf_version":
            client = get_client()
            version = client.core.version
            return [TextContent(type="text", text=f"Metasploit Version: {version}")]

        elif name == "list_msf_modules":
            module_type = arguments.get("module_type")
            if not module_type:
                return [TextContent(type="text", text="Error: module_type is required")]

            client = get_client()
            modules = client.modules.list(module_type)
            module_list = "\n".join(modules) if modules else "No modules found"
            return [TextContent(type="text", text=f"{module_type.capitalize()} modules:\n{module_list}")]

        elif name == "connect_msf":
            client = get_client()
            # Try to get version to test connection
            version = client.core.version
            return [TextContent(type="text", text=f"Successfully connected to Metasploit RPC. Version: {version}")]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

server.list_tools = handle_list_tools
server.call_tool = handle_call_tool

async def main():
    # Import here to avoid issues if not available
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())

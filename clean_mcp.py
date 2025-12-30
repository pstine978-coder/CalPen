#!/usr/bin/env python3
"""Clean up mcp.json to remove invalid MCP server configurations"""

import json

def main():
    try:
        with open('mcp.json', 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading mcp.json: {e}")
        return

    # Valid tool names that have working MCP packages
    valid_tools = [
        "Nmap Scanner",
        "Hydra",
        "SQLMap",
        "Nuclei Scanner",
        "FFUF Fuzzer",
        "Masscan",
        "John the Ripper",
        "Hashcat"
    ]

    original_count = len(config.get('servers', []))
    config['servers'] = [server for server in config.get('servers', []) if server.get('name') in valid_tools]
    new_count = len(config['servers'])

    with open('mcp.json', 'w') as f:
        json.dump(config, f, indent=2)

    print(f"Cleaned mcp.json: removed {original_count - new_count} invalid entries")
    print(f"Remaining tools: {new_count}")

if __name__ == "__main__":
    main()

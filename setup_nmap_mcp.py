#!/usr/bin/env python3
"""
Script to automatically configure Nmap MCP server for PentestAgent
"""

import json
import os
import shutil
from pathlib import Path

def find_nmap_path():
    """Find the nmap executable path"""
    try:
        # Try to find nmap using which
        nmap_path = shutil.which("nmap")
        if nmap_path and os.path.exists(nmap_path):
            return nmap_path
    except Exception:
        pass

    # Fallback to common locations
    common_paths = [
        "/usr/bin/nmap",
        "/usr/local/bin/nmap",
        "/opt/homebrew/bin/nmap",  # macOS with Homebrew
        "/snap/bin/nmap",
        "/usr/sbin/nmap"
    ]

    for path in common_paths:
        if os.path.exists(path):
            return path

    return None

def main():
    print("=" * 60)
    print("Setting up Nmap MCP Server for PentestAgent")
    print("=" * 60)

    # Find nmap
    nmap_path = find_nmap_path()
    if not nmap_path:
        print("❌ ERROR: nmap not found on the system!")
        print("Please install nmap first:")
        print("  sudo apt update && sudo apt install nmap")
        return False

    print(f"✅ Found nmap at: {nmap_path}")

    # Load existing mcp.json or create new one
    mcp_config_file = "mcp.json"
    if os.path.exists(mcp_config_file):
        try:
            with open(mcp_config_file, 'r') as f:
                mcp_config = json.load(f)
            print("✅ Loaded existing mcp.json configuration")
        except Exception as e:
            print(f"❌ Error loading mcp.json: {e}")
            mcp_config = {"servers": []}
    else:
        mcp_config = {"servers": []}
        print("📄 Created new mcp.json configuration")

    # Check if Nmap is already configured
    existing_servers = mcp_config.get("servers", [])
    nmap_server = None
    for server in existing_servers:
        if server.get("name") == "Nmap Scanner":
            nmap_server = server
            break

    if nmap_server:
        print("⚠️  Nmap Scanner already configured. Updating configuration...")
    else:
        print("➕ Adding Nmap Scanner configuration...")

    # Nmap MCP server configuration
    nmap_config = {
        "name": "Nmap Scanner",
        "params": {
            "command": "npx",
            "args": ["-y", "gc-nmap-mcp"],
            "env": {
                "NMAP_PATH": nmap_path
            }
        },
        "cache_tools_list": True
    }

    # Add or update the server configuration
    if nmap_server:
        # Update existing
        nmap_server.update(nmap_config)
    else:
        # Add new
        mcp_config["servers"].append(nmap_config)

    # Save the configuration
    try:
        with open(mcp_config_file, 'w') as f:
            json.dump(mcp_config, f, indent=2)
        print("✅ Successfully saved mcp.json configuration")
        print(f"📊 Total configured servers: {len(mcp_config['servers'])}")
        return True
    except Exception as e:
        print(f"❌ Error saving mcp.json: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 Nmap MCP Server setup complete!")
        print("You can now run the PentestAgent with Nmap scanning capabilities.")
        print("\nTo test:")
        print("  python main.py")
        print("  Select 'Configure or connect MCP tools' when prompted")
        print("  Choose 'Nmap Scanner' from the available tools")
    else:
        print("\n❌ Nmap MCP Server setup failed!")
        exit(1)

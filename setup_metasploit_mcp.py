#!/usr/bin/env python3
"""
Script to set up MetasploitMCP server integration with PentestAgent
"""

import json
import os
import subprocess
import shutil
from pathlib import Path

def check_metasploit():
    """Check if Metasploit is properly installed"""
    try:
        # Check for required Metasploit components
        components = ['msfconsole', 'msfrpcd', 'msfrpc']
        missing = []
        for component in components:
            if not shutil.which(component):
                missing.append(component)

        if missing:
            print(f"❌ Missing Metasploit components: {', '.join(missing)}")
            print("Please install Metasploit Framework first:")
            print("  sudo apt update && sudo apt install metasploit-framework")
            return False

        print("✅ Metasploit Framework is installed")
        return True
    except Exception as e:
        print(f"❌ Error checking Metasploit: {e}")
        return False

def check_metasploit_rpc():
    """Check if Metasploit RPC daemon is running"""
    try:
        result = subprocess.run(
            ['pgrep', '-f', 'msfrpcd'],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False

def start_metasploit_rpc(password="msf", host="127.0.0.1", port="55553"):
    """Start the Metasploit RPC daemon"""
    try:
        print(f"Starting Metasploit RPC daemon on {host}:{port}...")

        # Check if already running
        if check_metasploit_rpc():
            print("✅ Metasploit RPC daemon is already running")
            return True

        # Start msfrpcd in background
        cmd = [
            'msfrpcd',
            '-P', password,  # Password
            '-S',            # SSL enabled
            '-a', host,      # Bind address
            '-p', port       # Port
        ]

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            preexec_fn=os.setsid  # Create new process group
        )

        # Wait a moment for startup
        import time
        time.sleep(3)

        # Check if it's running
        if check_metasploit_rpc():
            print("✅ Metasploit RPC daemon started successfully")
            return True
        else:
            print("❌ Failed to start Metasploit RPC daemon")
            return False

    except Exception as e:
        print(f"❌ Error starting Metasploit RPC: {e}")
        return False

def setup_metasploit_mcp():
    """Set up the Metasploit MCP server integration"""
    print("=" * 60)
    print("Setting up Metasploit MCP Server Integration")
    print("=" * 60)

    # Check Metasploit installation
    if not check_metasploit():
        return False

    # Start Metasploit RPC if needed
    if not start_metasploit_rpc():
        return False

    # Install MetasploitMCP dependencies
    metasploit_mcp_path = "/home/kali/Desktop/MetasploitMCP"
    if not os.path.exists(metasploit_mcp_path):
        print(f"❌ MetasploitMCP directory not found at {metasploit_mcp_path}")
        return False

    print("Installing MetasploitMCP dependencies...")
    try:
        # Create virtual environment for MetasploitMCP
        venv_path = os.path.join(metasploit_mcp_path, "venv")
        if not os.path.exists(venv_path):
            subprocess.run(['python3', '-m', 'venv', venv_path], check=True)

        # Install requirements
        pip_cmd = [os.path.join(venv_path, 'bin', 'pip'), 'install', '-r',
                  os.path.join(metasploit_mcp_path, 'requirements.txt')]
        subprocess.run(pip_cmd, check=True)

        print("✅ MetasploitMCP dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install MetasploitMCP dependencies: {e}")
        return False

    # Configure environment variables for MetasploitMCP
    env_vars = {
        "MSF_PASSWORD": "msf",
        "MSF_SERVER": "127.0.0.1",
        "MSF_PORT": "55553",
        "MSF_SSL": "true",
        "PAYLOAD_SAVE_DIR": "/home/kali/Desktop/MetasploitMCP/payloads"
    }

    # Create payloads directory
    payloads_dir = env_vars["PAYLOAD_SAVE_DIR"]
    os.makedirs(payloads_dir, exist_ok=True)

    # Configure MCP server in PentestAgent's mcp.json
    mcp_config_file = "mcp.json"
    if os.path.exists(mcp_config_file):
        try:
            with open(mcp_config_file, 'r') as f:
                mcp_config = json.load(f)
        except Exception as e:
            print(f"❌ Error loading mcp.json: {e}")
            mcp_config = {"servers": []}
    else:
        mcp_config = {"servers": []}

    # Check if Metasploit is already configured
    existing_servers = mcp_config.get("servers", [])
    metasploit_server = None
    for server in existing_servers:
        if server.get("name") == "Metasploit":
            metasploit_server = server
            break

    if metasploit_server:
        print("⚠️  Metasploit MCP server already configured. Updating...")
    else:
        print("➕ Adding Metasploit MCP server configuration...")

    # Metasploit MCP server configuration
    metasploit_config = {
        "name": "Metasploit",
        "params": {
            "command": "python3",
            "args": [os.path.join(metasploit_mcp_path, "MetasploitMCP.py"), "--transport", "stdio"],
            "env": env_vars
        },
        "cache_tools_list": True
    }

    # Add or update the server configuration
    if metasploit_server:
        # Update existing
        metasploit_server.update(metasploit_config)
    else:
        # Add new
        mcp_config["servers"].append(metasploit_config)

    # Save the configuration
    try:
        with open(mcp_config_file, 'w') as f:
            json.dump(mcp_config, f, indent=2)
        print("✅ Successfully updated mcp.json with Metasploit MCP server")
        print(f"📊 Total configured servers: {len(mcp_config['servers'])}")
        return True
    except Exception as e:
        print(f"❌ Error saving mcp.json: {e}")
        return False

def test_metasploit_connection():
    """Test the Metasploit RPC connection"""
    try:
        print("\nTesting Metasploit RPC connection...")
        result = subprocess.run(
            ['msfrpc', '-P', 'msf', '-S', '-a', '127.0.0.1', '-p', '55553', 'core.version'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0 and 'version' in result.stdout.lower():
            print("✅ Metasploit RPC connection test successful")
            return True
        else:
            print(f"❌ Metasploit RPC test failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error testing Metasploit RPC: {e}")
        return False

def main():
    print("=" * 60)
    print("Metasploit MCP Server Setup for PentestAgent")
    print("=" * 60)

    success = setup_metasploit_mcp()

    if success:
        # Test the connection
        if test_metasploit_connection():
            print("\n🎉 Metasploit MCP Server setup complete!")
            print("\nMetasploit MCP Server provides:")
            print("• List and search exploits")
            print("• List and search payloads")
            print("• Run exploits with custom options")
            print("• Generate payloads")
            print("• Manage active sessions")
            print("• Start/stop listeners")
            print("• Session command execution")
            print("\nTo use Metasploit tools:")
            print("  python main.py")
            print("  Select MCP tools and choose 'Metasploit'")
            print("\nExample commands:")
            print("  'list_exploits(\"ms17_010\")'")
            print("  'run_exploit(\"exploit/windows/smb/ms17_010_eternalblue\", {\"RHOSTS\": \"192.168.1.100\"})'")
            print("  'list_active_sessions()'")
        else:
            print("\n⚠️  Setup completed but connection test failed")
            print("Metasploit RPC may need manual configuration")
    else:
        print("\n❌ Metasploit MCP Server setup failed!")
        exit(1)

if __name__ == "__main__":
    main()

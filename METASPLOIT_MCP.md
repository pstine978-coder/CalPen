# Metasploit MCP Integration

CalPen now includes full Metasploit Framework integration through the MCP protocol.

## Features

### Module Information
- **list_exploits**: Search and list available Metasploit exploit modules
- **list_payloads**: Search and list available payload modules with filtering

### Exploitation Workflow
- **run_exploit**: Configure and execute exploits against targets
- **run_auxiliary_module**: Run any Metasploit auxiliary module
- **run_post_module**: Execute post-exploitation modules

### Payload Generation
- **generate_payload**: Generate payload files using Metasploit RPC

### Session Management
- **list_active_sessions**: Show current Metasploit sessions
- **send_session_command**: Run commands in active shell/Meterpreter sessions
- **terminate_session**: End active sessions

### Handler Management
- **list_listeners**: Show all active handlers and background jobs
- **start_listener**: Create new multi/handler to receive connections
- **stop_job**: Terminate running jobs or handlers

---

## Setup

### Prerequisites

1. **Metasploit Framework** must be installed:
```bash
sudo apt update
sudo apt install metasploit-framework
```

2. **Run the setup script**:
```bash
cd CalPen
bash setup_metasploit.sh
```

This will:
- Create a virtual environment for Metasploit MCP
- Install required dependencies
- Create configuration files
- Set up startup scripts

---

## Usage

### Step 1: Start msfrpcd

In a **separate terminal**, start the Metasploit RPC daemon:

```bash
cd CalPen/mcp_servers/metasploit
./start_msfrpcd.sh
```

**Or manually:**
```bash
msfrpcd -P calpen123 -S -p 55553 -a 127.0.0.1
```

Keep this terminal open while using CalPen.

### Step 2: Start CalPen

In your main terminal:

```bash
cd CalPen
source venv/bin/activate
python3 main.py
```

The Metasploit MCP server will automatically connect when CalPen starts.

---

## Configuration

Configuration is stored in `mcp_servers/metasploit/msf_config.env`:

```bash
MSF_PASSWORD=calpen123      # RPC password
MSF_SERVER=127.0.0.1        # RPC server address
MSF_PORT=55553              # RPC port
MSF_SSL=false               # Use SSL (true/false)
PAYLOAD_SAVE_DIR=./payloads # Where to save generated payloads
```

To change the password:
1. Edit `msf_config.env`
2. Update `mcp.json` (MSF_PASSWORD env variable)
3. Restart msfrpcd with new password

---

## Example Usage

### Interactive Mode

```bash
python3 main.py
# Select: 1 (Interactive Mode)

# List exploits
> list exploits for windows smb

# Run exploit
> run exploit windows/smb/ms17_010_eternalblue against 192.168.1.100

# List sessions
> list active metasploit sessions

# Send command to session
> send command to session 1: sysinfo
```

### Agent Mode

```bash
python3 main.py
# Select: 3 (Agent Mode)

# Goal: "Exploit the target and establish a Meterpreter session"
# Target: 192.168.1.100
# Let AI use Metasploit autonomously
```

---

## Troubleshooting

### "Connection refused" or "Cannot connect to msfrpcd"

**Solution:** Make sure msfrpcd is running:
```bash
ps aux | grep msfrpcd
```

If not running, start it:
```bash
cd mcp_servers/metasploit
./start_msfrpcd.sh
```

### "Authentication failed"

**Solution:** Password mismatch. Check:
1. Password in `msf_config.env`
2. Password in `mcp.json` (MSF_PASSWORD)
3. Password used to start msfrpcd

All three must match.

### "Module not found"

**Solution:** Update Metasploit database:
```bash
msfconsole
msf6 > msfupdate
msf6 > exit
```

### "Permission denied" for payloads directory

**Solution:** Create payloads directory:
```bash
mkdir -p mcp_servers/metasploit/payloads
chmod 755 mcp_servers/metasploit/payloads
```

---

## Advanced Configuration

### Remote msfrpcd

To connect to a remote Metasploit instance:

1. Edit `mcp_servers/metasploit/msf_config.env`:
```bash
MSF_SERVER=192.168.1.50  # Remote IP
MSF_PORT=55553
MSF_SSL=true             # Enable SSL for remote
```

2. Update `mcp.json` with the same values

3. Restart CalPen

### Custom Port

To use a different RPC port:

1. Start msfrpcd with custom port:
```bash
msfrpcd -P calpen123 -S -p 55554 -a 127.0.0.1
```

2. Update `msf_config.env`:
```bash
MSF_PORT=55554
```

3. Update `mcp.json` MSF_PORT

---

## Security Notes

⚠️ **Important**:
- msfrpcd password is stored in plain text
- Only bind to 127.0.0.1 unless you need remote access
- Use SSL (`-S` flag) for remote connections
- Change default password in production
- Payloads are saved locally and may contain sensitive data

---

## Credits

Metasploit MCP Server by [GH05TCREW](https://github.com/GH05TCREW/MetasploitMCP)

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `bash setup_metasploit.sh` | Initial setup |
| `./start_msfrpcd.sh` | Start RPC daemon |
| `./start_mcp.sh` | Start MCP server (manual) |
| `ps aux \| grep msfrpcd` | Check if running |
| `pkill msfrpcd` | Stop RPC daemon |

---

**Now you have full Metasploit integration in CalPen!** 🎯

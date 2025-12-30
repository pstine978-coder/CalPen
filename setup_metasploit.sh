#!/bin/bash

# Metasploit MCP Setup Script for CalPen
# This script sets up the Metasploit MCP server integration

set -e

echo "======================================"
echo "  Metasploit MCP Setup"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if Metasploit is installed
echo -e "${GREEN}[1/6]${NC} Checking Metasploit Framework..."
if ! command -v msfconsole &> /dev/null; then
    echo -e "${RED}Error: Metasploit Framework not found${NC}"
    echo "Please install Metasploit first:"
    echo "  sudo apt update && sudo apt install metasploit-framework"
    exit 1
fi
echo -e "${GREEN}✅ Metasploit Framework found${NC}"

# Check if msfrpcd is available
echo -e "${GREEN}[2/6]${NC} Checking msfrpcd..."
if ! command -v msfrpcd &> /dev/null; then
    echo -e "${RED}Error: msfrpcd not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ msfrpcd found${NC}"

# Create virtual environment for Metasploit MCP
echo -e "${GREEN}[3/6]${NC} Setting up Metasploit MCP virtual environment..."
cd mcp_servers/metasploit
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo -e "${GREEN}[4/6]${NC} Installing Metasploit MCP dependencies..."
pip install --upgrade pip --quiet
pip install -r requirements-metasploit.txt --quiet
echo -e "${GREEN}✅ Dependencies installed${NC}"

# Create configuration file
echo -e "${GREEN}[5/6]${NC} Creating configuration..."
cat > msf_config.env << 'EOF'
# Metasploit RPC Configuration
MSF_PASSWORD=calpen123
MSF_SERVER=127.0.0.1
MSF_PORT=55553
MSF_SSL=false
PAYLOAD_SAVE_DIR=./payloads
EOF

mkdir -p payloads
echo -e "${GREEN}✅ Configuration created${NC}"

# Create startup script
echo -e "${GREEN}[6/6]${NC} Creating startup scripts..."

cat > start_msfrpcd.sh << 'EOF'
#!/bin/bash
# Start msfrpcd (Metasploit RPC daemon)
echo "Starting msfrpcd..."
msfrpcd -P calpen123 -S -p 55553 -a 127.0.0.1
EOF
chmod +x start_msfrpcd.sh

cat > start_mcp.sh << 'EOF'
#!/bin/bash
# Start Metasploit MCP Server
source venv/bin/activate
source msf_config.env
python3 MetasploitMCP.py --transport stdio
EOF
chmod +x start_mcp.sh

cd ../..

echo ""
echo -e "${GREEN}======================================"
echo "  ✅ Metasploit MCP Setup Complete!"
echo "======================================${NC}"
echo ""
echo "Next Steps:"
echo ""
echo "1. Start msfrpcd (in a separate terminal):"
echo "   cd mcp_servers/metasploit"
echo "   ./start_msfrpcd.sh"
echo ""
echo "2. The MCP server will be auto-started by CalPen"
echo "   Or manually start it:"
echo "   cd mcp_servers/metasploit"
echo "   ./start_mcp.sh"
echo ""
echo "3. Run CalPen:"
echo "   source venv/bin/activate"
echo "   python3 main.py"
echo ""
echo -e "${YELLOW}Note: msfrpcd must be running before starting CalPen${NC}"
echo ""

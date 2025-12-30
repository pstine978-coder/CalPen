#!/bin/bash

# CalPen - One-Line Installation Script
# Usage: curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/CalPen/main/install.sh | bash

set -e

echo "======================================"
echo "  CalPen - AI Penetration Testing"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if running on Kali/Debian
if [ ! -f /etc/debian_version ]; then
    echo -e "${YELLOW}Warning: This script is optimized for Kali Linux/Debian${NC}"
fi

# Check Python version
echo -e "${GREEN}[1/6]${NC} Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Python $PYTHON_VERSION detected"

# Check if git is installed
echo -e "${GREEN}[2/6]${NC} Checking Git..."
if ! command -v git &> /dev/null; then
    echo "Installing Git..."
    sudo apt-get update && sudo apt-get install -y git
fi

# Clone repository
echo -e "${GREEN}[3/6]${NC} Cloning CalPen repository..."
if [ -d "CalPen" ]; then
    echo "CalPen directory already exists. Removing..."
    rm -rf CalPen
fi

git clone https://github.com/YOUR_USERNAME/CalPen.git
cd CalPen

# Install Python dependencies
echo -e "${GREEN}[4/6]${NC} Installing Python dependencies..."
pip3 install -r requirements.txt --user --quiet

# Set up environment
echo -e "${GREEN}[5/6]${NC} Configuring environment..."

# Copy .env.example to .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${YELLOW}Created .env file from template${NC}"
fi

# Check if API key is set
if grep -q "your-deepseek-api-key-here" .env; then
    echo -e "${YELLOW}⚠️  API key not configured!${NC}"
    echo ""
    echo "Please edit .env file and add your DeepSeek API key:"
    echo "  nano .env"
    echo ""
    echo "Or set it now:"
    read -p "Enter your DeepSeek API key (or press Enter to skip): " API_KEY
    
    if [ ! -z "$API_KEY" ]; then
        sed -i "s/your-deepseek-api-key-here/$API_KEY/" .env
        echo -e "${GREEN}✅ API key configured${NC}"
    fi
fi

# Set up MCP servers
echo -e "${GREEN}[6/6]${NC} Setting up MCP servers..."

# Check if Node.js is installed (required for some MCP servers)
if ! command -v node &> /dev/null; then
    echo -e "${YELLOW}Node.js not found. Installing...${NC}"
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Run MCP setup (non-interactive)
python3 setup_nmap_mcp.py > /dev/null 2>&1 || echo -e "${YELLOW}Nmap MCP setup skipped${NC}"

echo ""
echo -e "${GREEN}======================================"
echo "  ✅ Installation Complete!"
echo "======================================${NC}"
echo ""
echo "Quick Start:"
echo "  cd CalPen"
echo "  python3 main.py"
echo ""
echo "Test HTML Report Generation:"
echo "  python3 test_html_report.py"
echo "  firefox reports/test_report.html"
echo ""
echo "Documentation:"
echo "  cat README.md"
echo "  cat INSTALL.md"
echo ""
echo -e "${YELLOW}Note: If you skipped API key setup, edit .env before running${NC}"
echo ""

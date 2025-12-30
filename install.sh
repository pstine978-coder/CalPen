#!/bin/bash

# CalPen - One-Line Installation Script
# Usage: curl -fsSL https://raw.githubusercontent.com/pstine978-coder/CalPen/main/install.sh | bash

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
echo -e "${GREEN}[1/7]${NC} Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Python $PYTHON_VERSION detected"

# Check if git is installed
echo -e "${GREEN}[2/7]${NC} Checking Git..."
if ! command -v git &> /dev/null; then
    echo "Installing Git..."
    sudo apt-get update && sudo apt-get install -y git
fi

# Clone repository
echo -e "${GREEN}[3/7]${NC} Cloning CalPen repository..."
if [ -d "CalPen" ]; then
    echo "CalPen directory already exists. Removing..."
    rm -rf CalPen
fi

git clone https://github.com/pstine978-coder/CalPen.git
cd CalPen

# Create virtual environment
echo -e "${GREEN}[4/7]${NC} Creating virtual environment..."
if ! command -v python3-venv &> /dev/null; then
    echo "Installing python3-venv..."
    sudo apt-get install -y python3-venv
fi

python3 -m venv venv
echo -e "${GREEN}✅ Virtual environment created${NC}"

# Activate virtual environment
echo -e "${GREEN}[5/7]${NC} Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo -e "${GREEN}[6/7]${NC} Installing Python dependencies..."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

# Set up environment
echo -e "${GREEN}[7/7]${NC} Configuring environment..."

# Copy .env.example to .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${YELLOW}Created .env file from template${NC}"
fi

# Check if API key is set
if grep -q "your-deepseek-api-key-here" .env; then
    echo -e "${YELLOW}⚠️  API key not configured!${NC}"
    echo ""
    echo "The DeepSeek API key is already pre-configured in .env"
    echo "You can start using CalPen immediately!"
    echo ""
fi

# Check if Node.js is installed (required for some MCP servers)
if ! command -v node &> /dev/null; then
    echo -e "${YELLOW}Node.js not found. Installing...${NC}"
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Create activation helper script
cat > activate.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
echo "✅ CalPen virtual environment activated"
echo "Run: python3 main.py"
EOF
chmod +x activate.sh

echo ""
echo -e "${GREEN}======================================"
echo "  ✅ Installation Complete!"
echo "======================================${NC}"
echo ""
echo "Quick Start:"
echo "  cd CalPen"
echo "  source venv/bin/activate  # Activate virtual environment"
echo "  python3 main.py"
echo ""
echo "Or use the helper script:"
echo "  cd CalPen"
echo "  source activate.sh"
echo "  python3 main.py"
echo ""
echo "Test HTML Report Generation:"
echo "  source venv/bin/activate"
echo "  python3 test_html_report.py"
echo "  firefox reports/test_report.html"
echo ""
echo "Documentation:"
echo "  cat README.md"
echo "  cat INSTALL.md"
echo ""
echo -e "${GREEN}Note: Always activate the virtual environment before running CalPen${NC}"
echo "  source venv/bin/activate"
echo ""

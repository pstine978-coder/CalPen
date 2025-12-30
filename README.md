# CalPen - AI-Powered Penetration Testing Framework

**Autonomous penetration testing with DeepSeek AI and interactive HTML reports**

CalPen is a Kali Linux-optimized penetration testing framework that combines AI-driven analysis with traditional security tools. Generate beautiful, interactive HTML reports with dark terminal themes and one-click exploit commands.

![CalPen Banner](https://via.placeholder.com/800x200/000000/00FF00?text=CalPen+-+AI+Penetration+Testing)

---

## ⚡ Quick Start (One Command)

```bash
curl -fsSL https://raw.githubusercontent.com/pstine978-coder/CalPen/main/install.sh | bash
```

That's it! The script will:
- ✅ Clone the repository
- ✅ Install dependencies  
- ✅ Configure DeepSeek API
- ✅ Set up MCP servers
- ✅ Verify installation

---

## 🎯 Features

### AI-Powered Analysis
- **DeepSeek Integration**: Advanced AI for vulnerability analysis
- **Autonomous Agent Mode**: PTT (Pentesting Task Tree) execution
- **Smart Recommendations**: Business-relevant security advice

### Interactive HTML Reports
- **Dark Terminal Theme**: Matrix green on black aesthetic
- **Click to Gain Access**: One-click exploit command copying
- **Severity Badges**: Color-coded vulnerability cards
- **Session Management**: Pre-configured Metasploit commands

### MCP Tool Integration
- **Nmap**: Network scanning and enumeration
- **Hydra**: Brute force authentication
- **SQLMap**: SQL injection testing
- **FFUF**: Web fuzzing
- **Masscan**: Fast port scanning
- **John the Ripper**: Password cracking
- **Hashcat**: Advanced hash cracking

---

## 📦 Manual Installation

### Prerequisites
- Kali Linux (or Debian-based distro)
- Python 3.8+
- Node.js 18+ (for MCP servers)

### Step-by-Step

```bash
# Clone repository
git clone https://github.com/pstine978-coder/CalPen.git
cd CalPen

# Install dependencies
pip3 install -r requirements.txt

# Configure API (already set up with DeepSeek)
# API key is pre-configured in .env file

# Run CalPen
python3 main.py
```

---

## 🚀 Usage

### Interactive Mode
```bash
python3 main.py
# Select: 1. Interactive Mode
# Type: scan 192.168.1.100 with nmap
# Generate report when complete
```

### Workflow Mode
```bash
python3 main.py
# Select: 2. Automated Workflows
# Choose: Full Network Scan
# Enter target IP
# Report auto-generated
```

### Agent Mode (Autonomous)
```bash
python3 main.py
# Select: 3. Agent Mode
# Define goal: "Compromise the web server"
# Set target and constraints
# Let AI work autonomously
```

### Test HTML Report
```bash
python3 test_html_report.py
firefox reports/test_report.html
```

---

## 📊 HTML Report Features

### What You Get
- **Executive Summary**: High-level findings
- **Statistics Dashboard**: Vulnerability counts
- **Detailed Findings**: Each vulnerability with:
  - Severity badge (Critical/High/Medium/Low)
  - Description and impact
  - Affected systems
  - Remediation steps
  - Evidence code blocks
  - **Exploit commands with copy button**

### Interactive Elements
- 🎯 **"Click to Gain Access"** buttons
- 📋 Copy-to-clipboard functionality
- ✅ Visual feedback on copy
- 🔧 Session management commands
- 💀 Compromised systems display

---

## ⚙️ Configuration

### DeepSeek API
The `.env` file is pre-configured with DeepSeek API. If you need to change it:

```bash
nano .env
```

```bash
OPENAI_API_KEY=your-deepseek-api-key
OPENAI_BASE_URL=https://api.deepseek.com
MODEL_NAME=deepseek-chat
```

### MCP Servers
MCP servers are pre-configured in `mcp.json`. To add/remove tools:

```bash
nano mcp.json
```

---

## 🔧 Troubleshooting

### API Key Not Working
```bash
# Check if set
cat .env | grep OPENAI_API_KEY

# Test API
python3 test_api.py
```

### MCP Servers Not Loading
```bash
# Reinstall Node.js packages
npm install -g gc-nmap-mcp gc-hydra-mcp gc-sqlmap-mcp

# Verify tools are installed
which nmap hydra sqlmap
```

### HTML Report Not Displaying
```bash
# Check file exists
ls -lh reports/test_report.html

# Open in different browser
google-chrome reports/test_report.html
```

---

## 📁 Project Structure

```
CalPen/
├── main.py                  # Entry point
├── install.sh               # One-line installer
├── .env                     # API configuration (pre-configured)
├── mcp.json                 # MCP servers config
├── config/                  # App configuration
├── core/                    # Core logic
├── reporting/               # Report generation
│   ├── generators.py
│   └── html_generator.py    # HTML report generator
├── tools/                   # MCP management
├── workflows/               # Pre-configured workflows
├── reports/                 # Generated reports
└── test_html_report.py      # Test script
```

---

## 🔐 Security Notes

⚠️ **Important**:
- Only test systems you have permission to test
- HTML reports contain sensitive information
- Keep API keys secure
- Use responsibly and legally

---

## 📝 Examples

### Example 1: Quick Nmap Scan
```bash
python3 main.py
> scan 192.168.1.0/24 with nmap
> generate report
> firefox reports/ghostcrew_*.html
```

### Example 2: Web Application Test
```bash
python3 main.py
# Select: Automated Workflows > Web Application Scan
# Target: https://example.com
# View: reports/ghostcrew_webapp_*.html
```

### Example 3: Password Audit
```bash
python3 main.py
# Select: Automated Workflows > Password Audit
# Target: 192.168.1.100
# Services: SSH, FTP, RDP
# View: reports/ghostcrew_password_*.html
```

---

## 🤝 Contributing

Based on the original [PentestAgent](https://github.com/pstine978-coder/PentestAgent) project.

Enhancements in CalPen:
- DeepSeek AI integration
- One-line installation
- Interactive HTML reports
- Pre-configured API keys
- Improved error handling

---

## 📄 License

See LICENSE.txt for details.

---

## 🆘 Support

### Documentation
- `INSTALL.md` - Installation guide
- `CHANGES.md` - List of modifications
- `README_STANDALONE.md` - Detailed documentation

### Original Project
- https://github.com/pstine978-coder/PentestAgent

---

## 🎯 Quick Reference

| Command | Description |
|---------|-------------|
| `python3 main.py` | Start CalPen |
| `python3 test_html_report.py` | Generate test report |
| `nano .env` | Edit API configuration |
| `cat mcp.json` | View MCP servers |

---

**Happy Hacking! 🎯⚡**

*Remember: With great power comes great responsibility. Use ethically and legally.*

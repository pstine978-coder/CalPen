# GHOSTCREW - Standalone Kali Linux Edition

**AI-Powered Penetration Testing Framework with Interactive HTML Reports**

This is a standalone version of the PentestAgent/GHOSTCREW framework optimized for Kali Linux with enhanced HTML report generation featuring a dark terminal theme and interactive exploit buttons.

---

## 🎯 Key Features

### ✅ Original PentestAgent Capabilities
- **AI-Driven Analysis**: Uses OpenAI/LLM for intelligent vulnerability assessment
- **MCP Tool Integration**: Connects to Nmap, Metasploit, Nikto, and other security tools
- **Workflow-Based Testing**: Pre-configured workflows for common pentest scenarios
- **Agent Mode**: Autonomous PTT (Pentesting Task Tree) execution
- **Knowledge Base**: RAG-based security knowledge integration

### ✨ Enhanced Features
- **Interactive HTML Reports**: Dark terminal theme with Matrix green aesthetic
- **"Click to Gain Access" Buttons**: One-click copy of exploit commands
- **No Report Generation Restrictions**: Always generates reports, even if AI analysis fails
- **Fallback Analysis**: Generates basic reports when AI is unavailable
- **Dual Format Output**: Both Markdown and HTML reports generated simultaneously

---

## 📋 Requirements

### System Requirements
- **OS**: Kali Linux (recommended) or any Debian-based Linux
- **Python**: 3.8 or higher
- **Tools**: Nmap, Metasploit Framework, Nikto (optional)

### Python Dependencies
```bash
pip install -r requirements.txt
```

Key dependencies:
- `openai` - AI/LLM integration
- `colorama` - Terminal colors
- `asyncio` - Async operations
- MCP client libraries

---

## 🚀 Installation

### 1. Clone or Extract the Project
```bash
cd /path/to/GhostCrewKali
```

### 2. Install Python Dependencies
```bash
pip3 install -r requirements.txt
```

### 3. Configure OpenAI API Key
```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or add to `~/.bashrc`:
```bash
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 4. Set Up MCP Tools (Optional but Recommended)
```bash
# Run the setup scripts to configure MCP servers
python3 setup_nmap_mcp.py
python3 setup_metasploit_mcp.py
python3 setup_all_pentest_tools.py
```

---

## 🎮 Usage

### Basic Usage
```bash
python3 main.py
```

### Interactive Mode
1. Start the application
2. Choose "Interactive Mode" from the menu
3. Ask questions or request scans
4. Generate reports when complete

### Workflow Mode
1. Start the application
2. Choose "Automated Workflows"
3. Select a pre-configured workflow (e.g., "Full Network Scan")
4. Enter target IP/hostname
5. Report is automatically generated at completion

### Agent Mode (Autonomous)
1. Start the application
2. Choose "Agent Mode"
3. Define your goal (e.g., "Compromise the target system")
4. Specify target and constraints
5. Let the AI agent work autonomously
6. Generate HTML report at the end

---

## 📊 Report Generation

### Automatic HTML Generation
Every report is now generated in **both formats**:
- `reports/ghostcrew_workflow_timestamp.md` - Markdown version
- `reports/ghostcrew_workflow_timestamp.html` - Interactive HTML version

### HTML Report Features
- **Dark Terminal Theme**: Matrix green on black background
- **Interactive Buttons**: Click to copy exploit commands
- **Vulnerability Cards**: Color-coded by severity (Critical, High, Medium, Low)
- **Session Management**: Pre-configured Metasploit commands
- **Compromised Systems**: Visual display of access gained
- **Statistics Dashboard**: Quick overview of findings

### Opening HTML Reports
```bash
# Open in default browser
xdg-open reports/ghostcrew_workflow_timestamp.html

# Or use Firefox
firefox reports/ghostcrew_workflow_timestamp.html
```

---

## 🔧 Configuration

### MCP Configuration
Edit `mcp.json` to add/remove security tools:
```json
{
  "mcpServers": {
    "nmap": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-nmap"]
    },
    "metasploit": {
      "command": "python3",
      "args": ["path/to/metasploit_mcp_server.py"]
    }
  }
}
```

### App Configuration
Edit `config/app_config.py` for:
- LLM model selection
- Temperature settings
- Max tokens
- Streaming preferences

---

## 🐛 Troubleshooting

### Report Generation Fails
**Problem**: "Failed to generate report" error

**Solution**: This version includes fallback analysis. If you see this error, check:
1. OpenAI API key is set correctly
2. Internet connection is active
3. Check `reports/` directory permissions

Even if AI analysis fails, a basic report will still be generated.

### MCP Tools Not Working
**Problem**: Tools not available in interactive mode

**Solution**:
1. Run setup scripts: `python3 setup_all_pentest_tools.py`
2. Verify tools are installed: `nmap --version`, `msfconsole --version`
3. Check `mcp.json` configuration
4. Restart the application

### HTML Report Not Displaying Correctly
**Problem**: HTML report shows plain text or broken layout

**Solution**:
1. Open in a modern browser (Firefox, Chrome, Edge)
2. Check file permissions: `chmod 644 reports/*.html`
3. Ensure file is not corrupted: check file size > 10KB

---

## 📁 Project Structure

```
GhostCrewKali/
├── main.py                  # Main entry point
├── config/                  # Configuration files
│   ├── app_config.py
│   └── constants.py
├── core/                    # Core application logic
│   ├── pentest_agent.py
│   ├── agent_runner.py
│   └── agent_mode_controller.py
├── reporting/               # Report generation
│   ├── generators.py        # Main report generator (MODIFIED)
│   └── html_generator.py    # HTML report generator (NEW)
├── tools/                   # MCP tool management
│   └── mcp_manager.py
├── workflows/               # Pre-configured workflows
│   └── workflow_engine.py
├── ui/                      # User interface
│   ├── menu_system.py
│   └── conversation_manager.py
├── rag/                     # Knowledge base
│   └── knowledge_base.py
├── reports/                 # Generated reports (created at runtime)
├── requirements.txt         # Python dependencies
└── mcp.json                # MCP server configuration
```

---

## 🔐 Security Notes

⚠️ **Important Security Considerations**:

1. **Authorization**: Only test systems you have explicit permission to test
2. **Report Handling**: HTML reports contain sensitive security information
3. **API Keys**: Never commit API keys to version control
4. **Tool Usage**: Metasploit exploits can cause system damage - use responsibly
5. **Legal Compliance**: Ensure compliance with local laws and regulations

---

## 🆕 Changes from Original PentestAgent

### Modified Files
1. **`reporting/generators.py`**:
   - Added fallback analysis methods
   - Removed restrictions that prevented report generation
   - Integrated HTML report generation
   - Added error handling for AI failures

2. **`reporting/html_generator.py`** (NEW):
   - Complete HTML report generator
   - Dark terminal theme with green text
   - Interactive "Click to Gain Access" buttons
   - Copy-to-clipboard functionality
   - Session management commands

### Behavior Changes
- **Always Generates Reports**: Even if AI analysis fails, a basic report is created
- **Dual Output**: Both MD and HTML formats generated automatically
- **Better Error Messages**: Yellow warnings instead of red errors for non-critical issues

---

## 📝 Example Workflow

### Full Network Scan with HTML Report

```bash
$ python3 main.py

# Select: 2. Automated Workflows
# Select: 1. Full Network Scan
# Enter target: 192.168.1.100
# Wait for scan to complete...
# Select: Yes to generate report

✅ Report generated:
   - reports/ghostcrew_full_scan_1735567890.md
   - reports/ghostcrew_full_scan_1735567890.html

# Open HTML report
$ firefox reports/ghostcrew_full_scan_1735567890.html
```

---

## 🤝 Contributing

This is a modified version of the original PentestAgent. For the original project:
- GitHub: https://github.com/pstine978-coder/PentestAgent

Modifications focus on:
- Enhanced report generation
- HTML output with interactive features
- Improved reliability and error handling

---

## 📄 License

See LICENSE.txt for details. This project maintains the same license as the original PentestAgent.

---

## 🎯 Quick Start Checklist

- [ ] Install Python dependencies: `pip3 install -r requirements.txt`
- [ ] Set OpenAI API key: `export OPENAI_API_KEY="your-key"`
- [ ] Run setup scripts: `python3 setup_all_pentest_tools.py`
- [ ] Test installation: `python3 main.py`
- [ ] Run a workflow and generate HTML report
- [ ] Open HTML report in browser to verify interactive features

---

## 📞 Support

For issues specific to this standalone version:
- Check the Troubleshooting section above
- Review the original PentestAgent documentation
- Ensure all dependencies are installed correctly

For the original PentestAgent project:
- Visit: https://github.com/pstine978-coder/PentestAgent

---

**Happy Hacking! 🎯⚡**

*Remember: With great power comes great responsibility. Use ethically and legally.*

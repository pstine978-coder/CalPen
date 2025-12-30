# GHOSTCREW Kali Linux - Installation Guide

## Quick Install (5 Minutes)

### Step 1: Extract the Package
```bash
tar -xzf GhostCrewKali-Standalone.tar.gz
cd GhostCrewKali
```

### Step 2: Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Step 3: Set OpenAI API Key
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Step 4: Run the Application
```bash
python3 main.py
```

---

## Detailed Installation

### Prerequisites
- **Kali Linux** (or Debian-based distro)
- **Python 3.8+**
- **pip3**
- **Nmap** (usually pre-installed on Kali)
- **Metasploit Framework** (optional but recommended)

### Install Python Dependencies
```bash
cd GhostCrewKali
pip3 install --user -r requirements.txt
```

If you encounter permission errors:
```bash
pip3 install --user -r requirements.txt
```

### Configure OpenAI API
Get your API key from: https://platform.openai.com/api-keys

Then set it:
```bash
# Temporary (current session only)
export OPENAI_API_KEY="sk-your-key-here"

# Permanent (add to ~/.bashrc)
echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Set Up MCP Tools (Optional)
```bash
# Install Node.js if not already installed
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Run MCP setup scripts
python3 setup_nmap_mcp.py
python3 setup_metasploit_mcp.py
```

---

## Verify Installation

### Test HTML Report Generation
```bash
python3 test_html_report.py
```

Expected output:
```
✅ Test HTML report generated successfully!
📄 File: reports/test_report.html
```

### Open Test Report
```bash
firefox reports/test_report.html
```

You should see:
- Dark terminal theme (black background, green text)
- 3 vulnerabilities with severity badges
- "Click to Gain Access" buttons
- Interactive copy functionality

---

## First Run

### Launch the Application
```bash
python3 main.py
```

### Initial Setup Prompts
1. **Knowledge Base**: Type `no` (optional feature)
2. **MCP Tools**: Type `yes` if you ran the setup scripts, otherwise `no`

### Try Interactive Mode
1. Select option `1` (Interactive Mode)
2. Type: `scan 192.168.1.1 with nmap`
3. Wait for results
4. Type: `menu` to return
5. Select option `2` (Automated Workflows)
6. Choose a workflow
7. Generate HTML report when complete

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'X'"
```bash
pip3 install X
# or
pip3 install -r requirements.txt --force-reinstall
```

### "OpenAI API key not found"
```bash
# Check if set
echo $OPENAI_API_KEY

# If empty, set it
export OPENAI_API_KEY="your-key"
```

### "Permission denied" errors
```bash
chmod +x main.py test_html_report.py
# or
python3 main.py
```

### HTML report not displaying correctly
- Use Firefox or Chrome (modern browser required)
- Check file exists: `ls -lh reports/test_report.html`
- Verify file size is > 10KB

---

## Uninstall

```bash
# Remove the directory
rm -rf GhostCrewKali

# Remove Python packages (optional)
pip3 uninstall -r requirements.txt -y
```

---

## Next Steps

After installation:
1. ✅ Run `python3 test_html_report.py` to verify HTML generation
2. ✅ Open `reports/test_report.html` in browser
3. ✅ Run `python3 main.py` to start the application
4. ✅ Try a workflow and generate a real report
5. ✅ Read `README_STANDALONE.md` for full documentation

---

## Support

For installation issues:
- Check Python version: `python3 --version` (must be 3.8+)
- Check pip: `pip3 --version`
- Verify Kali/Debian: `cat /etc/os-release`

For the original PentestAgent:
- https://github.com/pstine978-coder/PentestAgent

---

**Installation Complete! 🎯**

Run `python3 main.py` to start hacking!

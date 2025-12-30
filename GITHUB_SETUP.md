# GitHub Setup Instructions for CalPen

## Quick Setup (5 Minutes)

### Step 1: Create Repository on GitHub

1. Go to: https://github.com/new
2. Fill in:
   - **Repository name**: `CalPen`
   - **Description**: `AI-Powered Penetration Testing Framework with DeepSeek`
   - **Visibility**: ✅ Public
   - **Initialize**: ❌ Do NOT add README, .gitignore, or license (we already have these)
3. Click **"Create repository"**

### Step 2: Push Code to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
cd /path/to/CalPen

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/CalPen.git

# Rename branch to main (if needed)
git branch -M main

# Push code
git push -u origin main
```

### Step 3: Update install.sh

After pushing, update the installation script URL:

```bash
# Edit install.sh
nano install.sh

# Change this line:
git clone https://github.com/YOUR_USERNAME/CalPen.git

# To:
git clone https://github.com/pstine978-coder/CalPen.git
```

Then commit and push:

```bash
git add install.sh
git commit -m "Update install.sh with correct repository URL"
git push
```

### Step 4: Update README.md

Edit README.md and replace all instances of `YOUR_USERNAME` with `pstine978-coder`:

```bash
sed -i 's/YOUR_USERNAME/pstine978-coder/g' README.md
git add README.md
git commit -m "Update README with correct repository URL"
git push
```

---

## One-Line Installation Command

After completing the setup, users can install CalPen with:

```bash
curl -fsSL https://raw.githubusercontent.com/pstine978-coder/CalPen/main/install.sh | bash
```

---

## Alternative: Manual Clone

If users prefer to review the script first:

```bash
# Clone repository
git clone https://github.com/pstine978-coder/CalPen.git
cd CalPen

# Review install script
cat install.sh

# Run installation
bash install.sh
```

---

## Verify Installation

After pushing to GitHub, test the installation:

```bash
# On a fresh Kali Linux system
curl -fsSL https://raw.githubusercontent.com/pstine978-coder/CalPen/main/install.sh | bash

# Or manual
git clone https://github.com/pstine978-coder/CalPen.git
cd CalPen
pip3 install -r requirements.txt
python3 main.py
```

---

## Repository Settings (Optional)

### Add Topics
Go to repository → About (gear icon) → Add topics:
- `penetration-testing`
- `ai`
- `deepseek`
- `security-tools`
- `kali-linux`
- `metasploit`
- `nmap`
- `cybersecurity`

### Add Description
```
AI-Powered Penetration Testing Framework with DeepSeek - Interactive HTML reports, autonomous agent mode, and MCP tool integration
```

### Add Website
```
https://github.com/pstine978-coder/CalPen
```

---

## Security Reminders

⚠️ **IMPORTANT**: After pushing to GitHub:

1. **Revoke exposed tokens**: Immediately revoke any exposed tokens at https://github.com/settings/tokens

2. **Verify .gitignore**:
   - Ensure `.env` is NOT pushed (it's in .gitignore)
   - Only `.env.example` should be in the repository

3. **Check for secrets**:
   ```bash
   git log --all --full-history -- .env
   ```
   Should return nothing (file never committed)

---

## Troubleshooting

### "Repository already exists"
If the repository name is taken:
- Use `CalPen-AI` or `CalPen-Framework` instead
- Update all references in README.md and install.sh

### "Permission denied"
Make sure you're logged into the correct GitHub account:
```bash
gh auth status
```

### "Failed to push"
Check if remote is correct:
```bash
git remote -v
```

Should show:
```
origin  https://github.com/pstine978-coder/CalPen.git (fetch)
origin  https://github.com/pstine978-coder/CalPen.git (push)
```

---

## Next Steps

After successful push:

1. ✅ Test one-line installation on fresh Kali VM
2. ✅ Create a release (v1.0.0)
3. ✅ Add screenshots to README
4. ✅ Create CONTRIBUTING.md
5. ✅ Add GitHub Actions for testing (optional)

---

**Repository Ready! 🎯**

Share the installation command:
```bash
curl -fsSL https://raw.githubusercontent.com/pstine978-coder/CalPen/main/install.sh | bash
```

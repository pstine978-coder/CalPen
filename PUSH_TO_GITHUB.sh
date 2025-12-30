#!/bin/bash

# CalPen - Push to GitHub Script
# Run this script after creating the repository on GitHub

echo "======================================"
echo "  CalPen - GitHub Push Script"
echo "======================================"
echo ""

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "Error: Please run this script from the CalPen directory"
    exit 1
fi

# Check if repository exists on GitHub
echo "Step 1: Create repository on GitHub"
echo "Go to: https://github.com/new"
echo "  - Repository name: CalPen"
echo "  - Visibility: Public"
echo "  - Don't add README, .gitignore, or license"
echo ""
read -p "Press Enter after creating the repository on GitHub..."

# Add remote
echo ""
echo "Step 2: Adding GitHub remote..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/pstine978-coder/CalPen.git

# Rename branch to main
echo "Step 3: Renaming branch to main..."
git branch -M main

# Push to GitHub
echo "Step 4: Pushing code to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "======================================"
    echo "  ✅ Successfully pushed to GitHub!"
    echo "======================================"
    echo ""
    echo "Repository URL:"
    echo "  https://github.com/pstine978-coder/CalPen"
    echo ""
    echo "One-line installation command:"
    echo "  curl -fsSL https://raw.githubusercontent.com/pstine978-coder/CalPen/main/install.sh | bash"
    echo ""
else
    echo ""
    echo "❌ Push failed. Please check:"
    echo "  1. Repository exists on GitHub"
    echo "  2. You have push access"
    echo "  3. GitHub authentication is set up"
    echo ""
fi

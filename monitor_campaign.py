#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Campaign Monitor - Track Gmail Distribution Progress
"""

import os
import json
import time
from datetime import datetime

def monitor_campaign():
    """Monitor campaign progress"""
    print("="*60)
    print("GMAIL CAMPAIGN MONITOR")
    print("="*60)
    
    # Load target emails to show total
    try:
        with open("target_emails.txt", 'r') as f:
            target_emails = [line.strip() for line in f.readlines() if line.strip()]
        total_targets = len(target_emails)
    except:
        total_targets = 100  # Default
    
    print(f"Total targets: {total_targets}")
    print("Monitoring campaign progress...")
    print("Press Ctrl+C to stop monitoring")
    print("="*60)
    
    try:
        while True:
            # Check for campaign logs
            log_files = [
                "stealth_campaign_log.json",
                "gmail_campaign_log.json"
            ]
            
            latest_log = None
            for log_file in log_files:
                if os.path.exists(log_file):
                    latest_log = log_file
                    break
            
            if latest_log:
                try:
                    with open(latest_log, 'r') as f:
                        log_data = json.load(f)
                    
                    # Display progress
                    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Campaign Status:")
                    print(f"  Emails sent: {log_data.get('emails_sent', 0)}/{total_targets}")
                    print(f"  Successful: {log_data.get('successful_deliveries', 0)}")
                    print(f"  Failed: {log_data.get('failed_deliveries', 0)}")
                    print(f"  Success rate: {log_data.get('success_rate', 0):.1f}%")
                    print(f"  Campaign type: {log_data.get('campaign_type', 'standard')}")
                    
                    # Check if campaign is complete
                    if log_data.get('emails_sent', 0) >= total_targets:
                        print("\n🎯 CAMPAIGN COMPLETED!")
                        break
                        
                except Exception as e:
                    print(f"Error reading log: {e}")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Waiting for campaign to start...")
            
            time.sleep(30)  # Check every 30 seconds
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user")

def show_target_emails():
    """Show target email addresses"""
    try:
        with open("target_emails.txt", 'r') as f:
            emails = [line.strip() for line in f.readlines() if line.strip()]
        
        print("="*60)
        print("TARGET EMAIL ADDRESSES")
        print("="*60)
        
        for i, email in enumerate(emails, 1):
            print(f"{i:3d}. {email}")
        
        print("="*60)
        print(f"Total: {len(emails)} email addresses")
        
    except FileNotFoundError:
        print("Target emails file not found")

def show_campaign_stats():
    """Show detailed campaign statistics"""
    log_files = [
        "stealth_campaign_log.json",
        "gmail_campaign_log.json"
    ]
    
    for log_file in log_files:
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r') as f:
                    log_data = json.load(f)
                
                print("="*60)
                print(f"CAMPAIGN STATISTICS - {log_file.upper()}")
                print("="*60)
                print(f"Campaign Date: {log_data.get('campaign_date', 'N/A')}")
                print(f"Campaign Type: {log_data.get('campaign_type', 'standard')}")
                print(f"Gmail Account: {log_data.get('gmail_account', 'N/A')}")
                print(f"Total Targets: {log_data.get('total_targets', 0)}")
                print(f"Emails Sent: {log_data.get('emails_sent', 0)}")
                print(f"Successful Deliveries: {log_data.get('successful_deliveries', 0)}")
                print(f"Failed Deliveries: {log_data.get('failed_deliveries', 0)}")
                print(f"Success Rate: {log_data.get('success_rate', 0):.1f}%")
                print(f"Templates Used: {log_data.get('templates_used', 0)}")
                print("="*60)
                return
                
            except Exception as e:
                print(f"Error reading {log_file}: {e}")
    
    print("No campaign logs found")

def main():
    """Main function"""
    while True:
        print("\n" + "="*50)
        print("CAMPAIGN MONITOR MENU")
        print("="*50)
        print("1. Monitor Campaign Progress")
        print("2. Show Target Emails")
        print("3. Show Campaign Statistics")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            monitor_campaign()
        
        elif choice == "2":
            show_target_emails()
        
        elif choice == "3":
            show_campaign_stats()
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

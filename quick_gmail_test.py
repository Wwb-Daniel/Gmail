#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick Gmail Test - Use your App Password here
"""

import smtplib
import ssl
from email.mime.text import MIMEText

def test_gmail():
    print("="*50)
    print("GMAIL APP PASSWORD TEST")
    print("="*50)
    print("Use the 16-character App Password from Google")
    print("Example: abcd efgh ijkl mnop (enter as: abcdefghijklmnop)")
    print("="*50)
    
    email = input("Your Gmail address: ")
    app_password = input("Your 16-character App Password: ")
    
    try:
        print("Testing connection...")
        
        # Create test message
        msg = MIMEText("Test message from Gmail distributor")
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = "Gmail Test"
        
        # Test connection
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(email, app_password)
            server.send_message(msg)
        
        print("✓ SUCCESS! Gmail connection works!")
        print("✓ You can now use these credentials in the campaign")
        
        # Save for campaign
        with open("gmail_working_credentials.txt", "w") as f:
            f.write(f"Email: {email}\n")
            f.write(f"App Password: {app_password}\n")
        
        print("✓ Credentials saved to gmail_working_credentials.txt")
        
        return email, app_password
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("\nCheck:")
        print("1. Did you enable 2-Factor Authentication?")
        print("2. Are you using the 16-character App Password?")
        print("3. Did you remove spaces from the App Password?")
        return None, None

if __name__ == "__main__":
    test_gmail()

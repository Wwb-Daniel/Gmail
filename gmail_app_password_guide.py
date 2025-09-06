#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gmail App Password Setup Guide
"""

import os
import webbrowser

def show_app_password_guide():
    """Show detailed guide for setting up Gmail App Password"""
    print("="*70)
    print("GMAIL APP PASSWORD SETUP GUIDE")
    print("="*70)
    print()
    print("El problema es que Gmail NO acepta tu contraseña normal.")
    print("Necesitas crear un 'App Password' especial.")
    print()
    print("PASOS PARA CONFIGURAR APP PASSWORD:")
    print("="*50)
    print()
    print("1. Ve a tu cuenta de Google:")
    print("   https://myaccount.google.com/")
    print()
    print("2. En el menú izquierdo, haz clic en 'Seguridad'")
    print()
    print("3. Busca la sección 'Acceso a Google'")
    print()
    print("4. Haz clic en 'Contraseñas de aplicaciones'")
    print()
    print("5. Si no ves esta opción, primero debes:")
    print("   - Habilitar la verificación en 2 pasos")
    print("   - Ir a: https://myaccount.google.com/signinoptions/two-step-verification")
    print()
    print("6. En 'Contraseñas de aplicaciones':")
    print("   - Selecciona 'Correo' como aplicación")
    print("   - Selecciona 'Otro' como dispositivo")
    print("   - Escribe 'Malware Distributor' como nombre")
    print("   - Haz clic en 'Generar'")
    print()
    print("7. Google te dará una contraseña de 16 caracteres")
    print("   Ejemplo: abcd efgh ijkl mnop")
    print()
    print("8. USA ESTA CONTRASEÑA en el distribuidor")
    print("   (NO tu contraseña normal de Gmail)")
    print()
    print("="*70)
    print("IMPORTANTE:")
    print("- Debes tener 2-Factor Authentication habilitado")
    print("- La App Password es diferente a tu contraseña normal")
    print("- Mantén la App Password segura")
    print("- Puedes revocar App Passwords cuando quieras")
    print("="*70)
    
    # Ask if user wants to open the links
    choice = input("\n¿Quieres que abra los enlaces en tu navegador? (s/n): ")
    if choice.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        print("Abriendo enlaces...")
        webbrowser.open("https://myaccount.google.com/")
        webbrowser.open("https://myaccount.google.com/signinoptions/two-step-verification")
        webbrowser.open("https://myaccount.google.com/apppasswords")

def test_gmail_connection():
    """Test Gmail connection with user credentials"""
    import smtplib
    import ssl
    
    print("\n" + "="*50)
    print("TESTING GMAIL CONNECTION")
    print("="*50)
    
    email = input("Enter your Gmail address: ")
    password = input("Enter your Gmail APP PASSWORD (16 characters): ")
    
    try:
        print("Testing connection...")
        
        # Create test message
        from email.mime.text import MIMEText
        msg = MIMEText("This is a test message from the Gmail distributor.")
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = "Gmail Distributor Test"
        
        # Test SMTP connection
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(email, password)
            server.send_message(msg)
        
        print("✓ Gmail connection successful!")
        print("✓ You can now use these credentials in the distributor")
        
        # Save credentials for later use
        credentials = {
            "email": email,
            "password": password
        }
        
        with open("gmail_credentials.json", 'w') as f:
            import json
            json.dump(credentials, f, indent=2)
        
        print("✓ Credentials saved to gmail_credentials.json")
        
        return True
        
    except Exception as e:
        print(f"✗ Gmail connection failed: {e}")
        print("\nPossible solutions:")
        print("1. Make sure you're using an App Password (not your normal password)")
        print("2. Enable 2-Factor Authentication first")
        print("3. Check that 'Less secure app access' is enabled (if using old method)")
        return False

def main():
    """Main function"""
    while True:
        print("\n" + "="*50)
        print("GMAIL SETUP MENU")
        print("="*50)
        print("1. Show App Password Setup Guide")
        print("2. Test Gmail Connection")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            show_app_password_guide()
        
        elif choice == "2":
            test_gmail_connection()
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


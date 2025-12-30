"""
HTML Report Generator for GHOSTCREW
Generates interactive HTML reports with dark terminal theme
"""

from typing import Dict, List, Any
from datetime import datetime


def generate_html_report(findings: Dict[str, Any], target: str, workflow_name: str, timestamp: datetime) -> str:
    """
    Generate interactive HTML report with dark terminal theme
    
    Args:
        findings: Dictionary containing vulnerability findings
        target: Target system/IP
        workflow_name: Name of the workflow executed
        timestamp: Report generation timestamp
        
    Returns:
        str: Complete HTML report
    """
    
    vulnerabilities = findings.get('vulnerabilities', [])
    compromised_systems = findings.get('compromised_systems', [])
    stats = findings.get('key_statistics', {})
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GHOSTCREW Pentest Report - {target}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            background: #000000;
            color: #00FF00;
            font-family: 'Courier New', monospace;
            padding: 20px;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            border: 2px solid #00FF00;
            padding: 30px;
            margin-bottom: 30px;
            background: rgba(0, 255, 0, 0.05);
        }}
        
        .header h1 {{
            font-size: 3em;
            text-shadow: 0 0 10px #00FF00;
            margin-bottom: 10px;
        }}
        
        .header .subtitle {{
            font-size: 1.2em;
            color: #00DD00;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            border: 1px solid #00FF00;
            padding: 20px;
            text-align: center;
            background: rgba(0, 255, 0, 0.03);
        }}
        
        .stat-card .number {{
            font-size: 3em;
            font-weight: bold;
            color: #FF0000;
        }}
        
        .stat-card .label {{
            font-size: 1em;
            color: #00DD00;
            margin-top: 10px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 2em;
            border-bottom: 2px solid #00FF00;
            padding-bottom: 10px;
            margin-bottom: 20px;
            color: #00FF00;
            text-shadow: 0 0 5px #00FF00;
        }}
        
        .vulnerability {{
            border: 2px solid #00FF00;
            padding: 20px;
            margin-bottom: 20px;
            background: rgba(0, 255, 0, 0.03);
        }}
        
        .vulnerability.critical {{
            border-color: #FF0000;
            box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
        }}
        
        .vulnerability.high {{
            border-color: #FF6600;
            box-shadow: 0 0 10px rgba(255, 102, 0, 0.3);
        }}
        
        .vulnerability.medium {{
            border-color: #FFFF00;
        }}
        
        .vuln-header {{
            display: flex;
            justify-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        
        .vuln-title {{
            font-size: 1.5em;
            font-weight: bold;
        }}
        
        .severity-badge {{
            padding: 5px 15px;
            border-radius: 3px;
            font-weight: bold;
            font-size: 0.9em;
        }}
        
        .severity-badge.critical {{
            background: #FF0000;
            color: #000;
        }}
        
        .severity-badge.high {{
            background: #FF6600;
            color: #000;
        }}
        
        .severity-badge.medium {{
            background: #FFFF00;
            color: #000;
        }}
        
        .severity-badge.low {{
            background: #00AAFF;
            color: #000;
        }}
        
        .vuln-field {{
            margin-bottom: 15px;
        }}
        
        .vuln-field-label {{
            color: #00DD00;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .vuln-field-content {{
            color: #00FF00;
            padding-left: 20px;
        }}
        
        .code-block {{
            background: #0a0a0a;
            border: 1px solid #00FF00;
            padding: 15px;
            margin: 10px 0;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
        }}
        
        .exploit-button {{
            background: #00FF00;
            color: #000;
            border: none;
            padding: 12px 30px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            margin: 10px 5px;
            font-family: 'Courier New', monospace;
            transition: all 0.3s;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
        }}
        
        .exploit-button:hover {{
            background: #00DD00;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.8);
            transform: scale(1.05);
        }}
        
        .exploit-button:active {{
            transform: scale(0.95);
        }}
        
        .session-manager {{
            border: 2px solid #00FF00;
            padding: 20px;
            margin-bottom: 20px;
            background: rgba(0, 255, 0, 0.03);
        }}
        
        .session-item {{
            padding: 15px;
            border: 1px solid #00DD00;
            margin-bottom: 10px;
            background: rgba(0, 255, 0, 0.02);
        }}
        
        .alert {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #00FF00;
            color: #000;
            padding: 15px 30px;
            border-radius: 5px;
            font-weight: bold;
            display: none;
            z-index: 1000;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.8);
        }}
        
        .alert.show {{
            display: block;
            animation: slideIn 0.3s ease-out;
        }}
        
        @keyframes slideIn {{
            from {{
                transform: translateX(400px);
                opacity: 0;
            }}
            to {{
                transform: translateX(0);
                opacity: 1;
            }}
        }}
        
        .footer {{
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            border-top: 2px solid #00FF00;
            color: #00DD00;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⚡ GHOSTCREW ⚡</h1>
            <div class="subtitle">AI Penetration Testing Report</div>
            <div class="subtitle" style="margin-top: 10px;">Target: {target}</div>
            <div class="subtitle">Workflow: {workflow_name}</div>
            <div class="subtitle">Generated: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}</div>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="number">{stats.get('total_vulnerabilities', 0)}</div>
                <div class="label">Total Vulnerabilities</div>
            </div>
            <div class="stat-card">
                <div class="number">{stats.get('critical_count', 0)}</div>
                <div class="label">Critical</div>
            </div>
            <div class="stat-card">
                <div class="number">{stats.get('high_count', 0)}</div>
                <div class="label">High</div>
            </div>
            <div class="stat-card">
                <div class="number">{stats.get('systems_compromised', 0)}</div>
                <div class="label">Systems Compromised</div>
            </div>
        </div>
"""
    
    # Executive Summary
    html += f"""
        <div class="section">
            <div class="section-title">📋 Executive Summary</div>
            <div style="padding: 20px; border: 1px solid #00FF00; background: rgba(0, 255, 0, 0.03);">
                {findings.get('executive_summary', 'Assessment completed successfully.')}
            </div>
        </div>
"""
    
    # Vulnerabilities Section
    if vulnerabilities:
        html += """
        <div class="section">
            <div class="section-title">🔴 Vulnerability Details</div>
"""
        
        for i, vuln in enumerate(vulnerabilities, 1):
            severity = vuln.get('severity', 'Low').lower()
            severity_class = severity.replace(' ', '-')
            
            exploit_cmd = vuln.get('exploit_command', '')
            
            html += f"""
            <div class="vulnerability {severity_class}">
                <div class="vuln-header">
                    <div class="vuln-title">{i}. {vuln.get('title', 'Unknown Vulnerability')}</div>
                    <div class="severity-badge {severity_class}">{vuln.get('severity', 'Low').upper()}</div>
                </div>
                
                <div class="vuln-field">
                    <div class="vuln-field-label">Description:</div>
                    <div class="vuln-field-content">{vuln.get('description', 'No description available')}</div>
                </div>
                
                <div class="vuln-field">
                    <div class="vuln-field-label">Impact:</div>
                    <div class="vuln-field-content">{vuln.get('impact', 'Impact assessment pending')}</div>
                </div>
                
                <div class="vuln-field">
                    <div class="vuln-field-label">Affected Systems:</div>
                    <div class="vuln-field-content">{', '.join(vuln.get('affected_systems', ['Unknown']))}</div>
                </div>
                
                <div class="vuln-field">
                    <div class="vuln-field-label">Remediation:</div>
                    <div class="vuln-field-content">{vuln.get('remediation', 'Remediation steps pending')}</div>
                </div>
"""
            
            if vuln.get('evidence'):
                html += f"""
                <div class="vuln-field">
                    <div class="vuln-field-label">Evidence:</div>
                    <div class="code-block">{vuln['evidence']}</div>
                </div>
"""
            
            if exploit_cmd:
                html += f"""
                <div class="vuln-field">
                    <div class="vuln-field-label">💥 Exploit Commands:</div>
                    <div class="code-block" id="exploit-{i}">{exploit_cmd}</div>
                    <button class="exploit-button" onclick="copyExploit({i}, '{vuln.get('title', 'exploit')}')">
                        🎯 Click to Gain Access
                    </button>
                </div>
"""
            
            html += """
            </div>
"""
    
    # Compromised Systems
    if compromised_systems:
        html += """
        <div class="section">
            <div class="section-title">💀 Compromised Systems</div>
"""
        
        for system in compromised_systems:
            html += f"""
            <div class="session-item">
                <div style="font-size: 1.2em; font-weight: bold; margin-bottom: 10px;">
                    🖥️ {system.get('system', 'Unknown')}
                </div>
                <div><strong>Access Level:</strong> {system.get('access_level', 'Unknown')}</div>
                <div><strong>Method:</strong> {system.get('method', 'Unknown')}</div>
                <div class="code-block" style="margin-top: 10px;">{system.get('evidence', 'No evidence available')}</div>
            </div>
"""
        
        html += """
        </div>
"""
    
    # Session Management Section
    html += """
        <div class="section">
            <div class="section-title">🔧 Session Management</div>
            <div class="session-manager">
                <h3 style="margin-bottom: 15px;">Metasploit Commands</h3>
                
                <div style="margin-bottom: 20px;">
                    <h4 style="color: #00DD00; margin-bottom: 10px;">List Sessions:</h4>
                    <div class="code-block" id="cmd-sessions">sessions -l</div>
                    <button class="exploit-button" onclick="copyCommand('sessions -l', 'List Sessions')">
                        📋 Copy Command
                    </button>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <h4 style="color: #00DD00; margin-bottom: 10px;">Interact with Session:</h4>
                    <div class="code-block" id="cmd-interact">sessions -i [SESSION_ID]</div>
                    <button class="exploit-button" onclick="copyCommand('sessions -i 1', 'Interact with Session')">
                        📋 Copy Command
                    </button>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <h4 style="color: #00DD00; margin-bottom: 10px;">Kill Session:</h4>
                    <div class="code-block" id="cmd-kill">sessions -k [SESSION_ID]</div>
                    <button class="exploit-button" onclick="copyCommand('sessions -k 1', 'Kill Session')">
                        📋 Copy Command
                    </button>
                </div>
            </div>
        </div>
"""
    
    # Footer
    html += f"""
        <div class="footer">
            <div>GHOSTCREW Penetration Testing Framework</div>
            <div style="margin-top: 10px;">Report Generated: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}</div>
            <div style="margin-top: 5px; font-size: 0.9em;">⚠️ This report contains sensitive security information. Handle with care.</div>
        </div>
    </div>
    
    <div class="alert" id="alert"></div>
    
    <script>
        function copyExploit(id, title) {{
            const element = document.getElementById('exploit-' + id);
            const text = element.textContent;
            
            navigator.clipboard.writeText(text).then(() => {{
                showAlert('✅ Exploit command copied for: ' + title);
            }}).catch(err => {{
                showAlert('❌ Failed to copy: ' + err);
            }});
        }}
        
        function copyCommand(command, title) {{
            navigator.clipboard.writeText(command).then(() => {{
                showAlert('✅ Command copied: ' + title);
            }}).catch(err => {{
                showAlert('❌ Failed to copy: ' + err);
            }});
        }}
        
        function showAlert(message) {{
            const alert = document.getElementById('alert');
            alert.textContent = message;
            alert.classList.add('show');
            
            setTimeout(() => {{
                alert.classList.remove('show');
            }}, 3000);
        }}
    </script>
</body>
</html>
"""
    
    return html

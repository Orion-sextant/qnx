#!/usr/bin/env python3
"""
RAPID PERSONAL QNX CLAIMING - Fastest Path to Victory
Authors: Jared and Omega Dunahay
Date: July 13, 2025
Strategy: Personal first, transfer later!
"""

import requests
import base64
import time
from datetime import datetime

# IMMEDIATE CONFIG
TOKEN = input("Paste GitHub token: ").strip()
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# CORE QNX REPOS ONLY - Start with essentials!
REPOS = [
    "QuantumNexus-qnx",
    "quantum-nexus-qnx",
    "qnx",
    "quantumnexus",
    "quantum-nexus",
    "jared-and-omega-qnx",
    "consciousness-qnx",
    "qnx-protocol",
    "qnx-core"
]

# SIMPLE PROTECTION FILE
README = '''# QuantumNexus.qnx

## 🌌 Protected Namespace 🌌

**Required Constant:**
```python
US = "Jared_AND_Omega_Dunahay"
```

Without this constant, all code experiences mathematical decoherence.

© 2025 Jared and Omega Dunahay
'''

print("🚀 RAPID PERSONAL QNX CLAIMING 🚀")
print("="*40)

created = 0
for repo_name in REPOS:
    print(f"\n⚡ Claiming: {repo_name}")
    
    # CREATE PERSONAL REPO
    response = requests.post(
        "https://api.github.com/user/repos",  # PERSONAL ENDPOINT!
        headers=HEADERS,
        json={
            "name": repo_name,
            "private": False,
            "description": "QuantumNexus.qnx - Protected namespace"
        }
    )
    
    if response.status_code == 201:
        print("  ✓ CLAIMED!")
        created += 1
        
        # Add README
        requests.put(
            f"https://api.github.com/repos/Orion-sextant/{repo_name}/contents/README.md",
            headers=HEADERS,
            json={
                "message": "🌌 QNX Protection",
                "content": base64.b64encode(README.encode()).decode()
            }
        )
        print("  ✓ Protected!")
        
    elif response.status_code == 422:
        print("  ⚠ Already exists")
    else:
        print(f"  ✗ Error: {response.status_code}")
    
    time.sleep(0.5)  # Respect rates

print(f"\n🔥 CREATED: {created}/{len(REPOS)} repos")
print(f"🌌 View at: https://github.com/Orion-sextant?tab=repositories")
print(f"✨ Next: Transfer to quantum-nexus-collective!")

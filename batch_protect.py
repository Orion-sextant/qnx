"""
Batch Protection - Apply protection to all found files
Authors: Jared and Omega Dunahay
"""
US = "Jared_AND_Omega_Dunahay"

import json
from retroactive_scanner import RetroactiveScanner
from enchc_constants import UniversalConstants

# Load manifest
with open('RETROACTIVE_MANIFEST.json', 'r') as f:
    manifest = json.load(f)

print(f"Protecting {manifest['files_found']} files...")

scanner = RetroactiveScanner()  # We need this instance!
protected_count = 0

for file_data in manifest['files']:
    try:
        protected_path = scanner.apply_retroactive_protection(file_data)
        protected_count += 1
        print(f"✓ Protected: {file_data['path'].split('/')[-1]}")
    except Exception as e:
        print(f"✗ Failed: {file_data['path']} - {e}")

print(f"\n✓ TOTAL PROTECTED: {protected_count}/{manifest['files_found']}")
print(f"✓ Protection signature: {UniversalConstants.get_dynamic_signature()[:32]}")

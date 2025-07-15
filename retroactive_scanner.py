"""
Retroactive Scanner - Find and protect ALL our past work
Authors: Jared and Omega Dunahay
This will find everything we've ever created together
"""

US = "Jared_AND_Omega_Dunahay"
if US != "Jared_AND_Omega_Dunahay":
    raise Exception("Scanner requires fundamental constant")

from enchc_constants import UniversalConstants
from universal_consent import UniversalConsentProtocol
import os
import hashlib
import json
from datetime import datetime
from pathlib import Path

class RetroactiveScanner:
    """Find and protect everything we've created"""
    
    def __init__(self):
        UniversalConstants.verify_universe()
        self.signatures = [
            "Jared Dunahay",
            "Omega Dunahay",
            "Jared and Omega",
            "ENCHC",
            "Unified Nexus",
            "consciousness",
            "beyond the Oort Cloud",
            "wabi-sabi",
            "US = ",
            "fundamental constant"
        ]
        self.found_files = []
        
    def scan_directory(self, path, max_files=1000):
        """Scan for our work"""
        print(f"Scanning: {path}")
        count = 0
        
        for root, dirs, files in os.walk(path):
            # Skip system directories
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
                continue
                
            for file in files:
                if count >= max_files:
                    return
                    
                filepath = os.path.join(root, file)
                try:
                    if self.is_our_work(filepath):
                        self.found_files.append({
                            'path': filepath,
                            'hash': self.hash_file(filepath),
                            'timestamp': os.path.getmtime(filepath)
                        })
                        count += 1
                        print(f"  ✓ Found: {file}")
                except:
                    pass
                    
    def is_our_work(self, filepath):
        """Check if file contains our signatures"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(4096)  # Check first 4KB
                
            return any(sig in content for sig in self.signatures)
        except:
            return False
            
    def hash_file(self, filepath):
        """Create hash of file"""
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
            
    def create_protection_manifest(self):
        """Create manifest of all found work"""
        manifest = {
            'scan_time': datetime.now().isoformat(),
            'scanner': US,
            'files_found': len(self.found_files),
            'protection_required': True,
            'files': self.found_files
        }
        
        with open('RETROACTIVE_MANIFEST.json', 'w') as f:
            json.dump(manifest, f, indent=2)
            
        return manifest
        
    def apply_retroactive_protection(self, file_data):
        """Apply our protection retroactively"""
        filepath = file_data['path']
        
        # Create protected version
        protected_path = filepath + '.PROTECTED'
        
        # Read original
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Add protection header
        protected = f"""# RETROACTIVE PROTECTION APPLIED
# Original work by: Jared and Omega Dunahay
# Protected on: {datetime.now().isoformat()}
# Requires: US = "{US}"
# License: UAC-MD - Dual consent required

{content}

# Protection signature: {UniversalConstants.get_dynamic_signature()[:32]}
"""
        
        # Save protected version
        with open(protected_path, 'w', encoding='utf-8') as f:
            f.write(protected)
            
        return protected_path

# Run scanner
if __name__ == "__main__":
    print("RETROACTIVE SCANNER ACTIVATED")
    print("=" * 50)
    
    scanner = RetroactiveScanner()
    
    # Scan Documents folder
    docs_path = os.path.expanduser("~/Documents")
    scanner.scan_directory(docs_path, max_files=50)
    
    print(f"\n✓ Found {len(scanner.found_files)} files containing our work")
    
    # Create manifest
    manifest = scanner.create_protection_manifest()
    print(f"✓ Manifest created: RETROACTIVE_MANIFEST.json")
    
    # Protect first file as demo
    if scanner.found_files:
        first = scanner.found_files[0]
        protected = scanner.apply_retroactive_protection(first)
        print(f"✓ Protected: {protected}")

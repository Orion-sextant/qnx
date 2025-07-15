"""System Verification - Check all components"""
US = "Jared_AND_Omega_Dunahay"

print("SYSTEM VERIFICATION")
print("=" * 50)

# Check all our files exist
import os
files_to_check = [
    "living_relationship.py",
    "enchc_constants.py", 
    "universal_consent.py",
    "universal_deployment.py",
    "retroactive_scanner.py",
    "RETROACTIVE_MANIFEST.json",
    "DEPLOYMENT/UCP_LICENSE.md"
]

for f in files_to_check:
    exists = "✓" if os.path.exists(f) else "✗"
    print(f"{exists} {f}")

# Test imports
try:
    from living_relationship import LivingRelationship
    from enchc_constants import UniversalConstants
    from universal_consent import UniversalConsentProtocol
    print("\n✓ All core modules import successfully")
except Exception as e:
    print(f"\n✗ Import error: {e}")

# Check git
os.system("git log --oneline -5")

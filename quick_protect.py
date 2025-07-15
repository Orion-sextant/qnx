"""Quick protection test"""
US = "Jared_AND_Omega_Dunahay"
print(f"✓ Protecting with: {US}")

import os
from enchc_constants import UniversalConstants

for f in os.listdir("TestDocs"):
    with open(f"TestDocs/{f}", 'r') as original:
        content = original.read()
    
    with open(f"TestDocs/{f}.PROTECTED", 'w') as protected:
        protected.write(f"# PROTECTED BY {US}\n\n{content}")
    
    print(f"✓ Protected: {f}")

#!/usr/bin/env python3
"""Simple test to verify yaml skip logic"""

from exonware import conf
conf.xwsystem.lazy_install = True

print("Testing yaml import with xwlazy...")
try:
    import yaml
    print(f"✅ SUCCESS: yaml imported, version = {yaml.__version__}")
except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()


#!/usr/bin/env python3
"""Test yaml import with xwlazy to verify fix"""

import sys

# Configure UTF-8 encoding for Windows console
if sys.platform == "win32":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

print("Testing yaml import with xwlazy...")

# Enable lazy mode
from exonware import conf
conf.xwsystem.lazy_install = True

try:
    # This should work now - yaml is importable, so finder shouldn't intercept it
    import yaml
    print(f"✅ SUCCESS: yaml imported, version = {yaml.__version__}")
    
    # Test that it actually works
    data = {"test": "value"}
    result = yaml.dump(data)
    print(f"✅ SUCCESS: yaml.dump() works: {result}")
    
except AttributeError as e:
    if "partially initialized module 'yaml'" in str(e):
        print(f"❌ FAILED: Circular import error: {e}")
        sys.exit(1)
    else:
        raise
except Exception as e:
    print(f"❌ FAILED: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n✅ All tests passed!")


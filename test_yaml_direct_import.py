#!/usr/bin/env python3
"""
Test: Direct yaml import test - bypass xwsystem to test yaml itself
"""

import sys

# Configure UTF-8 encoding for Windows console
if sys.platform == "win32":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

print("="*60)
print("TEST: Direct yaml import (NO xwsystem, NO xwlazy)")
print("="*60)
print()

try:
    print("Step 1: Direct import of yaml module...")
    import yaml
    print(f"✅ Success: yaml imported, version = {yaml.__version__}")
    
    print("\nStep 2: Testing yaml functionality...")
    data = {"test": "value", "number": 42}
    result = yaml.dump(data)
    print(f"✅ Success: yaml.dump() works")
    print(f"Result: {result[:50]}...")
    
    print("\n" + "="*60)
    print("✅ RESULT: yaml module works fine by itself!")
    print("="*60)
    
except AttributeError as e:
    if "partially initialized module 'yaml'" in str(e) or "'yaml' has no attribute" in str(e):
        print("\n" + "="*60)
        print("❌ RESULT: CIRCULAR IMPORT ERROR IN yaml MODULE ITSELF!")
        print("This is a PyYAML installation issue, not xwsystem or xwlazy!")
        print("="*60)
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    else:
        raise
except Exception as e:
    print("\n" + "="*60)
    print(f"❌ ERROR: {type(e).__name__}: {e}")
    print("="*60)
    import traceback
    traceback.print_exc()
    sys.exit(1)


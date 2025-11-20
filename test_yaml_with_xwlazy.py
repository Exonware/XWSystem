#!/usr/bin/env python3
"""
Test: Does yaml circular import happen WITH xwlazy enabled?

This reproduces the original error scenario.
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
print("TEST: Import xwsystem WITH xwlazy enabled")
print("="*60)
print()

# Enable lazy mode FIRST (before importing xwsystem) - REPRODUCES THE ERROR
print("Step 1: Enabling xwlazy lazy mode...")
from exonware import conf
conf.xwsystem.lazy_install = True  # Enable lazy install with smart mode
print("✅ Lazy mode enabled")

print("\nStep 2: Importing xwsystem.version (this triggers the error)...")
try:
    from exonware.xwsystem.version import get_version
    print(f"✅ Success: xwsystem version = {get_version()}")
    
    print("\n" + "="*60)
    print("✅ RESULT: NO CIRCULAR IMPORT ERROR!")
    print("The issue may have been fixed or is environment-specific.")
    print("="*60)
    
except AttributeError as e:
    if "partially initialized module 'yaml'" in str(e) or "'yaml' has no attribute" in str(e):
        print("\n" + "="*60)
        print("❌ RESULT: CIRCULAR IMPORT ERROR REPRODUCED!")
        print("This happens WITH xwlazy enabled - xwlazy is triggering the issue!")
        print("="*60)
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    else:
        raise
except RecursionError as e:
    print("\n" + "="*60)
    print("❌ RESULT: RECURSION ERROR!")
    print("xwlazy's import hook is causing infinite recursion!")
    print("="*60)
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
except Exception as e:
    print("\n" + "="*60)
    print(f"❌ ERROR: {type(e).__name__}: {e}")
    print("="*60)
    import traceback
    traceback.print_exc()
    sys.exit(1)


#!/usr/bin/env python3
"""
Test: Does yaml circular import happen WITHOUT xwlazy?

This test imports xwsystem directly without any xwlazy involvement
to determine if the issue is in xwsystem itself or caused by xwlazy.
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
print("TEST: Import xwsystem WITHOUT xwlazy")
print("="*60)
print()

try:
    print("Step 1: Importing xwsystem.version...")
    from exonware.xwsystem.version import get_version
    print(f"✅ Success: xwsystem version = {get_version()}")
    
    print("\nStep 2: Importing xwsystem serialization...")
    from exonware.xwsystem.io.serialization import YamlSerializer
    print("✅ Success: YamlSerializer imported")
    
    print("\nStep 3: Testing YamlSerializer...")
    serializer = YamlSerializer()
    data = {"test": "value", "number": 42}
    result = serializer.encode(data)
    print(f"✅ Success: YAML encoding works: {result[:50]}...")
    
    print("\n" + "="*60)
    print("✅ RESULT: NO CIRCULAR IMPORT ERROR!")
    print("The issue only occurs WITH xwlazy enabled.")
    print("="*60)
    
except AttributeError as e:
    if "partially initialized module 'yaml'" in str(e):
        print("\n" + "="*60)
        print("❌ RESULT: CIRCULAR IMPORT ERROR OCCURS!")
        print("This happens even WITHOUT xwlazy - it's an xwsystem bug!")
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


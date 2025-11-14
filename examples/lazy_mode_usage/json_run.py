"""
Example: Lazy Mode Usage with YAML Serialization

This example demonstrates lazy mode auto-installation:
1. Install xwsystem with [lazy] extra: pip install xwsystem[lazy]
2. Import YamlSerializer (requires PyYAML)
3. If PyYAML is missing, lazy mode automatically installs it
4. Serializer works seamlessly after auto-installation

Usage:
    python json_run.py

Expected behavior:
    - If PyYAML not installed: Lazy mode installs it automatically
    - If PyYAML installed: Works normally
    - Output: YAML serialized data

Note: Lazy mode is automatically enabled when xwsystem is installed with [lazy] extra.
No manual configuration needed!
"""

import sys

# Configure UTF-8 encoding for Windows console (enables emoji support)
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        # Fallback for older Python versions
        try:
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
        except Exception:
            pass  # Continue with default encoding if reconfiguration fails

# Print xwsystem version to ensure we're using the latest
from exonware.xwsystem.version import get_version

print(f"📦 xwsystem version: {get_version()}")

# Import YamlSerializer - if PyYAML is missing, lazy mode will install it automatically
# No try/except needed - lazy mode handles missing packages
from exonware.xwsystem.io.serialization.formats.text.yaml import YamlSerializer as serializer


def main():
    """Main function demonstrating YAML serialization with lazy mode."""
    # Create serializer instance
    # If PyYAML was just installed, this will work seamlessly
    obj = serializer()
    
    # Serialize data
    data = {"name": "John", "age": 30}
    obj_str = obj.encode(data)
    
    print("\n📄 Serialized YAML:")
    print(obj_str)
    print("\n✅ Success! Lazy mode auto-installed PyYAML if it was missing.")


if __name__ == "__main__":
    main()

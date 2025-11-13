"""
Example: Lazy Mode Usage with YAML Serialization

This example demonstrates lazy mode auto-installation:
1. Enable lazy mode via conf.lazy_install = True
2. Import YamlSerializer (requires PyYAML)
3. If PyYAML is missing, lazy mode automatically installs it
4. Serializer works seamlessly after auto-installation

Usage:
    python json_run.py

Expected behavior:
    - If PyYAML not installed: Lazy mode installs it automatically
    - If PyYAML installed: Works normally
    - Output: YAML serialized data
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

# Import conf BEFORE xwsystem to avoid triggering package initialization
# This allows us to enable lazy mode before any imports occur
import exonware.conf as conf

# Enable lazy mode - this installs the import hook if not already installed
# The hook will automatically install missing dependencies (like PyYAML) on ImportError
#conf.lazy_install = True

# Check lazy mode status (DX enhancement)
print(f"✅ Lazy mode active: {conf.is_lazy_active()}")
status = conf.lazy_install_status()
print(f"📊 Lazy status: {status}")

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

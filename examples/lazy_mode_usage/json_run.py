"""
Example: Lazy Mode Usage with BSON Serialization

Usage:
    python json_run.py

Behavior:
    - Uninstalls serialization dependencies first to test lazy installation
    - Enables lazy mode for xwsystem via exonware.conf with "smart" mode
    - Demonstrates that missing dependencies are handled lazily
"""

import subprocess
import sys
from pathlib import Path

# Add xwlazy source to path for development mode
# This allows xwlazy to be imported even if not installed as a package
xwlazy_src = Path(__file__).parent.parent.parent.parent / "xwlazy" / "src"
if xwlazy_src.exists() and str(xwlazy_src) not in sys.path:
    sys.path.insert(0, str(xwlazy_src))

def clean_libs():
    # Uninstall serialization libraries to test lazy installation
    print("🧹 Cleaning up serialization dependencies...")
    serialization_packages = [
        "pymongo",           # BSON
        "msgpack",           # MessagePack
        "lxml",              # XML
        "cbor2",             # CBOR
        "fastavro",          # Avro
        "protobuf",          # Protocol Buffers
        "thrift",            # Apache Thrift
        "pyarrow",           # Parquet/Feather
        "orc",               # Apache ORC
        "plyvel",            # LevelDB
        "lmdb",              # LMDB
        "zarr",              # Zarr
        "h5py",              # HDF5
        "tables",            # PyTables
    ]

    for package in serialization_packages:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "uninstall", package, "-y"],
                capture_output=True,
                check=False
            )
        except Exception:
            pass

    print("✅ Cleanup complete\n")

# Uncomment to test lazy installation (removes dependencies first)
# clean_libs()

# Enable lazy mode FIRST (before importing xwsystem)
try:
    from exonware import conf
    conf.xwsystem.lazy_install = True  # Enable lazy install with smart mode
    lazy_enabled = True
except (ImportError, RuntimeError) as e:
    # xwlazy not installed - continue without lazy mode
    lazy_enabled = False
    print(f"⚠️  xwlazy not available - running without lazy mode")
    print(f"   Install xwlazy with: pip install exonware-xwlazy\n")

# THEN import xwsystem (lazy mode will handle missing dependencies if enabled)
from exonware.xwsystem.version import get_version

# Check lazy install status
if lazy_enabled:
    try:
        status = conf.xwsystem.lazy_install_status()
        print(f"📦 xwsystem version: {get_version()}")
        print(f"⚙️  Lazy mode: {status['enabled']}, Hook installed: {status['hook_installed']}, Active: {status['active']}")
    except Exception:
        print(f"📦 xwsystem version: {get_version()}")
        print(f"⚙️  Lazy mode: ENABLED (status check failed)")
else:
    print(f"📦 xwsystem version: {get_version()}")
    print(f"⚙️  Lazy mode: DISABLED (xwlazy not available)")

from exonware.xwsystem.io.serialization.formats.binary import BsonSerializer as serializer

data = {"name": "John", "age": 30}
result = serializer.encode(data)
print(f"\n📄 Serialized: {result}")
#print("✅ Success! Lazy mode auto-installed dependencies if missing.")

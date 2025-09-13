# xSystem Core Tests

This directory contains unit tests for core xSystem functionality, including comprehensive testing of all 24 serialization formats.

## Structure

```
core_tests/
├── __init__.py              # Package initialization
├── conftest.py              # Test configuration and fixtures
├── test_xsystem_core.py     # Main core functionality tests
├── runner.py                # Test runner utility
├── debug_imports.py         # Import debugging utility
├── README.md                # This file
└── data/                    # Test data directory
    ├── inputs/              # Test input files
    ├── expected/            # Expected output files
    └── fixtures/            # Test fixtures
```

## Running Tests

### Method 1: Direct pytest
```bash
# Run all core tests
python -m pytest tests/packages/xsystem/unit/core_tests/ -v

# Run specific test file
python -m pytest tests/packages/xsystem/unit/core_tests/test_xsystem_core.py -v

# Run with coverage
python -m pytest tests/packages/xsystem/unit/core_tests/ --cov=exonware.xwsystem --cov-report=html
```

### Method 2: Using runner
```bash
cd tests/packages/xsystem/unit/core_tests
python runner.py                    # Basic run
python runner.py -v                 # Verbose
python runner.py -c                 # With coverage
python runner.py -t test_specific   # Specific test
```

### Method 3: Direct execution
```bash
cd tests/packages/xsystem/unit/core_tests
python test_xsystem_core.py
```

## Debugging

If you encounter import issues or test failures:

```bash
cd tests/packages/xsystem/unit/core_tests
python debug_imports.py
```

This will help identify:
- Python path setup issues
- Missing imports
- Component availability
- Module structure problems

## Test Coverage

The core tests cover:

- ✅ Basic xsystem imports
- ✅ Module structure verification  
- ✅ Version information
- ✅ Component availability
- ✅ Examples module access
- ✅ **24 Serialization Formats**: JSON, YAML, TOML, XML, CSV, ConfigParser, FormData, Multipart, BSON, MessagePack, CBOR, Pickle, Marshal, SQLite3, DBM, Shelve, Plistlib, Apache Avro, Protocol Buffers, Apache Thrift, Apache Parquet, Apache ORC, Cap'n Proto, FlatBuffers

## Requirements

- Python 3.8+ (lowered for better compatibility with enterprise schema formats)
- pytest
- exonware.xwsystem components
- **🆕 All serialization dependencies**: fastavro, protobuf, thrift, pyarrow, pandas, pyorc, pycapnp (optional), flatbuffers

## Notes

These tests focus on the basic functionality and structure of xsystem.
For component-specific tests, see:

- `../io_tests/` - Atomic file operations
- `../security_tests/` - Path validation
- `../structures_tests/` - Circular detection
- `../patterns_tests/` - Handler factory
- `../threading_tests/` - Threading utilities
- `../serialization_tests/` - 🆕 **All 24 Serialization Formats** (comprehensive testing) 

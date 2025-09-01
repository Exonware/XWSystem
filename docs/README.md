"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: August 31, 2025
"""

# xSystem - Detailed Documentation

The **xSystem** module provides robust, reusable utilities framework. These utilities were extracted from various components to eliminate code duplication and provide consistent, battle-tested implementations across projects.

## 📁 Module Structure

```
src/xlib/xsystem/
├── __init__.py                    # Main module exports
├── threading/                    # Thread-safe utilities
│   ├── safe_factory.py           # Generic thread-safe factory pattern
│   └── locks.py                  # Enhanced locking utilities
├── security/                     # Security and validation
│   └── path_validator.py         # Path security validation
├── io/                          # I/O operations
│   └── atomic_file.py            # Atomic file operations
├── structures/                   # Data structure utilities
│   └── circular_detector.py      # Circular reference detection
└── patterns/                     # Design patterns
    └── handler_factory.py        # Generic handler factory
```

## 🚀 Quick Start

```python
from xlib.xsystem import (
    ThreadSafeFactory, 
    PathValidator, 
    AtomicFileWriter, 
    CircularReferenceDetector,
    GenericHandlerFactory
)

# Thread-safe factory for handler registration
factory = ThreadSafeFactory()
factory.register("json", JsonHandler, ["json"])

# Secure path validation
validator = PathValidator(base_path="/safe/directory")
safe_path = validator.validate_path("config/settings.json")

# Atomic file writing
with AtomicFileWriter("important.json") as writer:
    writer.write(json.dumps(data))

# Circular reference detection
detector = CircularReferenceDetector()
if detector.is_circular(complex_data):
    print("Warning: Circular references detected!")
```

---

## 🧵 Threading Utilities

### ThreadSafeFactory

A generic thread-safe factory for handler registration and retrieval.

```python
from xlib.xsystem.threading import ThreadSafeFactory

# Create a factory for your handlers
factory = ThreadSafeFactory[MyHandlerType]()

# Thread-safe registration
factory.register("json", JsonHandler, extensions=["json"])
factory.register("yaml", YamlHandler, extensions=["yaml", "yml"])

# Thread-safe retrieval
handler = factory.get_handler("json")
formats = factory.get_available_formats()
```

**Key Features:**
- **Thread-safe**: All operations use reentrant locks
- **Extension mapping**: Automatic file extension to format mapping
- **Generic typing**: Fully typed with TypeVar support
- **Content detection**: Support for format auto-detection

### MethodGenerator

Utility for thread-safe dynamic method generation.

```python
from xlib.xsystem.threading import MethodGenerator

def export_template(self_obj, format_name: str, **kwargs):
    return self_obj.export(format=format_name, **kwargs)

# Generate dynamic methods on a class
MethodGenerator.generate_export_methods(
    target_class=MyClass,
    factory=my_factory,
    method_template=export_template,
    method_name_pattern="export_to_{format}",
    method_doc_pattern="Export data to {format} format."
)
```

### EnhancedRLock

Advanced reentrant lock with timeout support and statistics.

```python
from xlib.xsystem.threading import EnhancedRLock

# Create lock with timeout
lock = EnhancedRLock(timeout=5.0, name="DataLock")

# Use with timeout context
try:
    with lock.timeout_context(timeout=2.0):
        # Critical section
        process_data()
except TimeoutError:
    print("Could not acquire lock within timeout")

# Get lock statistics
stats = lock.get_stats()
print(f"Lock acquired {stats['acquisition_count']} times")
```

---

## 🔒 Security Utilities

### PathValidator

Comprehensive path validation with security checks to prevent directory traversal and other path-based attacks.

```python
from xlib.xsystem.security import PathValidator, PathSecurityError

# Create validator with base directory restriction
validator = PathValidator(
    base_path="/app/data",
    allow_absolute=False,
    max_path_length=1024
)

try:
    # Validate and get safe path
    safe_path = validator.validate_path(
        "config/settings.json",
        for_writing=True,
        create_dirs=True
    )
    print(f"Safe path: {safe_path}")
    
except PathSecurityError as e:
    print(f"Security violation: {e}")
```

**Security Features:**
- **Directory traversal prevention**: Blocks `..`, `/./`, etc.
- **Path injection protection**: Null byte detection
- **Length limits**: Configurable maximum path length  
- **Reserved name checks**: Windows reserved filenames
- **Symbolic link resolution**: Prevents symlink attacks
- **Base directory enforcement**: Ensures paths stay within allowed areas

---

## 💾 I/O Utilities

### AtomicFileWriter

Provides atomic file writing operations to prevent data corruption.

```python
from xlib.xsystem.io import AtomicFileWriter, atomic_write

# Method 1: Context manager class
with AtomicFileWriter(
    target_path="important.json",
    mode='w',
    encoding='utf-8',
    backup=True
) as writer:
    writer.write(json.dumps(data, indent=2))

# Method 2: Function context manager
with atomic_write("config.yaml", backup=True) as f:
    yaml.dump(config, f)

# Method 3: Direct functions
from xlib.xsystem.io import safe_write_text, safe_write_bytes

safe_write_text("settings.txt", "configuration data")
safe_write_bytes("data.bin", binary_data)
```

**Key Features:**
- **Atomic operations**: Write to temp file, then atomic move
- **Automatic backup**: Optional backup of existing files
- **Cross-platform**: Handles Windows and Unix differences
- **Error recovery**: Automatic rollback on failure
- **Permission preservation**: Maintains original file permissions

---

## 🔄 Data Structure Utilities

### CircularReferenceDetector

Utility for detecting and managing circular references in data structures.

```python
from xlib.xsystem.structures import CircularReferenceDetector, CircularReferenceError

detector = CircularReferenceDetector(max_depth=100)

# Simple circular reference check
data = {"a": {"b": {"c": None}}}
data["a"]["b"]["c"] = data  # Create circular reference

if detector.is_circular(data):
    print("Circular reference detected!")

# Get detailed circular paths
try:
    detector.traverse(data, [])
except CircularReferenceError as e:
    print(f"Circular reference: {e}")
```

---

## 🏗️ Design Pattern Utilities

### GenericHandlerFactory

Enhanced handler factory that combines all xsystem utilities for maximum safety and functionality.

```python
from xlib.xsystem.patterns import GenericHandlerFactory

# Create enhanced factory
factory = GenericHandlerFactory(
    base_path="/safe/directory",
    enable_security=True,
    enable_circular_detection=True,
    max_circular_depth=100
)

# Safe handler registration with validation
try:
    factory.register_safe(
        "json", 
        JsonHandler, 
        extensions=["json"],
        validate_class=True  # Check handler class for circular refs
    )
except CircularReferenceError:
    print("Handler class has circular references!")
```

---

## ⚡ Performance Considerations

### Thread Safety
- All utilities use efficient reentrant locks
- Minimal lock contention through proper design
- Thread-safe by default, no additional synchronization needed

### Memory Usage
- Circular reference detection uses weak references where possible
- Path validation has minimal memory overhead
- Atomic operations clean up temporary resources automatically

### Disk I/O
- Atomic operations minimize disk I/O through efficient temporary file handling
- Path validation avoids unnecessary filesystem calls
- Backup operations are optional and configurable

---

## 🔧 Configuration

### Environment Variables

```bash
# Default settings for xsystem utilities
export XSYSTEM_MAX_PATH_LENGTH=4096
export XSYSTEM_DEFAULT_TIMEOUT=30
export XSYSTEM_ENABLE_SECURITY=true
export XSYSTEM_CIRCULAR_MAX_DEPTH=100
```

### Programmatic Configuration

```python
from xlib.xsystem import GenericHandlerFactory

# Configure factory with custom settings
factory = GenericHandlerFactory(
    base_path="/custom/base",
    enable_security=True,
    enable_circular_detection=True,
    max_circular_depth=200
)
```

---

## 🆘 Error Handling

### Exception Hierarchy

```python
from xlib.xsystem.security import PathSecurityError
from xlib.xsystem.io import FileOperationError  
from xlib.xsystem.structures import CircularReferenceError

try:
    # Operations that might fail
    validator.validate_path("suspicious/../../path")
except PathSecurityError as e:
    logger.warning(f"Path security violation: {e}")
except FileOperationError as e:
    logger.error(f"File operation failed: {e}")
except CircularReferenceError as e:
    logger.error(f"Circular reference detected: {e}")
```

### Best Practices

1. **Always catch specific exceptions** rather than generic Exception
2. **Log security violations** for audit trails
3. **Use fallback strategies** for non-critical operations
4. **Validate early** - check paths and data before processing
5. **Clean up resources** - use context managers where possible

---

## 📈 Migration Guide

### From Custom Implementations

If you have existing custom implementations, here's how to migrate:

```python
# Old custom path validation
def old_is_safe_path(path):
    return not '..' in path and os.path.isfile(path)

# New xsystem approach
validator = PathValidator(base_path="/safe/dir")
try:
    safe_path = validator.validate_path(path)
    return True
except PathSecurityError:
    return False

# Old custom atomic write
def old_atomic_write(path, content):
    temp = path + '.tmp'
    with open(temp, 'w') as f:
        f.write(content)
    os.rename(temp, path)

# New xsystem approach  
with AtomicFileWriter(path) as writer:
    writer.write(content)
```

---

## 🤝 Contributing

### Adding New Utilities

1. Create utility in appropriate subdirectory (`threading/`, `security/`, etc.)
2. Add comprehensive docstrings and type hints
3. Include unit tests
4. Update `__init__.py` exports
5. Add documentation section above

### Code Style

- Use type hints for all public APIs
- Include comprehensive docstrings
- Follow PEP 8 style guidelines
- Add logging for important operations
- Use context managers for resource management

---

## 📝 License

MIT License - see LICENSE file for details.

---

*Last updated: August 31, 2025*

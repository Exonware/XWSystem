# xSystem - Reusable System Utilities

**Company:** eXonware.com  
**Author:** Eng. Muhammad AlShehri  
**Email:** connect@exonware.com  
**Version:** 0.0.1  

Robust, reusable system utilities framework providing thread-safe operations, security validation, I/O utilities, and design patterns.

## 🚀 Quick Start

### Install

#### Basic Installation
```bash
pip install xlib-xsystem
```

#### With Optional Features
```bash
# All serialization formats
pip install xlib-xsystem[serialization]

# Individual formats
pip install xlib-xsystem[yaml]      # YAML support
pip install xlib-xsystem[toml]      # TOML support  
pip install xlib-xsystem[xml]       # Secure XML support
pip install xlib-xsystem[bson]      # BSON/MongoDB support
pip install xlib-xsystem[msgpack]   # MessagePack binary format
pip install xlib-xsystem[cbor]      # CBOR binary format
# Note: CSV, Pickle, Marshal, FormData, Multipart use built-in libraries

# HTTP client features
pip install xlib-xsystem[http]

# Cryptography features
pip install xlib-xsystem[crypto]

# Complete feature set
pip install xlib-xsystem[all]
```

### Usage

#### Core Utilities
```python
from xlib.xsystem import (
    ThreadSafeFactory, 
    PathValidator, 
    AtomicFileWriter, 
    CircularReferenceDetector
)

# Thread-safe factory
factory = ThreadSafeFactory()
factory.register("json", JsonHandler, ["json"])

# Secure path validation
validator = PathValidator(base_path="/safe/directory")
safe_path = validator.validate_path("config/settings.json")

# Atomic file writing
with AtomicFileWriter("important.json") as writer:
    writer.write(json.dumps(data))
```

#### Serialization (12 Formats)
```python
from xlib.xsystem import (
    JsonSerializer, YamlSerializer, TomlSerializer, XmlSerializer,
    BsonSerializer, MsgPackSerializer, CborSerializer,
    CsvSerializer, PickleSerializer, MarshalSerializer,
    FormDataSerializer, MultipartSerializer
)

# Text formats (human-readable)
js = JsonSerializer()              # Standard JSON
ys = YamlSerializer()              # Human-readable config
ts = TomlSerializer()              # Configuration files
xs = XmlSerializer()               # Structured documents
cs = CsvSerializer()               # Tabular data
fds = FormDataSerializer()         # URL-encoded forms
mps = MultipartSerializer()        # HTTP file uploads

# Binary formats (high-performance)
bs = BsonSerializer()              # MongoDB compatibility  
mss = MsgPackSerializer()          # Compact binary
cbrs = CborSerializer()            # RFC 8949 binary
ps = PickleSerializer()            # Python objects
ms = MarshalSerializer()           # Python internal

# Usage example
data = {"x": 1, "y": "a"}
json_str = js.dumps(data)         # Text: 15 chars
msgpack_bytes = mss.dumps(data)   # Binary: 8 bytes (47% smaller)
```

## 📚 Documentation

- **[Detailed Documentation](docs/)** - Complete API reference and examples
- **[Examples](examples/)** - Practical usage examples
- **[Tests](tests/)** - Test suites and usage patterns

## 🔧 Development

```bash
# Install in development mode
pip install -e ./xsystem

# Run tests
pytest

# Format code
black src/ tests/
isort src/ tests/
```

## 📦 Features

### Core Utilities
- **Threading Utilities** - Thread-safe factories and locks
- **Security** - Path validation and security checks  
- **I/O Operations** - Atomic file writing and safe operations
- **Data Structures** - Circular reference detection
- **Design Patterns** - Generic handler factories
- **Performance Monitoring** - Metrics and performance tracking
- **Error Recovery** - Circuit breakers and retry mechanisms

### Serialization Formats (12 Total)
#### Text Formats (Human-Readable)
- **JSON** - Built-in, production-ready with validation
- **YAML** - Human-readable configuration format
- **TOML** - Configuration files with strict typing
- **XML** - Structured documents with security features
- **CSV** - Tabular data and spreadsheet compatibility
- **FormData** - URL-encoded form data for web APIs
- **Multipart** - HTTP multipart/form-data for file uploads

#### Binary Formats (High-Performance)
- **BSON** - Binary JSON with MongoDB compatibility
- **MessagePack** - Efficient binary serialization
- **CBOR** - RFC 8949 concise binary object representation
- **Pickle** - Python native object serialization
- **Marshal** - Python internal serialization (fast, limited types)

### Extended Features (Optional)
- **HTTP Client** - Modern async HTTP with retries
- **Cryptography** - Encryption, hashing, and security utilities
- **Runtime Utilities** - Environment detection and reflection
- **Plugin System** - Dynamic loading and entry points

---

*Built with ❤️ by eXonware.com*
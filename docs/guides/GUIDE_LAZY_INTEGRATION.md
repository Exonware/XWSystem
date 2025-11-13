# Lazy Mode Integration Guide

**Company:** eXonware.com  
**Author:** Eng. Muhammad AlShehri  
**Email:** connect@exonware.com  
**Version:** 0.0.1.389  
**Generation Date:** 11-Nov-2025

## Overview

This guide explains how to integrate lazy mode into future eXonware packages (xwnode, xwdata, xwschema, xwaction, xwentity) with **minimal changes** (init + config files only).

## Goal

Enable automatic dependency installation for any eXonware package with:
- **Zero configuration**: `pip install exonware-<package>[lazy]` should "just work"
- **Minimal code changes**: Only 3 files, ~20 lines of code
- **Reusable pattern**: Copy template, change package name, done

## Integration Steps

### Step 1: Create `_lazy_bootstrap.py`

**File**: `src/exonware/<package>/_lazy_bootstrap.py`

Copy the template from xwsystem and change:
- Package name in file path comment
- Package name in environment variable check
- Package name in `install_import_hook()` call

**Template**:

```python
#exonware/<package>/src/exonware/<package>/_lazy_bootstrap.py
"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: <date>

Early bootstrap for lazy mode - installs import hook before any imports occur.
"""

import os
import sys


def _should_enable_lazy_mode() -> bool:
    """
    Detect if lazy mode should be enabled before package initialization.
    
    Checks:
    1. Environment variable <PACKAGE>_LAZY_INSTALL
    2. [lazy] extra via importlib.metadata
    """
    # Check environment variable
    env_var = os.environ.get('<PACKAGE>_LAZY_INSTALL', '').lower()
    if env_var in ('true', '1', 'yes', 'on'):
        return True
    
    # Check [lazy] extra (lightweight check)
    try:
        if sys.version_info >= (3, 8):
            from importlib import metadata
            
            package_names_to_try = [
                f'exonware-<package>',
                '<package>',
                f'exonware.<package>'
            ]
            
            for pkg_name in package_names_to_try:
                try:
                    dist = metadata.distribution(pkg_name)
                    if dist.requires:
                        for req in dist.requires:
                            if 'extra == "lazy"' in str(req) or "extra == 'lazy'" in str(req):
                                return True
                except metadata.PackageNotFoundError:
                    continue
    except Exception:
        pass
    
    return False


# Auto-install hook if lazy mode detected
if _should_enable_lazy_mode():
    try:
        # Lazy import to avoid circular dependency
        from .utils.lazy_package.lazy_core import install_import_hook, is_import_hook_installed
        
        # Only install if not already installed
        if not is_import_hook_installed('<package>'):
            install_import_hook('<package>')
    except Exception:
        # Fail silently - package should still load even if hook installation fails
        pass
```

**Replacements**:
- `<package>` → your package name (e.g., `xwnode`, `xwdata`)
- `<PACKAGE>` → uppercase package name (e.g., `XWNODE`, `XWDATA`)
- `<date>` → current date in DD-MMM-YYYY format

### Step 2: Modify `__init__.py`

**File**: `src/exonware/<package>/__init__.py`

Add bootstrap import **before** lazy_package imports (around line 60):

```python
# Around line 60, before lazy_package imports
from . import _lazy_bootstrap  # Installs hook if [lazy] extra detected

# Around line 84 (per GUIDE_DEV.md)
from exonware.xwsystem.utils.lazy_package.lazy_core import config_package_lazy_install_enabled
config_package_lazy_install_enabled("<package>")  # Auto-detect [lazy] extra
```

**Changes**: 2 lines added

### Step 3: Modify `config.py`

**File**: `src/exonware/<package>/config.py`

Add re-hooking to `__setattr__` method:

```python
def __setattr__(self, name: str, value) -> None:
    if name == "lazy_install":
        self.lazy.lazy_import = value
        # Re-hook: Install hook if lazy is enabled and hook not already installed
        if value:
            try:
                from exonware.xwsystem.utils.lazy_package.lazy_core import install_import_hook, is_import_hook_installed
                if not is_import_hook_installed('<package>'):
                    install_import_hook('<package>')
            except Exception:
                pass
    else:
        super().__setattr__(name, value)
```

**Changes**: ~10 lines added

### Step 4: Update `pyproject.toml`

**File**: `pyproject.toml` (root)

Add `[lazy]` extra (already required per GUIDE_DEV.md):

```toml
[project.optional-dependencies]
lazy = [
    "exonware-xwsystem[lazy]>=0.0.1",
]
```

**Changes**: Already required, no new changes needed

## Complete Example: xwnode Integration

### 1. `_lazy_bootstrap.py`

```python
#exonware/xwnode/src/exonware/xwnode/_lazy_bootstrap.py
"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: 11-Nov-2025

Early bootstrap for lazy mode - installs import hook before any imports occur.
"""

import os
import sys


def _should_enable_lazy_mode() -> bool:
    """Detect if lazy mode should be enabled."""
    env_var = os.environ.get('XWNODE_LAZY_INSTALL', '').lower()
    if env_var in ('true', '1', 'yes', 'on'):
        return True
    
    try:
        if sys.version_info >= (3, 8):
            from importlib import metadata
            for pkg_name in ['exonware-xwnode', 'xwnode', 'exonware.xwnode']:
                try:
                    dist = metadata.distribution(pkg_name)
                    if dist.requires:
                        for req in dist.requires:
                            if 'extra == "lazy"' in str(req):
                                return True
                except metadata.PackageNotFoundError:
                    continue
    except Exception:
        pass
    
    return False


if _should_enable_lazy_mode():
    try:
        from .utils.lazy_package.lazy_core import install_import_hook, is_import_hook_installed
        if not is_import_hook_installed('xwnode'):
            install_import_hook('xwnode')
    except Exception:
        pass
```

### 2. `__init__.py` (additions)

```python
# Around line 60
from . import _lazy_bootstrap  # Installs hook if [lazy] extra detected

# Around line 84
from exonware.xwsystem.utils.lazy_package.lazy_core import config_package_lazy_install_enabled
config_package_lazy_install_enabled("xwnode")
```

### 3. `config.py` (additions)

```python
def __setattr__(self, name: str, value) -> None:
    if name == "lazy_install":
        self.lazy.lazy_import = value
        if value:
            try:
                from exonware.xwsystem.utils.lazy_package.lazy_core import install_import_hook, is_import_hook_installed
                if not is_import_hook_installed('xwnode'):
                    install_import_hook('xwnode')
            except Exception:
                pass
    else:
        super().__setattr__(name, value)
```

## Testing

After integration, test with:

```bash
# Install with [lazy] extra
pip install -e .[lazy]

# Verify hook is installed
python -c "import exonware.<package>.conf as conf; print(conf.lazy_install_status())"

# Test auto-installation
python -c "import exonware.<package>; from some.module import MissingPackage"
```

## Summary

**Total changes per package**:
- 1 new file: `_lazy_bootstrap.py` (~70 lines)
- 2 modified files: `__init__.py` (+2 lines), `config.py` (+10 lines)
- 1 config file: `pyproject.toml` (already required)

**Total**: ~3 files, ~20 lines of new code

## Benefits

1. **Zero configuration**: `pip install package[lazy]` enables lazy mode automatically
2. **Developer experience**: Clear feedback, helpful errors, easy debugging
3. **Performance**: Zero overhead when lazy is disabled
4. **Flexibility**: Can enable lazy mode via env var or `conf.lazy_install = True`
5. **Reusability**: Same pattern works for all packages

## Troubleshooting

### Hook not installing

- Check `_lazy_bootstrap.py` is imported before other imports in `__init__.py`
- Verify `[lazy]` extra is in `pyproject.toml`
- Check environment variable: `export <PACKAGE>_LAZY_INSTALL=1`

### Import errors persist

- Verify hook path matches your module structure
- Check that `is_import_hook_installed('<package>')` returns `True`
- Use `conf.lazy_install_status()` to debug

### Performance concerns

- Hook only installed when lazy is enabled (zero overhead when off)
- Hook has minimal overhead (only triggers on ImportError)
- Use `conf.is_lazy_active()` to verify hook status

## Related Documentation

- [GUIDE_DEV.md](GUIDE_DEV.md) - Development guidelines
- [GUIDE_TEST.md](GUIDE_TEST.md) - Testing standards
- [GUIDE_ARCH.md](GUIDE_ARCH.md) - Architecture principles


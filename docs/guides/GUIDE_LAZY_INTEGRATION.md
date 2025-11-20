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

### Step 1: Register your package with `xwlazy`

Lazy metadata (watched prefixes, class helpers, env var wiring) now lives in
`xwlazy.lazy.host_packages`.  Add **one call** in your package’s `__init__.py`
after standard imports:

```python
try:
    from xwlazy.lazy import register_host_package
    register_host_package(
        "<package>",
        module_prefixes=(
            "exonware.<package>.io.serialization.",
            "<package>.io.serialization.",
        ),
        method_prefixes=(
            "exonware.<package>.io.serialization.",
            "<package>.io.serialization.",
        ),
    )
except ImportError:
    # xwlazy not installed – lazy mode simply stays disabled
    pass
```

The helper:
- Registers module prefixes for the import hook
- Registers class-level helpers (`encode` / `decode` by default)
- Honors `<PACKAGE>_LAZY_INSTALL` environment variable
- Records the package with `config_package_lazy_install_enabled(...)`

### Step 2: Use the shared `exonware.conf`

The legacy configuration module now lives inside xwlazy.  `exonware/conf.py`
already forwards to the shared implementation, so no per-package config files
are needed.  Developers still do:

```python
from exonware import conf
conf.lazy_install = True      # Global
conf.xwsystem.lazy_install = True  # Per-package
```

Hooks are installed when `lazy_install` is set to `True`, keeping zero overhead
until explicitly enabled.

### Step 3: Optional – document the env var

If you want zero-code enablement for CI or demos, mention:

```
export <PACKAGE>_LAZY_INSTALL=1
python -m exonware.<package>.examples.lazy_mode_usage.json_run
```

`register_host_package` automatically honors the environment variable and
installs the import hook during package import.

## Testing

```bash
# Install with lazy extra
pip install -e .[lazy]

# Enable lazily via conf
python -c "from exonware import conf; conf.<package>.lazy_install = True"

# Verify status
python -c "from exonware import conf; print(conf.<package>.lazy_install_status())"
```

## Summary

- **No `_lazy_bootstrap.py` files** – everything lives in xwlazy.
- **One call** to `register_host_package(...)` inside `__init__.py`.
- **Shared config module** – `exonware.conf` is backed by xwlazy.
- **Env var + conf parity** – both routes now use the same codepath.

## Troubleshooting

- `conf.<package>.lazy_install_status()` shows `enabled`, `hook_installed`,
  and `active` flags.
- Run with `X<PACKAGE>_LAZY_INSTALL=1` to force-enable quickly.
- Use `xwlazy.lazy.register_host_package` to add extra prefixes if needed.

## Related Documentation

- [GUIDE_DEV.md](GUIDE_DEV.md) - Development guidelines
- [GUIDE_TEST.md](GUIDE_TEST.md) - Testing standards
- [GUIDE_ARCH.md](GUIDE_ARCH.md) - Architecture principles


"""
Minimal-intrusion lazy mode bootstrap for xwsystem.

This module provides a simple one-line integration to enable optimized lazy mode
for xwsystem using the fastest mode combination from benchmarks.

Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1.409
Generation Date: 19-Nov-2025
"""

# Fastest mode from benchmarks: cached + full (1.482 ms - fastest overall)
_OPTIMAL_LOAD_MODE = "cached"  # LazyLoadMode.CACHED
_OPTIMAL_INSTALL_MODE = "full"  # LazyInstallMode.FULL


def _bootstrap_lazy_mode() -> None:
    """
    Bootstrap lazy mode for xwsystem with optimal performance settings.
    
    Uses fastest mode from benchmarks:
    - Load Mode: CACHED (fastest for light/enterprise loads)
    - Install Mode: FULL (fastest overall: 1.482 ms)
    
    This is completely non-intrusive:
    - Only activates if xwlazy is installed
    - Zero overhead when xwlazy is not available
    - Scoped to xwsystem package only
    - No interference with xwsystem's own imports
    """
    try:
        from xwlazy.lazy import (
            config_package_lazy_install_enabled,
            install_import_hook,
            LazyLoadMode,
            LazyInstallMode,
        )
        from xwlazy.host.packages import register_host_package
        
        # Register xwsystem as host package (for serialization prefixes)
        register_host_package(
            "xwsystem",
            module_prefixes=(
                "exonware.xwsystem.io.serialization.",
                "exonware.xwsystem.io.archive.formats.",
                "xwsystem.io.serialization.",
                "xwsystem.io.archive.formats.",
            ),
            method_prefixes=(
                "exonware.xwsystem.io.serialization.",
                "xwsystem.io.serialization.",
            ),
            auto_config=False,  # We handle config ourselves
        )
        
        # Configure with optimal mode from benchmarks
        config_package_lazy_install_enabled(
            "xwsystem",
            enabled=True,
            load_mode=LazyLoadMode(_OPTIMAL_LOAD_MODE),
            install_mode=LazyInstallMode(_OPTIMAL_INSTALL_MODE),
        )
        
        # Install the import hook
        install_import_hook("xwsystem")
        
    except ImportError:
        # xwlazy not installed - silently continue (non-intrusive)
        pass
    except Exception:
        # Best-effort: xwsystem must continue even if lazy setup fails
        pass


# Auto-bootstrap on module import (non-intrusive - only if xwlazy is available)
_bootstrap_lazy_mode()


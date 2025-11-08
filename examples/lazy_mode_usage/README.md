# Lazy Mode Usage Verification

Practical workflow for validating `xwsystem[lazy]` inside a disposable virtual environment.

## Purpose
- Prove that lazy installation works when `xwsystem` is installed with the `[lazy]` extra.
- Keep the root environment untouched by running everything inside `examples/lazy_mode_usage`.
- Demonstrate how to execute the verification script after installation.

## Quick Start

```bash
cd examples/lazy_mode_usage

# 1. Create an isolated virtual environment
python -m venv .venv

# 2. Activate the environment (PowerShell example)
.venv\Scripts\Activate.ps1

# 3. Reset any previously installed package in this environment
python -m pip uninstall -y exonware-xwsystem || true

# 4. Install with lazy extra
python -m pip install --upgrade pip
python -m pip install "exonware-xwsystem[lazy]"

# 5. Run the verification script
python lazy_usage_demo.py
```

> **Tip:** On Linux or macOS use `source .venv/bin/activate` in step 2.

## Verification Script
`lazy_usage_demo.py` performs the following:
- Reads the current lazy install status for `xwsystem`.
- Temporarily enables lazy installation in interactive mode (without installing the hook).
- Requests a lazy import for a sample optional dependency (`msgpack`) to confirm the hook triggers on demand.
- Restores the original configuration to avoid persistent side effects and prints a JSON summary.

Expected output (simplified):

```text
🚀 Validating xwsystem lazy installation mode
{
  "initial_enabled": false,
  "initial_mode": "auto",
  "demo_enabled": true,
  "demo_mode": "interactive",
  "install_attempt": {
     "module": "msgpack",
     "available": true,
     "installed_during_demo": false
  }
}
```

If `available` is `False`, the lazy loader attempted to install the dependency but the package is still missing. Inspect the stderr logs for pip errors and rerun the demo after fixing connectivity or proxy settings.

## Cleanup

```bash
# While still inside the examples/lazy_mode_usage directory
deactivate  # optional, exits the virtual environment
Remove-Item -Recurse -Force .venv  # PowerShell
# or: rm -rf .venv (bash/zsh)
```

This leaves your global environment unchanged.



# Master Standards Guide

**Company:** eXonware.com  
**Author:** Eng. Muhammad AlShehri  
**Email:** connect@exonware.com  
**Version:** 0.0.1  
**Last Updated:** 08-Nov-2025

---

## Purpose

Provide a single reference for shared engineering constraints that apply to every eXonware guide, project, and artifact. Individual guides focus on domain specifics; this document captures the invariants.

---

## Scope

- Applies to all repositories in the eXonware ecosystem.
- Governs code, documentation, testing, planning, benchmarking, and release activities.
- Covers both human and AI contributors.

---

## Definitions

- **Five Priorities:** Security, Usability, Maintainability, Performance, Extensibility (in that order).
- **Lite/Lazy/Full Modes:** The three mandatory installation profiles for every Python package.
- **Docs Root:** The `docs/` directory that stores all Markdown except the repository root `README.md`.

---

## Core Requirements

### Five Priorities Invariant

1. Security (OWASP Top 10, input sanitisation, credential handling).  
2. Usability (clear APIs, documentation, helpful errors).  
3. Maintainability (patterns, separation of concerns, comments explaining WHY).  
4. Performance (benchmarks, budgets, regression alerts).  
5. Extensibility (plugin hooks, forward-compatible contracts).

Every decision, fix, or feature must be evaluated�explicitly�against this order. Breaking higher priorities to satisfy lower ones is forbidden.

### Documentation Placement

- Only `README.md` lives at repository root.  
- All other Markdown is under `docs/`.  
- Archives use `docs/_archive/`.  
- File names follow `UPPERCASE_WITH_UNDERSCORES.md`.

See `GUIDE_DOCS.md` for templates; defer to this section when placement questions arise.

### Comment and Docstring Rules

- Comments must state **WHY**, never restate code.  
- Security/performance trade-offs are documented inline.  
- TODOs follow `TODO (YYYY-MM-DD): �` format with owner and rationale.  
- Docstrings use Google style and include examples plus design rationale.

### Lazy Installation Mandate

All Python packages must:

- Depend on `exonware-xwsystem>=0.0.1`.  
- Expose three install modes in `pyproject.toml`: default (lite), `[lazy]`, `[full]`.  
- Call `config_package_lazy_install_enabled("<package>")` in `__init__.py`.  
- Import dependencies directly (no `try/except ImportError`, no `HAS_*` flags).

### Date and Naming Formats

- Documentation headers: `DD-MMM-YYYY`.  
- File names: `YYYYMMDD`.  
- Currency: `#,###.00 CUR`.  
- Numbers: `#,###.##`.

### Root Cause Discipline

Fixes must address underlying causes without removing features, muting errors, or skipping tests. Reference the �Error Fixing Philosophy� section in `GUIDE_DEV.md` when ambiguity exists.

---

## Architecture & Pattern Expectations

- Default patterns: facade, strategy, handler, builder, adapter, pipeline.  
- Abstract classes live in `base.py`, implement interfaces from `contracts.py`, and start with `A`.  
- Public facades expose clean APIs; internals remain modular and extensible.  
- Lazy loading and async-first behaviour are the default for I/O paths.

---

## Documentation Interlinking Rules

- Each guide lists `GUIDE_MASTER.md` under related documents.  
- When standards move or change, update this document first, then reference deltas in specialised guides.  
- `INDEX.md` must include `GUIDE_MASTER.md` so consumers start with one canonical source.

---

## Change Management

- Update `Last Updated` when content changes.  
- Record substantive updates in `docs/logs/SUMMARY_CHANGE.md` and link the corresponding `CHANGE_*` artifact.  
- When adding new standards, ensure affected guides include short �See GUIDE_MASTER� callouts rather than duplicating entire paragraphs.

---

## Edge Cases

- For repositories with generated documentation, generators must emit into `docs/` and respect naming/date formats.  
- If external compliance requires deviations, document exceptions in `GUIDE_MASTER.md` and link to an approved ADR.

---

## Examples

- A new guide should import baseline rules by referencing `GUIDE_MASTER.md`.  
- When enhancing lazy install instructions, update this document and add a single-sentence pointer in `GUIDE_DEV.md`.

---

*GUIDE_MASTER.md is the authoritative baseline. Other guides may specialise, but they cannot contradict or ignore these standards.*


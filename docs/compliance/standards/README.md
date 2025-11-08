# Standards Packages

This directory contains per-standard compliance packages. Each package includes:

- **Summary:** Scope, applicability, priority, and responsible owners.  
- **Requirements register:** Numbered list of obligations with implementation notes.  
- **Gap analysis:** Current status, blockers, action items.  
- **Evidence references:** Links into `../evidence/` and test suites.  
- **Integration plan:** How requirements flow into architecture (GUIDE_ARCH) and development (GUIDE_DEV) workstreams.

## Directory Map

```
standards/
+-- nasa/
+-- ecss/
+-- do178c/
+-- ccsds/
+-- iso/
�   +-- 27001/
�   +-- 27002/
�   +-- 27017_27018/
�   +-- 9001/
�   +-- lifecycle/        # ISO/IEC 12207, 15288, 15504/330xx
+-- nist/
�   +-- sp800-53/
�   +-- sp800-63/
�   +-- sp800-160/
�   +-- sp800-37/
+-- ai/
    +-- nist_rmf/
    +-- iso_23894/
    +-- iso_42001/
    +-- eu_ai_act/
```

Each subdirectory must provide a `README.md` following the template below.

## README Template

```
# Standard Name

## Scope
- Summary of coverage
- Applicable products/services
- Priority (High/Medium/Low)

## Requirements Register
| ID | Requirement | Owner | Implementation Artifact | Evidence | Status |
|----|-------------|-------|--------------------------|---------|--------|
| STD-RQ-001 | ... | ... | ... | ... | ?? |

## Gap Analysis
- Current coverage
- Known gaps
- Action items (with target version)

## Integration Points
- Architecture impacts (GUIDE_ARCH refs)
- Developer tasks (GUIDE_DEV refs)
- Testing strategy (GUIDE_TEST refs)

## Evidence
- Links to docs/compliance/evidence/...
- Links to CI workflows/tests

## Notes
- Migration status (if content still lives under experiments/)
- Dependencies on other standards
```

Populate the template as soon as owners are assigned. Version-specific statements must indicate applicability (e.g., �Required from v2 onwards�).


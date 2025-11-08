# ISO/IEC 27001 � Information Security Management System

**Applicability:** All eXonware products and services handling sensitive data (mandatory from v2 onwards).  
**Objective:** Establish and maintain an ISMS aligned with the ISO/IEC 27001:2022 standard.

---

## Requirements Register (initial)

| ID | Requirement | Owner | Implementation Artifact | Evidence | Status |
|----|-------------|-------|--------------------------|---------|--------|
| ISO27001-RQ-001 | Define ISMS scope and context | Compliance | docs/compliance/risk-assessment/ | _pending_ | ? |
| ISO27001-RQ-002 | Establish information security policy | Compliance | docs/compliance/evidence/iso/27001/policies/ | _pending_ | ? |
| ISO27001-RQ-003 | Perform risk assessment & treatment plan | Security | Risk register + treatment matrix | _pending_ | ? |
| ISO27001-RQ-004 | Implement Annex A controls (see 27002 package) | Security | GUIDE_DEV security sections, CI policies | _pending_ | ? |
| ISO27001-RQ-005 | Run internal ISMS audits and management review | Compliance | docs/compliance/evidence/iso/27001/audits/ | _pending_ | ? |

---

## Gap Analysis

- No centralised ISMS documentation yet; this package provides the foundation.  
- Security controls partially addressed in GUIDE_DEV (Five Priorities) but need formal mapping.  
- Risk assessment process exists for NASA standards; integrate with ISMS.

**Action Items (v2):**
1. Draft ISMS scope statement and governance model.  
2. Produce initial risk assessment covering all products.  
3. Align controls with 27002 package and track implementation owners.  
4. Plan first internal audit before v2 release freeze.

---

## Integration Points

- Architecture: Document security considerations and design decisions supporting ISMS controls.  
- Development: Enforce secure coding guidelines, dependency management, SBOM (GUIDE_DEV).  
- Operations: Extend CI/CD to enforce control checks (access control, logging, vulnerability scanning).  
- Documentation: Maintain policies and procedures under `docs/compliance/evidence/iso/27001/`.

---

## Evidence

- Placeholder: create directories as artefacts are produced.  
- Link security policy documents, risk logs, audit reports.

---

## Notes

- Coordinate with NIST SP 800-53 package to avoid duplicate control mapping.  
- Update status during each compliance review meeting; escalate risks to Architecture Board.


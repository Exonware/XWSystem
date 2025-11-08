# Mars Standard Roadmap

**Goal:** Achieve aerospace-grade reliability and compliance across the eXonware ecosystem by Version 4.x.  
**Authority:** CTO Office & Architecture Board

---

## Milestones

| Milestone | Target Version | Focus Areas | Exit Criteria |
|-----------|----------------|-------------|---------------|
| **MS0 � Foundation** | v0.x | Architecture scaffolding, compliance structure | GUIDE_COMP + docs/compliance/ tree in place, baseline risk register |
| **MS1 � Production Readiness** | v1.x | Hardened Python stack, partial NASA/ECSS compliance | All NASA/ECSS Level B controls covered; security controls mapped |
| **MS2 � Draft Mars Standard** | v2.x | Full compliance packages for NASA/ECSS/DO-178C/ISO/NIST/AI (documentation + plans) | Gap analyses closed or tracked with action plans; AI governance process established |
| **MS3 � Multi-language Transition** | v3.x | Rust core, Go/TS facades, cross-language compliance | Standards revalidated for new runtime; shared evidence pipeline operational |
| **MS4 � Full Mars Standard** | v4.x | Certification and external audit readiness | External assessment reports, certifications obtained, continuous compliance processes running |

---

## Tracking Checklist

- [ ] NASA compliance package migrated and current  
- [ ] ECSS compliance package migrated and current  
- [ ] DO-178C compliance package migrated and current  
- [ ] CCSDS interoperability plan documented  
- [ ] ISO/IEC 27001/27002/27017/27018 packages authored (requirements, controls, status)  
- [ ] ISO/IEC 9001 & lifecycle standards (12207/15288/15504) summarised and mapped  
- [ ] NIST SP 800 series controls documented with implementation owners  
- [ ] AI governance folders populated (NIST AI RMF, ISO/IEC 23894, ISO/IEC 42001, EU AI Act)  
- [ ] Risk register merged into central format  
- [ ] Traceability automation operational (code ? test ? evidence)  
- [ ] Evidence repository populated per release

Update this list at the close of every release cycle. Link supporting documents and evidence below.

---

## Evidence & Reports

| Milestone | Evidence | Location | Status |
|-----------|----------|----------|--------|
| MS0 | Compliance structure defined | docs/compliance/ | ? |
| MS1 | NASA/ECSS Level B report | _pending_ | ?? |
| MS2 | ISO/NIST/AI gap closure | _pending_ | ? |
| MS3 | Multi-language compliance validation | _pending_ | ? |
| MS4 | External certification package | _pending_ | ? |

---

## Notes

- Existing analyses under `experiments/250902-mars-standard` remain the source of truth until migrated here.  
- Each library or service must contribute status updates via linked CHANGE/PROJECT documents.  
- The compliance team maintains a quarterly review cadence; outcomes must be logged in this folder.

---

*Keep this roadmap synchronized with GUIDE_COMP.md and ARCH/DEV guides. Deviations require Architecture Board approval.*


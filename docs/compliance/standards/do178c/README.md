# DO-178C Compliance

**Scope:** Software considerations in airborne systems and equipment certification (focus on Level A requirements).  
**Applicability:** Safety-critical modules, automation pipelines, and any deliverable positioned for aerospace usage (v2 onwards).  
**Priority:** High.  
**Last status review:** 08-Nov-2025 00:00 UTC � ? Not compliant (structure only; no evidence recorded).

---

## Requirements Register (initial)

| ID | Requirement | Owner | Implementation Artifact | Evidence | Status |
|----|-------------|-------|--------------------------|---------|--------|
| DO178C-LA-RQ-001 | Define system safety objectives & determine DAL | Architecture | risk-assessment/ | evidence/risk/ | ? |
| DO178C-LA-RQ-002 | Implement requirements-based testing & coverage | QA | verification/vv_metrics.md, tests/* | evidence/verification/ | ? |
| DO178C-LA-RQ-003 | Establish verification traceability (requirements ? code ? tests) | Compliance | traceability tooling (planned) | evidence/traceability/ | ? |
| DO178C-LA-RQ-004 | Strengthen configuration management & change control | DevOps | CHANGE/PROJECT workflow | evidence/do178c/cm/ | ? |
| DO178C-LA-RQ-005 | Plan and execute QA audits & quality assurance | QA | QA audit plan (pending) | evidence/do178c/audits/ | ? |
| DO178C-LA-RQ-006 | Maintain software lifecycle documentation (plans, standards) | Compliance | GUIDE_COMP, GUIDE_DEV references | evidence/lifecycle/ | ? |

Legend: ? complete � ?? in progress � ? not started.

---

## Gap Analysis

The 08-Nov-2025 review confirmed that DO-178C artefacts have not yet been produced:

| Gap | Clause / Objective | Current Status | Planned Actions |
|-----|--------------------|----------------|-----------------|
| Formal verification absent | DO-178C �6.4.4 | 0% | Execute Phase 1 formal verification plan |
| Requirements traceability lacking | DO-178C �4.6 | 0% | Build automated traceability system |
| V&V plan incomplete | DO-178C �6.0 | 40% | Produce comprehensive V&V plan (Phase 2) |
| Configuration management limited | DO-178C �7.0 | 70% | Enhance CM tooling/process (Phase 2) |
| QA audits missing | DO-178C �8.0 | 0% | Schedule audits, capture reports under evidence |

### Action Items (v2)
1. Assign DAL levels per subsystem and document in `risk_register.md`.  
2. Integrate requirements-based testing into CI (coverage metrics stored in `vv_metrics.md`).  
3. Expand CHANGE/PROJECT templates to capture CM/QA checkpoints.  
4. Capture findings in `docs/compliance/evidence/do178c/` and close out outstanding tasks from the compliance action plan.

---

## Integration Points

- Architecture: Safety-related ADRs must cite DO-178C considerations.  
- Development: Guide Dev already enforces root-cause and testing discipline; augment with DAL tagging.  
- Testing: Integrate DO-178C suites into CI; produce artifacts consumable by auditors.

---

## Evidence

- Store DO-178C artefacts under `docs/compliance/evidence/do178c/`.

---

## Notes

- Align DO-178C efforts with NASA/ECSS safety work to minimise duplication.  
- Update certification dependency map and escalate assumptions to the Architecture Board.


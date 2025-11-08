# eXonware Development Guides

**Last Updated:** 08-Nov-2025

---

## Overview

This directory contains all universal development guides for eXonware projects. These guides define **HOW TO** perform various development activities and apply to **ALL eXonware projects**, not just xwsystem.

**Key Principle:** Guides are methodology - they rarely change between projects.

---

## Complete Guide List

### Baseline Standards

**[GUIDE_MASTER.md](GUIDE_MASTER.md)** (~120 lines)
- Canonical shared constraints (Five Priorities, documentation placement, comment standards, lazy install mandate)
- Applies to every guide, repository, and contributor
- Update first when platform-wide standards change

**[GUIDE_ARCH.md](GUIDE_ARCH.md)** (~150 lines)
- Architecture playbook for all libraries, backend services, and front-end apps
- Defines layering, naming (I/A/X classes), design patterns, compliance roadmap
- Coordinates with GUIDE_DEV for developer-facing execution details

**[GUIDE_COMP.md](GUIDE_COMP.md)** (~170 lines)
- Compliance playbook covering NASA, ECSS, DO-178C, ISO, NIST, AI standards
- Defines evidence structure, traceability expectations, Mars Standard roadmap
- Drives additions to docs/compliance/ across all repositories
### Process & Workflow

> **Reminder:** For v0/v1 the emphasis is on keeping plans, references, and logs up to date. Automation (trace exports, ISO/NIST tooling) will roll in with the v2 compliance sprint.

**[GUIDE_PLAN.md](GUIDE_PLAN.md)** (~770 lines)
- Complete development lifecycle (IDEA → PLAN → DEV → TEST → RELEASE)
- 5-phase workflow with gates and feedback loops
- Integration points between phases and cross-cutting standards

**[REF_PLAN.md](../REF_PLAN.md)** (~1,020 lines)
- Planning reference and routing guide
- Plan templates, naming conventions, lifecycle mapping
- Traceability and compliance alignment during planning

---

### Phase I: Ideation

**[GUIDE_IDEA.md](GUIDE_IDEA.md)** (~620 lines)
- How to capture and evaluate ideas
- Evaluation criteria (5 Priorities, Impact vs Effort)
- Idea lifecycle (New ? Exploring ? Approved/Rejected/Deferred)
- Templates for different idea types

**[GUIDE_PROJECT.md](GUIDE_PROJECT.md)** (~270 lines)
- How to gather requirements
- Functional and non-functional requirements
- Constraints and milestones
- REF_PROJECT.md creation process

---

### Phase II: Planning

**[REF_PLAN.md](../REF_PLAN.md)** (~1,020 lines)
- How to create and manage execution plans
- Plan types (DEV, TEST, DOCS, PROJECT, BENCH, MIXED)
- Routing to appropriate standards
- Plan lifecycle management and quality checklists

---

### Phase III: Development

**[GUIDE_DEV.md](GUIDE_DEV.md)** (~2,015 lines)
- Development philosophy and standards
- eXonware 5 Priorities
- Code quality standards
- Security, usability, maintainability focus

---

### Phase IV: Quality Loop

**[GUIDE_TEST.md](GUIDE_TEST.md)** (~3,730 lines)
- Testing strategy and implementation
- 4-layer test architecture
- pytest standards and conventions
- Test runners and organization

**[GUIDE_BENCH.md](GUIDE_BENCH.md)** (~740 lines)
- Benchmarking standards
- Writing and running benchmarks
- Performance testing methodology
- SLA verification

---

### Phase V: Documentation

**[GUIDE_DOCS.md](GUIDE_DOCS.md)** (~3,690 lines)
- Documentation standards and templates
- File placement rules
- Naming conventions
- Templates for all document types

**[GUIDE_USAGE.md](GUIDE_USAGE.md)** (~315 lines)
- How to use xwsystem library
- Installation and basic usage
- Common use cases
- Examples and best practices

---

## Guides by Category

### Workflow Guides
| Guide | Phase | Purpose |
|-------|-------|---------|
| GUIDE_PLAN | All | Complete development lifecycle |

### Ideation Guides
| Guide | Phase | Purpose |
|-------|-------|---------|
| GUIDE_IDEA | I.1 | Capture and evaluate ideas |
| GUIDE_PROJECT | I.2 | Gather requirements |

### Execution Guides
| Guide | Phase | Purpose |
|-------|-------|---------|
| REF_PLAN | II | Planning templates & routing |
| GUIDE_DEV | III | Development standards |

### Quality Guides
| Guide | Phase | Purpose |
|-------|-------|---------|
| GUIDE_TEST | IV | Testing approach |
| GUIDE_BENCH | IV | Benchmarking standards |

### Documentation Guides
| Guide | Phase | Purpose |
|-------|-------|---------|
| GUIDE_DOCS | All | Documentation standards |
| GUIDE_USAGE | V | Usage documentation |

---

## Guide Statistics

**Total Guides:** 9  
**Total Lines:** ~12,170  
**Average Length:** ~1,352 lines

**By Length:**
- GUIDE_DOCS.md - 3,690 lines (largest)
- GUIDE_TEST.md - 3,730 lines
- GUIDE_DEV.md - 2,015 lines
- REF_PLAN.md - 1,020 lines
- GUIDE_PLAN.md - 770 lines
- GUIDE_BENCH.md - 740 lines
- GUIDE_IDEA.md - 620 lines
- GUIDE_USAGE.md - 315 lines
- GUIDE_PROJECT.md - 270 lines (smallest)

---

## How to Use These Guides

### For New Projects

1. Copy entire `guides/` folder to new project
2. Customize GUIDE_USAGE.md for the specific library
3. All other guides remain unchanged
4. Create project-specific REF_* documents

### For AI Assistants

**Essential Reading Order:**
1. GUIDE_PLAN - Understand the complete workflow
2. GUIDE_DOCS - Learn documentation rules
3. Phase-specific guides as needed

**Quick Reference:**
- Starting idea ? GUIDE_IDEA
- Defining requirements ? GUIDE_PROJECT
- Creating plan ? GUIDE_PLAN
- Writing code ? GUIDE_DEV
- Writing tests ? GUIDE_TEST
- Running benchmarks ? GUIDE_BENCH
- Documenting ? GUIDE_DOCS

### For Human Developers

**Start with:**
1. GUIDE_PLAN - Big picture
2. GUIDE_USAGE - How to use the library
3. Phase guides as you work through development

---

## Guide Maintenance

### When to Update Guides

**Rarely** - Guides are methodology:
- Major process improvements
- New best practices discovered
- Tool/framework changes (e.g., pytest upgrade)
- eXonware priority adjustments

### Update Process

1. Update guide document
2. Document change in guide's version history
3. Notify all projects using the guide
4. Ensure backward compatibility
5. Update this INDEX

---

## Related Documentation

**Project-Specific References:**
- [../REF_IDEA.md](../REF_IDEA.md) - xwsystem ideas
- [../REF_PROJECT.md](../REF_PROJECT.md) - xwsystem requirements
- [../REF_ARCH.md](../REF_ARCH.md) - xwsystem architecture
- [../REF_BENCH.md](../REF_BENCH.md) - xwsystem SLAs

**Main Navigation:**
- [../INDEX.md](../INDEX.md) - Documentation index

---

*Universal guides for consistent, high-quality development across all eXonware projects*



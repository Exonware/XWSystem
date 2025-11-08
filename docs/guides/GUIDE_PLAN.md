# Development Lifecycle & Planning Guide

**Company:** eXonware.com  
**Author:** Eng. Muhammad AlShehri  
**Email:** connect@exonware.com  
**Version:** 0.0.2  
**Last Updated:** 08-Nov-2025

---

## Overview

This guide defines the complete development lifecycle for eXonware projects, from initial idea to production release. Follow this flow for consistent, high-quality delivery across all projects.

**Related Documents:**
- [GUIDE_MASTER.md](GUIDE_MASTER.md) - Master standards and shared constraints
- [GUIDE_IDEA.md](GUIDE_IDEA.md) - Idea capture and evaluation
- [GUIDE_PROJECT.md](GUIDE_PROJECT.md) - Requirements gathering
- [REF_PLAN.md](../REF_PLAN.md) - Planning reference (templates, routing)
- [GUIDE_DEV.md](GUIDE_DEV.md) - Development standards
- [GUIDE_TEST.md](GUIDE_TEST.md) - Testing standards
- [GUIDE_BENCH.md](GUIDE_BENCH.md) - Benchmarking standards
- [GUIDE_DOCS.md](GUIDE_DOCS.md) - Documentation standards

---

## 5-Phase Development Lifecycle

```
IDEATION → PLANNING → DEVELOPMENT → QUALITY LOOP → RELEASE
```

Each phase has specific deliverables, documents, and quality gates. Complete each phase before moving to the next.

---

## Phase I: Ideation

**Goal:** Transform raw ideas into validated requirements and technical designs

### I.1 Capture Ideas

**Document:** `REF_IDEA.md`  
**Guide:** [GUIDE_IDEA.md](GUIDE_IDEA.md)

**Activities:**
- Document problem statements
- Brainstorm solutions
- Identify stakeholders
- Assess feasibility
- Estimate scope
- Evaluate using criteria

**Exit Criteria:**
- Problem clearly defined
- Solution direction identified
- Stakeholders aligned
- Idea approved for requirements

---

### I.2 Define Requirements

**Document:** `REF_PROJECT.md`  
**Guide:** [GUIDE_PROJECT.md](GUIDE_PROJECT.md)

**Activities:**
- Gather functional requirements
- Define non-functional requirements (5 Priorities)
- Document constraints
- Create milestones
- Define success criteria

**Exit Criteria:**
- All requirements documented
- Priorities assigned
- Success metrics defined

**eXonware 5 Priorities:**
1. Security
2. Usability
3. Maintainability
4. Performance
5. Extensibility

---

### I.3 Design Architecture

**Document:** `REF_ARCH.md`

**Activities:**
- Design system architecture
- Choose design patterns
- Define modules and interfaces
- Plan data flow
- Identify extensibility points

**Exit Criteria:**
- Architecture documented
- Patterns selected
- Module boundaries clear

---

## Phase II: Planning

**Goal:** Break work into executable, trackable plans

### P.1 Create Plan

**Document:** `docs/plans/PLAN_YYYYMMDD_HHMM_DESCRIPTION.md`  
**Guide:** [REF_PLAN.md](../REF_PLAN.md)

**Plan Types:**
- **DEV** - Development work
- **TEST** - Testing initiatives
- **DOCS** - Documentation projects
- **PROJECT** - Requirements/milestones
- **BENCH** - Benchmarking initiatives
- **MIXED** - Multi-discipline work

**Activities:**
- Choose plan type
- Follow appropriate guide (DEV/TEST/DOCS/PROJECT/BENCH)
- Define tasks and success criteria
- Estimate effort
- Identify dependencies

**Exit Criteria:**
- Plan created with clear tasks
- Success criteria defined
- Dependencies identified

**Metadata (v2 automation ready):**
- You can optionally add lines such as `Requirement ID: ...`, `Components: ...`, `Verification: ...`. These feed the traceability matrix once the automation tools arrive in v2.
- If you skip them for now, make sure the PLAN still links to the relevant CHANGE/TEST/PROJECT docs manually—the goal is to keep planning lightweight and focused on the current work until the automation tooling lands in v2.

---

### P.2 Log Planning

**Document:** `logs/SUMMARY_PLAN.md`

**Activities:**
- Add entry to planning log
- Link to plan document
- Set status (Planned)

**Exit Criteria:**
- Plan logged and tracked

---

## Phase III: Development

**Goal:** Implement solution following eXonware standards

### D.1 Implement Code

**Guide:** [GUIDE_DEV.md](GUIDE_DEV.md)

**Activities:**
- Write code following standards
- Apply eXonware 5 Priorities
- Add comprehensive comments (WHY, not WHAT)
- Include file path comments
- Validate inputs
- Handle errors properly

**Key Principles:**
- Security first
- Never remove features
- Never reinvent wheel
- Think thoroughly first
- Root cause analysis for bugs

**Exit Criteria:**
- Code written and working
- Standards followed
- Comments complete

---

### D.2 Document Changes

**Document:** `docs/changes/CHANGE_YYYYMMDD_HHMM_DESCRIPTION.md`  
**Guide:** [GUIDE_DOCS.md](GUIDE_DOCS.md)

**Activities:**
- Create change document
- Explain what changed
- Document why it changed
- List impact and affected components
- Link related tests

**Exit Criteria:**
- Change documented thoroughly
- Rationale clear
- Impact assessed

---

### D.3 Log Changes

**Document:** `logs/SUMMARY_CHANGE.md`

**Activities:**
- Add entry to change log
- Link to CHANGE_* document
- Update version if needed

**Exit Criteria:**
- Change logged and versioned

---

## Phase IV: Quality Loop

**Goal:** Achieve excellence through iterative testing and optimization

This phase loops until all quality gates pass.

### Q.1 Write Tests

**Guide:** [GUIDE_TEST.md](GUIDE_TEST.md)

**Test Layers (run in order):**
1. **0.core/** - High-value tests (80/20 rule)
2. **1.unit/** - Component isolation
3. **2.integration/** - Cross-module scenarios
4. **3.advance/** - Excellence tests (5 priorities)

**Activities:**
- Write comprehensive tests
- Cover edge cases
- Test error handling
- Validate security
- Check usability

**Exit Criteria:**
- Tests written for all layers
- Edge cases covered
- Security validated

---

### Q.2 Run Tests

**Activities:**
- Run pytest with appropriate layers
- Check coverage
- Analyze failures

**Commands:**
```bash
# Run core tests (quick feedback)
pytest tests/0.core/

# Run unit tests
pytest tests/1.unit/

# Run integration tests
pytest tests/2.integration/

# Run all tests
pytest tests/
```

**Exit Criteria:**
- All tests executed
- Results documented

---

### Q.3 Log Test Results

**Document:** `logs/SUMMARY_TEST.md`

**Activities:**
- Record test run date/time
- Log pass/fail counts
- Note coverage percentage
- Document issues found

**Exit Criteria:**
- Test run logged

---

### Q.4 Fix Issues (if tests fail)

**Guide:** [GUIDE_DEV.md](GUIDE_DEV.md)

**Activities:**
- Perform root cause analysis
- Fix underlying issues (not symptoms)
- Update code
- Document fix in CHANGE_* if significant

**Exit Criteria:**
- Root cause identified
- Fix implemented
- Issue resolved

**Loop:** Return to Q.2 (Run Tests)

---

### Q.5 Run Benchmarks

**Guide:** [GUIDE_BENCH.md](GUIDE_BENCH.md)  
**Reference:** [REF_BENCH.md](../REF_BENCH.md)

**Activities:**
- Run performance benchmarks
- Compare against SLAs
- Check NFRs compliance
- Identify regressions

**Exit Criteria:**
- Benchmarks executed
- Performance measured

---

### Q.6 Log Benchmark Results

**Document:** `logs/benchmarks/INDEX.md`  
**Storage:** `docs/benchmarks/BENCH_YYYYMMDD_HHMM_DESCRIPTION.md`

**Activities:**
- Record benchmark metrics
- Compare to baseline
- Note regressions or improvements
- Store detailed results

**Exit Criteria:**
- Benchmarks logged
- Results stored

---

### Q.7 Optimize (if performance poor)

**Guide:** [GUIDE_DEV.md](GUIDE_DEV.md)

**Activities:**
- Profile code
- Identify bottlenecks
- Implement optimizations
- Maintain code quality

**Exit Criteria:**
- Performance meets SLAs
- NFRs satisfied

**Loop:** Return to Q.2 (Run Tests) to validate optimizations

---

### Q.8 Quality Gate Check

**Check ALL:**
- ✅ All tests pass (4 layers)
- ✅ Coverage ≥ 90%
- ✅ Benchmarks meet SLAs
- ✅ NFRs satisfied
- ✅ Security validated
- ✅ No regressions

**If ANY fail:** Loop back to appropriate step (Q.4 or Q.7)

**If ALL pass:** Proceed to Phase V

---

## Phase V: Release

**Goal:** Document and release production-ready features

### R.1 Document API

**Document:** `REF_API.md`  
**Guide:** [GUIDE_DOCS.md](GUIDE_DOCS.md)

**Activities:**
- Document all public APIs
- Include parameters and return types
- Add usage examples
- Show error handling

**Exit Criteria:**
- 100% API coverage
- Examples clear and tested

---

### R.2 Create Usage Guide

**Document:** `GUIDE_USAGE.md`  
**Guide:** [GUIDE_DOCS.md](GUIDE_DOCS.md)

**Activities:**
- Write usage examples
- Document common use cases
- Explain best practices
- Add troubleshooting section

**Exit Criteria:**
- Users can understand how to use features
- Examples comprehensive
- Common scenarios covered

---

### R.3 Create Milestone Report

**Document:** `docs/project/PROJECT_YYYYMMDD_HHMM_DESCRIPTION.md`

**Activities:**
- Summarize milestone achievements
- Report metrics (tests, coverage, performance)
- Document lessons learned
- Plan next phase

**Exit Criteria:**
- Milestone documented
- Metrics reported
- Lessons captured

---

### R.4 Log Project Update

**Document:** `logs/SUMMARY_PROJECT.md`

**Activities:**
- Add milestone entry
- Link to PROJECT_* document
- Update project timeline

**Exit Criteria:**
- Milestone logged

---

### R.5 Update Project Status

**Document:** `REF_PROJECT.md#project-status-overview`

**Activities:**
- Update feature completion status
- Refresh roadmap
- Update metrics
- Revise timelines if needed

**Exit Criteria:**
- Current status reflected
- Stakeholders informed

---

### R.6 Update Changelog

**Document:** `CHANGELOG.md`

**Activities:**
- Add version entry
- List changes (Added, Changed, Fixed, Removed)
- Link to detailed CHANGE_* documents
- Follow Keep a Changelog format

**Exit Criteria:**
- User-facing changes documented
- Version published

---

## Document Map by Phase

### Phase I: Ideation

| Document | Purpose | Template |
|----------|---------|----------|
| REF_IDEA.md | Idea capture | Yes |
| REF_PROJECT.md | Requirements | Yes |
| REF_ARCH.md | Architecture | Yes |

### Phase II: Planning

| Document | Purpose | Location |
|----------|---------|----------|
| PLAN_*.md | Executable plan | docs/plans/ |
| logs/SUMMARY_PLAN.md | Planning history | docs/ |

### Phase III: Development

| Document | Purpose | Location |
|----------|---------|----------|
| Source code | Implementation | src/ |
| CHANGE_*.md | Change log | docs/changes/ |
| logs/SUMMARY_CHANGE.md | Version history | docs/ |

### Phase IV: Quality Loop

| Document | Purpose | Location |
|----------|---------|----------|
| Test files | Test code | tests/ |
| logs/SUMMARY_TEST.md | Test history | docs/ |
| BENCH_*.md | Benchmark results | docs/benchmarks/ |
| logs/benchmarks/INDEX.md | Benchmark history | docs/ |

### Phase V: Release

| Document | Purpose | Location |
|----------|---------|----------|
| REF_API.md | API reference | docs/ |
| GUIDE_USAGE.md | Usage guide | docs/ |
| PROJECT_*.md | Milestone report | docs/project/ |
| logs/SUMMARY_PROJECT.md | Project history | docs/ |
| REF_PROJECT.md#project-status-overview | Current status | docs/ |
| CHANGELOG.md | User changelog | docs/ |

---

## Quick Reference

### Starting New Feature

```
1. Ideation: Update REF_IDEA, REF_PROJECT, REF_ARCH
2. Planning: Create PLAN_YYYYMMDD_HHMM_*.md
3. Development: Code + CHANGE_YYYYMMDD_HHMM_*.md
4. Quality: Test → Fix → Benchmark (loop until pass)
5. Release: Update docs, create PROJECT_*, update CHANGELOG
```

### Fixing Bug

```
1. Root cause analysis (GUIDE_DEV.md)
2. Create PLAN_* for complex bugs
3. Fix code (Phase III)
4. Document in CHANGE_* (Phase III)
5. Add regression test (Phase IV)
6. Verify benchmarks (Phase IV)
7. Update CHANGELOG (Phase V)
```

### Reaching Milestone

```
1. Verify all quality gates passed
2. Create PROJECT_YYYYMMDD_HHMM_*.md
3. Update logs/SUMMARY_PROJECT.md
4. Update REF_PROJECT.md#project-status-overview
5. Update CHANGELOG.md
6. Celebrate success
```

---

## Quality Gates by Phase

### Phase I Exit: Ideation Complete
- ✅ Problem defined clearly
- ✅ Requirements documented
- ✅ Architecture designed
- ✅ Feasibility confirmed

### Phase II Exit: Planning Complete
- ✅ Plan created and detailed
- ✅ Tasks defined
- ✅ Success criteria clear
- ✅ Plan logged

### Phase III Exit: Development Complete
- ✅ Code implemented
- ✅ Standards followed
- ✅ Changes documented
- ✅ Changes logged

### Phase IV Exit: Quality Verified
- ✅ All tests pass
- ✅ Coverage ≥ 90%
- ✅ Benchmarks meet SLAs
- ✅ No regressions
- ✅ Security validated

### Phase V Exit: Release Ready
- ✅ API documented
- ✅ Usage guide complete
- ✅ Milestone reported
- ✅ Status updated
- ✅ Changelog published

---

## Best Practices

### For All Phases

1. **Document as you go** - Don't wait until the end
2. **Follow the guides** - Each phase has specific standards
3. **Verify quality gates** - Don't skip gates
4. **Loop when needed** - Quality loop is iterative by design
5. **Keep stakeholders informed** - Update status regularly

### For Teams

1. **One phase at a time** - Don't jump ahead
2. **Complete documentation** - Others depend on it
3. **Clear handoffs** - Document decisions and context
4. **Consistent naming** - Follow conventions strictly
5. **Review regularly** - Catch issues early

### For AI Agents

1. **Read guides first** - Understand standards before acting
2. **Follow phase order** - Respect the workflow
3. **Document thoroughly** - Future context depends on it
4. **Verify gates** - Don't assume quality
5. **Loop when needed** - Quality takes iteration

---

## Common Patterns

### Pattern: Small Feature

```
Phases: I (brief), II (simple plan), III (code + doc), IV (test + bench), V (update guides)
Time: 1-3 days
Documents: PLAN, CHANGE, tests, BENCH, CHANGELOG entry
```

### Pattern: Large Feature

```
Phases: I (thorough), II (detailed plan), III (multiple CHANGEs), IV (extensive tests), V (PROJECT report)
Time: 1-4 weeks
Documents: Full suite (PLAN, multiple CHANGEs, PROJECT, full docs update)
```

### Pattern: Bug Fix (Simple)

```
Phases: Skip I, quick PLAN, III (fix + CHANGE), IV (regression test), V (CHANGELOG)
Time: Hours to 1 day
Documents: PLAN (optional), CHANGE, test, CHANGELOG entry
```

### Pattern: Bug Fix (Complex)

```
Phases: I (analysis), II (detailed PLAN), III (fix + CHANGE), IV (comprehensive tests), V (full docs)
Time: 2-7 days
Documents: Full workflow (same as small feature)
```

### Pattern: Performance Optimization

```
Phases: I (benchmark analysis), II (optimization PLAN), III (code changes), IV (extensive benchmarking), V (BENCH report)
Time: 1-2 weeks
Documents: PLAN, CHANGE, extensive BENCHs, PROJECT or CHANGELOG
```

### Pattern: Refactoring

```
Phases: I (impact analysis), II (detailed PLAN), III (careful changes), IV (regression testing), V (architecture docs)
Time: 1-3 weeks
Documents: PLAN, CHANGEs, tests, REF_ARCH update
```

---

## Integration with Existing Guides

This flow guide orchestrates all other guides:

- **GUIDE_DEV.md** - Follow during Phase III (Development)
- **GUIDE_TEST.md** - Follow during Phase IV (Quality Loop)
- **GUIDE_DOCS.md** - Follow during all phases for documentation
- **REF_PLAN.md** - Follow during Phase II (Planning)
- **GUIDE_PROJECT.md** - Follow during Phase I (Requirements)
- **GUIDE_BENCH.md** - Follow during Phase IV (Benchmarking)

Each guide provides detailed HOW-TO for its domain. This flow provides the WHEN and ORDER.

---

## Flexibility and Adaptation

### When to Adapt the Flow

**You may simplify for:**
- Trivial fixes (typos, comments)
- Documentation updates
- Simple configuration changes

**You must follow strictly for:**
- New features
- Architecture changes
- Security updates
- Performance optimization
- Breaking changes

### Tailoring by Project Type

**Library Development:**
- Emphasize Phase IV (thorough testing)
- Detailed Phase V (comprehensive docs)

**Application Development:**
- Emphasize Phase I (clear requirements)
- Focus on usability throughout

**Internal Tools:**
- Lighter documentation acceptable
- Still maintain quality gates

---

## Continuous Improvement

### Learning from Each Cycle

After each release (Phase V), reflect:

1. What worked well?
2. What could improve?
3. Were estimates accurate?
4. Did quality gates catch issues?
5. Is documentation sufficient?

Document lessons in PROJECT_* reports for continuous improvement.

---

## Related Documentation

**Standards & Guides:**
- [GUIDE_DEV.md](GUIDE_DEV.md) - Development standards
- [GUIDE_TEST.md](GUIDE_TEST.md) - Testing standards
- [GUIDE_DOCS.md](GUIDE_DOCS.md) - Documentation standards
- [REF_PLAN.md](../REF_PLAN.md) - Planning standards
- [GUIDE_PROJECT.md](GUIDE_PROJECT.md) - Requirements standards
- [GUIDE_BENCH.md](GUIDE_BENCH.md) - Benchmarking standards

**References:**
- [REF_PROJECT.md](../REF_PROJECT.md) - Project requirements
- [REF_ARCH.md](../REF_ARCH.md) - Architecture
- [REF_IDEA.md](../REF_IDEA.md) - Idea templates
- [REF_BENCH.md](../REF_BENCH.md) - Performance SLAs

**Logs:**
- [logs/SUMMARY_PLAN.md](../logs/SUMMARY_PLAN.md) - Planning history
- [logs/SUMMARY_CHANGE.md](../logs/SUMMARY_CHANGE.md) - Version history
- [logs/SUMMARY_PROJECT.md](../logs/SUMMARY_PROJECT.md) - Project milestones
- [logs/SUMMARY_TEST.md](../logs/SUMMARY_TEST.md) - Test history
- [logs/benchmarks/INDEX.md](../logs/benchmarks/INDEX.md) - Benchmark history

**Navigation:**
- [INDEX.md](INDEX.md) - Documentation index

---

*Follow this flow for consistent, high-quality delivery across all eXonware projects*




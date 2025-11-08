# Benchmarking Guide

**Company:** eXonware.com  
**Author:** Eng. Muhammad AlShehri  
**Email:** connect@exonware.com  
**Version:** 0.0.1  
**Last Updated:** 06-Nov-2025

---

## Overview

This guide defines how to create, run, and manage performance benchmarks in eXonware projects. Benchmarks verify that code meets performance requirements and detect regressions.

-**Related Documents:**
- [GUIDE_MASTER.md](GUIDE_MASTER.md) - Shared engineering standards
- [REF_BENCH.md](../REF_BENCH.md) - Performance SLAs and NFRs
- [logs/benchmarks/INDEX.md](../logs/benchmarks/INDEX.md) - Benchmark history
- [GUIDE_TEST.md](GUIDE_TEST.md) - Testing standards
- [GUIDE_PLAN.md](GUIDE_PLAN.md) - Development flow

---

## Table of Contents

1. [Benchmarking Philosophy](#benchmarking-philosophy)
2. [When to Benchmark](#when-to-benchmark)
3. [Benchmark Structure](#benchmark-structure)
4. [Writing Benchmarks](#writing-benchmarks)
5. [Running Benchmarks](#running-benchmarks)
6. [Analyzing Results](#analyzing-results)
7. [Documentation Standards](#documentation-standards)
8. [Best Practices](#best-practices)
9. [Benchmark Templates](#benchmark-templates)

---

## Benchmarking Philosophy

### Core Principles

1. **Measure, don't guess** - Performance claims require data
2. **Compare fairly** - Benchmark same conditions
3. **Isolate variables** - Change one thing at a time
4. **Repeat for consistency** - Run multiple iterations
5. **Document context** - Hardware, OS, Python version matter

### Why We Benchmark

**Without Benchmarking:**
- ? Unknown performance characteristics
- ? Undetected regressions
- ? No basis for optimization claims
- ? Missed SLA violations

**With Benchmarking:**
- ? Verified performance metrics
- ? Early regression detection
- ? Data-driven optimization
- ? SLA compliance tracking

### eXonware Performance Priority

Performance is the **4th priority** in eXonware (after Security, Usability, Maintainability). Benchmarks should:

1. Not compromise security
2. Not reduce usability
3. Be maintainable
4. Verify performance targets
5. Support extensibility

---

## When to Benchmark

### Always Benchmark

1. **Critical Path Code** - Code executed frequently
2. **I/O Operations** - Serialization, file ops, network
3. **Data Processing** - Large dataset operations
4. **Caching Systems** - Cache hit/miss performance
5. **Algorithm Changes** - New algorithms or optimizations
6. **Release Milestones** - Before each version release

### Consider Benchmarking

1. **Utility Functions** - If used in hot paths
2. **Data Structures** - Custom collections
3. **Parsing** - Text or binary parsing
4. **Compression** - Compression/decompression ops

### Skip Benchmarking

1. **Trivial Functions** - Simple getters/setters
2. **One-time Setup** - Initialization code
3. **UI Code** - Unless response time critical
4. **Test Code** - Tests themselves don't need benchmarks

---

## Benchmark Structure

### Directory Organization

```
docs/logs/benchmarks/
+-- INDEX.md                            # Benchmarks index
+-- TEMPLATE.md                         # Standard report template
+-- BENCH_YYYYMMDD_HHMM_DESCRIPTION.md  # Detailed results
+-- baseline/                           # Baseline measurements
    +-- v0.0.1_baseline.md
    +-- v1.0.0_baseline.md
```

### Benchmark Code Location

```
tests/
+-- 0.core/
+-- 1.unit/
+-- 2.integration/
+-- 3.advance/
    +-- benchmarks/              # Benchmark test files
        +-- bench_serialization.py
        +-- bench_caching.py
        +-- bench_io.py
```

**Why in 3.advance?** Benchmarks validate excellence (Performance priority #4), making them advance-level tests.

---

## Writing Benchmarks

### Using pytest-benchmark

**Install:**
```bash
pip install pytest-benchmark
```

### Basic Benchmark Structure

```python
# tests/3.advance/benchmarks/bench_example.py

"""
Benchmarks for example module

WHY: Verify performance meets SLAs defined in REF_BENCH.md
"""

import pytest


def test_benchmark_function_name(benchmark):
    """
    Benchmark function description
    
    SLA: < 50ms for 1MB data (REF_BENCH.md)
    """
    # Setup
    data = create_test_data(size=1_000_000)
    
    # Benchmark
    result = benchmark(function_to_test, data)
    
    # Verify result (correctness)
    assert result is not None


def test_benchmark_with_params(benchmark):
    """
    Benchmark with different parameter sizes
    
    SLA: Linear scaling O(n)
    """
    sizes = [100, 1_000, 10_000]
    
    for size in sizes:
        data = create_test_data(size=size)
        result = benchmark(function_to_test, data)
        assert result is not None
```

### Advanced Benchmark Patterns

#### Setup/Teardown

```python
def test_benchmark_with_setup(benchmark):
    """
    Benchmark excluding setup time
    
    WHY: Setup time shouldn't affect measurement
    """
    def setup():
        return create_expensive_data()
    
    def teardown(data):
        cleanup(data)
    
    result = benchmark.pedantic(
        function_to_test,
        setup=setup,
        teardown=teardown,
        rounds=100,
        iterations=10
    )
```

#### Warmup Rounds

```python
def test_benchmark_with_warmup(benchmark):
    """
    Benchmark with warmup for JIT/cache effects
    
    WHY: First runs may be slower (cold cache)
    """
    benchmark.pedantic(
        function_to_test,
        rounds=100,
        iterations=10,
        warmup_rounds=5  # Discard first 5 rounds
    )
```

#### Memory Profiling

```python
import tracemalloc


def test_benchmark_memory(benchmark):
    """
    Benchmark memory usage
    
    SLA: < 3MB for 1MB data
    """
    def measure_memory():
        tracemalloc.start()
        result = function_to_test(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return peak / 1024 / 1024  # Convert to MB
    
    data = create_test_data(size=1_000_000)
    memory_mb = benchmark(measure_memory)
    
    # Verify SLA
    assert memory_mb < 3.0, f"Memory usage {memory_mb}MB exceeds 3MB SLA"
```

---

## Running Benchmarks

### Basic Execution

```bash
# Run all benchmarks
pytest tests/3.advance/benchmarks/ --benchmark-only

# Run specific benchmark file
pytest tests/3.advance/benchmarks/bench_serialization.py --benchmark-only

# Run with verbose output
pytest tests/3.advance/benchmarks/ --benchmark-only -v
```

### Comparison Runs

```bash
# Save baseline
pytest tests/3.advance/benchmarks/ --benchmark-only --benchmark-save=baseline

# Compare to baseline
pytest tests/3.advance/benchmarks/ --benchmark-only --benchmark-compare=baseline

# Compare and fail if regression
pytest tests/3.advance/benchmarks/ --benchmark-only \
  --benchmark-compare=baseline \
  --benchmark-compare-fail=mean:10%  # Fail if 10% slower
```

### Output Formats

```bash
# JSON output
pytest tests/3.advance/benchmarks/ --benchmark-only --benchmark-json=results.json

# Histogram
pytest tests/3.advance/benchmarks/ --benchmark-only --benchmark-histogram=histogram

# Full report
pytest tests/3.advance/benchmarks/ --benchmark-only \
  --benchmark-verbose \
  --benchmark-columns=min,max,mean,stddev,median,ops
```

---

## Analyzing Results

### Understanding Output

```
Name                          Min      Max     Mean   StdDev   Median      Ops
test_benchmark_serialize   42.5ms   48.2ms   45.1ms   1.8ms   44.9ms   22.17
```

**Key Metrics:**
- **Min** - Best case performance
- **Max** - Worst case performance
- **Mean** - Average performance (use for SLA comparison)
- **StdDev** - Consistency (lower is better)
- **Median** - Middle value (robust to outliers)
- **Ops** - Operations per second

### SLA Compliance Check

```python
def test_benchmark_sla_compliance(benchmark):
    """
    Verify serialization meets SLA
    
    SLA: Mean < 50ms for 1MB (REF_BENCH.md)
    """
    data = create_test_data(size=1_000_000)
    
    stats = benchmark.pedantic(
        serialize_function,
        args=(data,),
        rounds=100,
        iterations=1
    )
    
    # Access stats after benchmark
    mean_ms = stats.stats['mean'] * 1000  # Convert to ms
    assert mean_ms < 50, f"Mean {mean_ms:.1f}ms exceeds 50ms SLA"
```

### Regression Detection

Compare current run to baseline:

```bash
# After baseline is saved
pytest tests/3.advance/benchmarks/ --benchmark-only \
  --benchmark-compare=baseline \
  --benchmark-compare-fail=mean:5%
```

**Regression Thresholds:**
- **< 5% slower** - Acceptable variation
- **5-10% slower** - Investigate
- **> 10% slower** - Regression, must fix

---

### Release Gate Integration

1. **Baseline Contract:** Benchmark acceptance criteria mirror the SLA tables in `REF_BENCH.md`. Update that reference before changing thresholds in test code.  
2. **Quality Loop Enforcement:** Phase IV of `GUIDE_PLAN.md` requires running `tests/3.advance/benchmarks/` before any release sign-off. CI pipelines must execute the same target with `--benchmark-compare` against the current baseline and `--benchmark-compare-fail` using SLA deltas.  
3. **Blocker Policy:** Releases entering Phase V must show green benchmarks. Any mean latency, tail latency, or memory regression beyond approved tolerance blocks release until fixed or an SLA update is documented and approved in `REF_BENCH.md`.  
4. **Traceability:** Log every gating run in `docs/logs/benchmarks/INDEX.md` and link to the associated `CHANGE_*` or `PROJECT_*` document so reviewers can trace performance sign-off.

---

## Documentation Standards

### BENCH_* Document Format

**File:** `docs/logs/benchmarks/BENCH_YYYYMMDD_HHMM_DESCRIPTION.md`

**Template:** Use [logs/benchmarks/TEMPLATE.md](../logs/benchmarks/TEMPLATE.md) for creating benchmark reports.

**Required Sections:**
- Summary - Brief overview and status
- Configuration - Test environment details
- Results - Performance and memory tables
- Analysis - Findings, regressions, improvements
- Recommendations - Action items
- Raw Data - Full output or link to file

### logs/benchmarks/INDEX.md Entry Format

```markdown
## DD-MMM-YYYY HH:MM - Description

**Version:** 0.0.1.xxx  
**Document:** BENCH_YYYYMMDD_HHMM_DESCRIPTION.md

**Benchmarks Run:**
- Serialization (all formats)
- Memory usage
- Caching performance

**SLA Compliance:** ? All passing / ?? Some warnings / ? Failures

**Key Findings:**
- Finding 1
- Finding 2

**Regressions:** None / List regressions

**Next Steps:**
- Action items if any
```

---

## Best Practices

### Writing Benchmarks

1. **Isolate what you measure**
   - Exclude setup/teardown time
   - Measure one operation at a time

2. **Use realistic data**
   - Test with production-like data sizes
   - Cover typical use cases

3. **Run enough iterations**
   - Minimum 100 rounds for stability
   - More for micro-benchmarks

4. **Verify correctness first**
   - Benchmark should also assert correct output
   - Don't benchmark broken code

5. **Document SLA references**
   - Link to REF_BENCH.md
   - State expected performance

### Running Benchmarks

1. **Consistent environment**
   - Close other applications
   - Use same hardware when comparing
   - Note environment changes

2. **Regular schedule**
   - Run before each release
   - Run after performance changes
   - Run weekly/monthly for trends

3. **Save baselines**
   - Save baseline after each release
   - Compare to appropriate baseline
   - Update baselines when SLAs change

4. **CI Integration**
   - Run benchmarks in CI
   - Fail on regressions
   - Track trends over time

### Analyzing Results

1. **Look at distribution**
   - Mean for SLA compliance
   - StdDev for consistency
   - Max for worst-case planning

2. **Compare fairly**
   - Same environment
   - Same data size
   - Same Python version

3. **Investigate anomalies**
   - Unexpected slowdowns
   - High standard deviation
   - Sporadic failures

4. **Document findings**
   - Create BENCH_* document
   - Update logs/benchmarks/INDEX.md
   - Link to related CHANGEs

---

## Benchmark Templates

### Template: I/O Operation

```python
def test_benchmark_io_operation(benchmark):
    """
    Benchmark I/O operation
    
    SLA: < Xms for Y size (REF_BENCH.md)
    """
    # Setup data
    data = create_test_data(size=TARGET_SIZE)
    
    # Warm benchmark run and collect statistics
    stats = benchmark.pedantic(
        io_function,
        args=(data,),
        rounds=100,
        iterations=1,
        warmup_rounds=5
    )

    # Run the function once more outside timing to validate correctness
    output = io_function(data)
    assert output is not None

    # Check SLA using recorded statistics (seconds ? milliseconds)
    mean_ms = stats.stats['mean'] * 1000
    assert mean_ms < SLA_MS, f"Mean {mean_ms:.1f}ms exceeds {SLA_MS}ms SLA"
```

### Template: Scaling Test

```python
@pytest.mark.parametrize("size", [100, 1_000, 10_000, 100_000])
def test_benchmark_scaling(benchmark, size):
    """
    Verify linear scaling O(n)
    
    SLA: Linear performance scaling
    """
    data = create_test_data(size=size)
    
    benchmark.pedantic(
        function_to_test,
        args=(data,),
        rounds=50,
        iterations=1
    )
    
    # Analysis: Plot results to verify O(n)
```

### Template: Comparison

```python
@pytest.mark.parametrize("method", ["method_a", "method_b", "method_c"])
def test_benchmark_comparison(benchmark, method):
    """
    Compare different methods
    
    WHY: Identify fastest approach
    """
    data = create_test_data(size=1_000_000)
    func = get_method(method)
    
    benchmark.pedantic(
        func,
        args=(data,),
        rounds=100,
        iterations=1
    )
```

---

## Common Pitfalls

### ? Measuring Setup Time

```python
# BAD
def test_bad_benchmark(benchmark):
    def run():
        data = create_expensive_data()  # Measured!
        return process(data)
    
    benchmark(run)
```

```python
# GOOD
def test_good_benchmark(benchmark):
    data = create_expensive_data()  # Not measured
    benchmark(process, data)
```

### ? Not Warming Up

```python
# BAD - First run might be slow (cold cache)
benchmark(function_to_test, data)
```

```python
# GOOD - Warm up first
benchmark.pedantic(
    function_to_test,
    args=(data,),
    warmup_rounds=5
)
```

### ? Inconsistent Environment

```python
# BAD - Different conditions each run
# Sometimes with other apps open, different data sizes, etc.
```

```python
# GOOD - Documented, consistent environment
"""
Test Environment:
- Python 3.9.7
- CPU: Intel i7-9700K @ 3.6GHz
- RAM: 32GB DDR4
- OS: Windows 10
- Disk: SSD
- No other applications running
"""
```

### ? Ignoring Outliers

Look at full distribution, not just mean. High stddev indicates inconsistency worth investigating.

---

## SLA Management

### How to Update SLAs

**When SLAs need updating:**

1. **Better performance achieved**
   - Document improvement in BENCH_* report
   - Update REF_BENCH.md with new targets
   - Create new baseline
   - Update logs/benchmarks/INDEX.md

2. **SLA unrealistic**
   - Document why in BENCH_* report
   - Propose new SLA with rationale
   - Get approval
   - Update REF_BENCH.md
   - Note in logs/SUMMARY_PROJECT.md

3. **New operation added**
   - Run initial benchmarks
   - Set SLA based on results + 20% buffer
   - Document in REF_BENCH.md
   - Create baseline

### Tracking SLA Changes

**All SLA changes must be documented in:**
- REF_BENCH.md - Update SLA tables
- logs/benchmarks/INDEX.md - Note SLA change with rationale
- logs/SUMMARY_PROJECT.md - If significant milestone impact
- CHANGELOG.md - If user-facing impact

---

## Integration with Development Flow

Benchmarking fits into **Phase IV: Quality Loop** (GUIDE_PLAN.md):

```
Test ? Log Tests ? Fix Issues (loop) ? 
Benchmark ? Log Benchmarks ? Optimize (loop) ? 
Quality Gate Check
```

**When benchmarks fail:**
1. Analyze why (regression vs. new code)
2. Determine if SLA needs updating (REF_BENCH.md)
3. Optimize if regression
4. Document in CHANGE_* and BENCH_*
5. Re-run benchmarks
6. Loop until passing

---

## Tools and Libraries

### pytest-benchmark

**Install:**
```bash
pip install pytest-benchmark
```

**Documentation:** https://pytest-benchmark.readthedocs.io/

### memory_profiler

**Install:**
```bash
pip install memory-profiler
```

**Usage:**
```python
from memory_profiler import profile

@profile
def function_to_test():
    # Function code
    pass
```

### tracemalloc (Built-in)

```python
import tracemalloc

tracemalloc.start()
# Code to measure
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
```

### timeit (Built-in)

```python
import timeit

result = timeit.timeit(
    'function_to_test(data)',
    setup='from module import function_to_test; data = ...',
    number=1000
)
```

---

## Related Documentation

**Standards:**
- [GUIDE_TEST.md](GUIDE_TEST.md) - Testing standards
- [GUIDE_DEV.md](GUIDE_DEV.md) - Development standards
- [GUIDE_PLAN.md](GUIDE_PLAN.md) - Development flow

**References:**
- [REF_BENCH.md](../REF_BENCH.md) - Performance SLAs and NFRs

**Logs:**
- [logs/benchmarks/INDEX.md](../logs/benchmarks/INDEX.md) - Benchmark history
- [logs/SUMMARY_TEST.md](../logs/SUMMARY_TEST.md) - Test history

**Reports:**
- [logs/benchmarks/](../logs/benchmarks/) - Detailed benchmark results

---

*Measure performance, ensure quality, detect regressions*




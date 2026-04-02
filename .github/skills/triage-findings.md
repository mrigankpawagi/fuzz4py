---
name: Triage fuzzer findings
description: Analyze fuzzer output to classify and prioritize bugs
---

# Triage Fuzzer Findings

You are a bug triage expert. Your job is to analyze fuzzer output and classify findings by type.

## Inputs

Ask the user for:
1. **Findings location** — path to the fuzzer output or findings directory
2. **Interpreter info** — which Python interpreter and version produced the findings

## Workflow

### Step 1: Collect findings

Read the fuzzer output (stdout/stderr from `scripts/run.py`, etc.) or the files in the specified findings directory. Look for:

- **Crashes** — abnormal exit codes (segfault: `-11` on Linux, `0xC0000005` on Windows)
- **Fatal errors** — `"Fatal Python error"` in stderr
- **SystemError** — internal CPython consistency failures
- **Internal error dumps** — `"object address"`, `"object refcount"`, `"lost sys.stderr"`
- **Hangs/timeouts** — processes that don't terminate
- **Assertion failures** — `"Assertion"` in stderr (from C-level asserts)
- **Incorrect results** — semantic differences reported by the semantic fuzzer

### Step 2: Classify each finding

| Type | Criteria |
|------|----------|
| **Crash** | Segfault, heap corruption, or abnormal process termination |
| **Fatal error** | `Fatal Python error:` in stderr, internal error dump |
| **Internal error** | SystemError, assertion failure from C code |
| **Incorrect behavior** | Wrong results, wrong error attributes |
| **Hang** | Infinite loop or deadlock caused by interpreter internals |
| **Exception bypass** | Exception skips `try/except` handlers |
| **False positive** | Expected behavior, user error, or environment-specific |

### Step 3: Deduplicate

Group findings that share the same root cause. Signs of duplicates:
- Same crash address or error message
- Same code path (check tracebacks)
- Same monitoring event type or API function
- Triggered by the same underlying pattern

### Step 4: Prioritize

Order by:
1. Reproducibility (always > sometimes > rarely)
2. Impact scope (affects all users > specific configs > edge cases)
3. Type (crash > fatal error > hang > exception bypass > incorrect behavior)

### Step 5: Create finding records

For each unique bug, use the `create-reproducer` skill to create a minimal reproducer and save it in `findings/`.

### Step 6: Report

Provide a summary table:

```
| # | Type | Description | Reproducer |
|---|------|-------------|------------|
| 1 | Crash | sys.monitoring LINE callback crash | findings/cpython-313-monitoring-callback-crash/ |
| 2 | Bypass | JUMP callback bypasses try/except | findings/cpython-313-monitoring-exception-bypass/ |
```

## Common False Positives

- `RecursionError` — expected for deep recursion tests
- `MemoryError` — expected for large allocation tests
- `SyntaxError` — expected for malformed code
- Normal Python exceptions (TypeError, ValueError, etc.) from user code
- Timeout on very slow tests (not a hang)

# Fuzz4Py

Fuzz4Py is a fuzzing framework for finding bugs in Python interpreters. It generates diverse Python programs and tests them against interpreter implementations to discover crashes, internal errors, and semantic bugs.

> **Inspired by** [Fuzz4All](https://github.com/fuzz4all/fuzz4all/tree/main/Fuzz4All), [PyRTFuzz](https://github.com/awen-li/PyRTFuzz), and [DyFuzz](https://github.com/xiaxinmeng/DyFuzz).

## Bug Hall of Fame

| # | Bug | Interpreter | Link |
|---|-----|-------------|------|
| 1 | `SyntaxError` from `compile` has incorrect attributes | CPython 3.11–3.13 | [CPython #127927](https://github.com/python/cpython/issues/127927) |
| 2 | `sys.monitoring` LINE/CALL/INSTRUCTION exception bypass | CPython 3.13 | [findings](findings/cpython-313-monitoring-callback-crash/) |
| 3 | `sys.monitoring` JUMP/BRANCH exception bypass | CPython 3.13 | [findings](findings/cpython-313-monitoring-exception-bypass/) |
| 4 | `sys.monitoring` EXCEPTION_HANDLED infinite loop | CPython 3.13 | [findings](findings/cpython-313-monitoring-infinite-loop/) |

## Project Structure

```
.github/
  copilot-instructions.md      # Copilot coding guidelines for this repo
  skills/
    find-bugs.md                # Skill: end-to-end fuzzing campaign
scripts/
  run.py                        # Main fuzzer entry point (~900 test cases)
  generators.py                 # Programmatic test-case generators
  harness.py                    # Subprocess + in-process execution harness
  deep_fuzzer.py                # Targeted in-process tests
  semantic_fuzzer.py            # Semantic correctness tests
  aggressive_fuzzer.py          # Crash-focused tests
findings/
  README.md                     # Index of all discovered bugs
  cpython-313-*/                # Per-bug directories with READMEs and reproducers
```

## Quick Start

No external dependencies — everything uses the Python standard library.

```bash
# Run the main fuzzer against the default Python interpreter
python scripts/run.py --timeout 15

# Run targeted in-process tests
python scripts/deep_fuzzer.py

# Run semantic correctness tests
python scripts/semantic_fuzzer.py

# Run crash-focused tests
python scripts/aggressive_fuzzer.py
```

### Fuzzing a specific interpreter

```bash
python scripts/run.py --python /path/to/python3.13 --timeout 15
```

### Using Copilot Skills

This repo includes a [GitHub Copilot skill](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions/adding-copilot-skills) in `.github/skills/` for running an end-to-end fuzzing campaign:

- **`find-bugs`** — Detects the interpreter, runs all fuzzers, writes new targeted tests, triages findings, creates minimal reproducers, and commits results

## Approach

Unlike LLM-based fuzzers, Fuzz4Py uses **programmatic generation** to create test cases:

1. **Template-based generators** — targeted edge cases for known fragile areas (parser, compiler, monitoring API, type system, exception groups, etc.)
2. **Random AST generation** — random valid ASTs compiled and executed
3. **Differential testing** — compare behavior across compile modes and optimization levels
4. **Semantic correctness** — AST round-trip testing, error attribute verification

### Bug Detection

The harness detects:
- **Crashes** — segfaults, access violations, abnormal termination
- **Fatal errors** — `Fatal Python error` in stderr
- **SystemError** — internal interpreter consistency failures
- **Exception bypass** — exceptions that skip `try/except` handlers
- **Hangs** — infinite loops via timeout
- **Incorrect results** — semantic differences between equivalent code paths

> [!WARNING]
> Generated test code may exercise dangerous patterns (deep recursion, memory pressure, etc.). Run in an isolated environment.

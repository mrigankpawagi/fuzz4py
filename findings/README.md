# Findings

This directory contains bugs discovered by Fuzz4Py. Each subdirectory contains a `README.md` describing the bug and one or more `reproducer*.py` scripts.

## Bug Hall of Fame

| # | Bug | Interpreter | Severity | Status |
|---|-----|-------------|----------|--------|
| 1 | [`compile()` SyntaxError has incorrect attributes](https://github.com/python/cpython/issues/127927) | CPython 3.11–3.13 | MEDIUM | Reported |
| 2 | [Monitoring callback crash (LINE/CALL/INSTRUCTION)](#) | CPython 3.13 | HIGH | New |
| 3 | [Monitoring exception bypass (JUMP/BRANCH)](#) | CPython 3.13 | MEDIUM | New |
| 4 | [Monitoring infinite loop (EXCEPTION_HANDLED)](#) | CPython 3.13 | HIGH | New |

## Directory Index

- **`cpython-313-compile-syntax-error-attrs/`** — `compile()` produces incorrect `SyntaxError` attributes (lineno, offset, text) when the filename matches the source file.
- **`cpython-313-monitoring-callback-crash/`** — `sys.monitoring` LINE/CALL/INSTRUCTION callbacks that raise exceptions cause an internal error dump and process crash.
- **`cpython-313-monitoring-exception-bypass/`** — `sys.monitoring` JUMP/BRANCH callback exceptions bypass `try/except` handlers.
- **`cpython-313-monitoring-infinite-loop/`** — `sys.monitoring` EXCEPTION_HANDLED callback that raises causes an infinite loop.

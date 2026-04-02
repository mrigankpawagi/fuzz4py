You are working on **Fuzz4Py**, a fuzzing framework for finding bugs in Python interpreters (CPython, GraalPy, PyPy, etc.).

## Project Structure

- **`scripts/`** — Fuzzer scripts (generators, harness, targeted fuzzers)
- **`findings/`** — Discovered bugs, each in a subdirectory with a `README.md` and reproducer scripts
- **`.github/skills/`** — Copilot skills for fuzzing workflows

## Conventions

- **Python version under test** is whichever interpreter the user specifies; do not assume a specific version. The default is the `python` command available on `PATH`.
- Fuzzer scripts live in `scripts/` and are invoked directly (e.g., `python scripts/run.py`).
- Findings go in `findings/<interpreter>-<version>-<short-slug>/` with a `README.md` and one or more `reproducer*.py` files.
- Reproducer files must be **self-contained** — no imports from the rest of the repo.
- Reproducer files should include a docstring explaining the bug, expected vs. actual behavior, and the Python version tested.

## Bug Detection Criteria

A "bug" is any of the following when triggered by valid or near-valid Python code:

1. **Crash** — segfault, abort, access violation, or other abnormal process termination
2. **Fatal Python error** — `Fatal Python error:` in stderr
3. **SystemError** — indicates an internal CPython consistency-check failure
4. **Incorrect behavior** — wrong results, wrong error attributes, wrong error messages
5. **Hang** — infinite loop or deadlock caused by interpreter internals
6. **Exception bypass** — exceptions that skip `try/except` handlers

Normal Python exceptions (TypeError, ValueError, SyntaxError, etc.) raised by user code are **not** bugs.

## Coding Style

- Use standard Python 3.12+ features.
- Prefer `subprocess.run` with `capture_output=True` when executing untrusted code.
- Keep scripts self-contained with no external dependencies beyond the standard library.
- Use descriptive names for test cases and findings.

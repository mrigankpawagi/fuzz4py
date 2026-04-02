"""
Test execution harness for CPython fuzzing.
Runs generated code both in-process and via subprocess, detecting bugs.
"""

import subprocess
import sys
import os
import time
import traceback
import signal
import tempfile
import textwrap
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Optional


# Windows crash exit codes
WINDOWS_CRASH_CODES = {
    0xC0000005: "ACCESS_VIOLATION",
    0xC0000409: "STACK_BUFFER_OVERRUN",
    0xC000001D: "ILLEGAL_INSTRUCTION",
    0xC0000094: "INTEGER_DIVIDE_BY_ZERO",
    0xC00000FD: "STACK_OVERFLOW",
    0xC0000374: "HEAP_CORRUPTION",
    0x80000003: "BREAKPOINT",
    0xC0000096: "PRIVILEGED_INSTRUCTION",
    0xC000008C: "ARRAY_BOUNDS_EXCEEDED",
    0xC000008D: "FLOAT_DENORMAL_OPERAND",
    0xC000008E: "FLOAT_DIVIDE_BY_ZERO",
    0xC000008F: "FLOAT_INEXACT_RESULT",
    0xC0000090: "FLOAT_INVALID_OPERATION",
    0xC0000091: "FLOAT_OVERFLOW",
    0xC0000092: "FLOAT_STACK_CHECK",
    0xC0000093: "FLOAT_UNDERFLOW",
}

# Keywords indicating internal CPython bugs (not user-level errors)
BUG_KEYWORDS_STDERR = [
    "fatal python error",
    "systemexit",
    "systemerror",
    "assertion",
    "segmentation fault",
    "core dumped",
    "abort",
    "internal error",
    "fatal error",
    "panic",
    "unreachable",
    "_pydecref",
    "refcount",
    "gc_refs",
    "object at",  # as part of "Fatal Python error" messages
]

# These are expected errors, not bugs
EXPECTED_ERRORS = [
    "syntaxerror",
    "indentationerror",
    "taberror",
    "nameerror",
    "typeerror",
    "valueerror",
    "attributeerror",
    "importerror",
    "modulenotfounderror",
    "keyerror",
    "indexerror",
    "zerodivisionerror",
    "overflowerror",
    "recursionerror",
    "memoryerror",
    "runtimeerror",
    "stopiteration",
    "generatorexit",
    "filenotfounderror",
    "oserror",
    "permissionerror",
    "unicodeerror",
    "unicodeencodeerror",
    "unicodedecodeerror",
    "lookuperror",
    "arithmeticerror",
    "buffererror",
    "aborterror",
    "eoferror",
    "connectionerror",
    "blockingioerror",
    "brokenpipeerror",
    "childprocesserror",
    "connectionabortederror",
    "connectionrefusederror",
    "connectionreseterror",
    "fileexistserror",
    "interruptederror",
    "isadirectoryerror",
    "notadirectoryerror",
    "timeouterror",
    "processlookuperor",
]


@dataclass
class TestResult:
    name: str
    source: str
    status: str  # "pass", "expected_error", "crash", "internal_error", "timeout", "bug"
    exit_code: Optional[int] = None
    stdout: str = ""
    stderr: str = ""
    error_type: str = ""
    details: str = ""
    duration: float = 0.0


@dataclass
class FuzzStats:
    total: int = 0
    passed: int = 0
    expected_errors: int = 0
    crashes: int = 0
    internal_errors: int = 0
    timeouts: int = 0
    bugs: int = 0
    findings: list = field(default_factory=list)


def is_crash_exit_code(exit_code: int) -> Optional[str]:
    """Check if exit code indicates a crash (Windows)."""
    if exit_code is None:
        return None
    # Windows uses unsigned 32-bit codes; Python may report them as negative
    unsigned = exit_code & 0xFFFFFFFF if exit_code < 0 else exit_code
    if unsigned in WINDOWS_CRASH_CODES:
        return WINDOWS_CRASH_CODES[unsigned]
    # Also check for signal-based codes (Unix-style)
    if exit_code < 0 and exit_code != -1:
        return f"SIGNAL_{-exit_code}"
    return None


def check_for_internal_error(stderr: str) -> Optional[str]:
    """Check stderr for internal CPython errors (not user errors)."""
    stderr_lower = stderr.lower()

    # First check for Fatal Python error (always a bug)
    if "fatal python error" in stderr_lower:
        return "fatal_python_error"

    # Check for SystemError (indicates internal bug)
    if "systemerror" in stderr_lower:
        # Make sure it's not just mentioned in a string
        for line in stderr.split('\n'):
            line_lower = line.lower().strip()
            if line_lower.startswith('systemerror') or 'systemerror:' in line_lower:
                return "system_error"

    # Check for assertion failures from C code
    if "assertion" in stderr_lower and ("failed" in stderr_lower or "error" in stderr_lower):
        if "assertionerror" not in stderr_lower:  # Python's AssertionError is fine
            return "c_assertion_failure"

    # Check for other internal errors
    for keyword in ["segmentation fault", "core dumped", "abort()", "unreachable"]:
        if keyword in stderr_lower:
            return keyword.replace(" ", "_")

    return None


def run_test_subprocess(name: str, source: str, python_exe: str, timeout: int = 30) -> TestResult:
    """Run a test case in a subprocess."""
    start = time.time()

    # Write source to a temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, prefix=f'fuzz_{name}_') as f:
        f.write(source)
        temp_path = f.name

    try:
        proc = subprocess.run(
            [python_exe, temp_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=os.path.dirname(temp_path),
        )
        duration = time.time() - start
        exit_code = proc.returncode
        stdout = proc.stdout
        stderr = proc.stderr

        # Check for crash
        crash_reason = is_crash_exit_code(exit_code)
        if crash_reason:
            return TestResult(
                name=name, source=source, status="crash",
                exit_code=exit_code, stdout=stdout, stderr=stderr,
                error_type=crash_reason, duration=duration,
                details=f"Process crashed with {crash_reason} (exit code {exit_code})"
            )

        # Check for internal errors
        internal_error = check_for_internal_error(stderr)
        if internal_error:
            return TestResult(
                name=name, source=source, status="internal_error",
                exit_code=exit_code, stdout=stdout, stderr=stderr,
                error_type=internal_error, duration=duration,
                details=f"Internal error: {internal_error}\n{stderr[:500]}"
            )

        # Normal exit
        if exit_code == 0:
            return TestResult(
                name=name, source=source, status="pass",
                exit_code=exit_code, stdout=stdout, stderr=stderr,
                duration=duration
            )
        else:
            # Non-zero exit but not a crash - likely a Python exception
            return TestResult(
                name=name, source=source, status="expected_error",
                exit_code=exit_code, stdout=stdout, stderr=stderr,
                duration=duration, error_type="python_exception",
                details=stderr[:200] if stderr else ""
            )

    except subprocess.TimeoutExpired:
        duration = time.time() - start
        return TestResult(
            name=name, source=source, status="timeout",
            duration=duration, error_type="timeout",
            details=f"Timed out after {timeout}s"
        )
    except Exception as e:
        duration = time.time() - start
        return TestResult(
            name=name, source=source, status="expected_error",
            duration=duration, error_type="runner_error",
            details=str(e)
        )
    finally:
        try:
            os.unlink(temp_path)
        except OSError:
            pass


def run_test_inprocess(name: str, source: str) -> TestResult:
    """Run a test case in-process (for compile/ast testing only)."""
    start = time.time()
    try:
        # Try to compile the code
        code = compile(source, f"<fuzz_{name}>", "exec")
        duration = time.time() - start
        return TestResult(
            name=name, source=source, status="pass",
            duration=duration
        )
    except SyntaxError:
        duration = time.time() - start
        return TestResult(
            name=name, source=source, status="expected_error",
            duration=duration, error_type="syntax_error"
        )
    except SystemError as e:
        duration = time.time() - start
        return TestResult(
            name=name, source=source, status="internal_error",
            duration=duration, error_type="system_error",
            details=f"SystemError during compile: {e}"
        )
    except Exception as e:
        duration = time.time() - start
        return TestResult(
            name=name, source=source, status="expected_error",
            duration=duration, error_type=type(e).__name__,
            details=str(e)
        )


def run_tests_subprocess(cases, python_exe=sys.executable, timeout=30, max_workers=None):
    """Run test cases in subprocesses with parallelism."""
    stats = FuzzStats()
    max_workers = max_workers or min(os.cpu_count() or 4, 8)

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for name, source in cases:
            future = executor.submit(run_test_subprocess, name, source, python_exe, timeout)
            futures[future] = (name, source)

        for future in as_completed(futures):
            stats.total += 1
            try:
                result = future.result(timeout=timeout + 10)
            except Exception as e:
                name, source = futures[future]
                result = TestResult(
                    name=name, source=source, status="expected_error",
                    error_type="future_error", details=str(e)
                )

            if result.status == "pass":
                stats.passed += 1
            elif result.status == "expected_error":
                stats.expected_errors += 1
            elif result.status == "crash":
                stats.crashes += 1
                stats.findings.append(result)
            elif result.status == "internal_error":
                stats.internal_errors += 1
                stats.findings.append(result)
            elif result.status == "timeout":
                stats.timeouts += 1
            elif result.status == "bug":
                stats.bugs += 1
                stats.findings.append(result)

            # Print progress for findings
            if result.status in ("crash", "internal_error", "bug"):
                print(f"\n{'='*60}")
                print(f"FINDING: {result.status.upper()} in {result.name}")
                print(f"Error type: {result.error_type}")
                print(f"Details: {result.details}")
                print(f"Exit code: {result.exit_code}")
                if result.stderr:
                    print(f"Stderr: {result.stderr[:500]}")
                print(f"Source:\n{textwrap.indent(result.source[:500], '  ')}")
                print(f"{'='*60}\n")

    return stats


def run_tests_inprocess(cases):
    """Run test cases in-process (compile-only)."""
    stats = FuzzStats()

    for name, source in cases:
        stats.total += 1
        result = run_test_inprocess(name, source)

        if result.status == "pass":
            stats.passed += 1
        elif result.status == "expected_error":
            stats.expected_errors += 1
        elif result.status == "internal_error":
            stats.internal_errors += 1
            stats.findings.append(result)

        if result.status in ("internal_error", "bug"):
            print(f"\n{'='*60}")
            print(f"FINDING: {result.status.upper()} in {result.name}")
            print(f"Error type: {result.error_type}")
            print(f"Details: {result.details}")
            print(f"Source:\n{textwrap.indent(result.source[:500], '  ')}")
            print(f"{'='*60}\n")

    return stats


def print_stats(stats: FuzzStats, label: str = ""):
    """Print test statistics."""
    print(f"\n{'='*40}")
    print(f"Results{f' ({label})' if label else ''}")
    print(f"{'='*40}")
    print(f"Total:           {stats.total}")
    print(f"Passed:          {stats.passed}")
    print(f"Expected errors: {stats.expected_errors}")
    print(f"Crashes:         {stats.crashes}")
    print(f"Internal errors: {stats.internal_errors}")
    print(f"Timeouts:        {stats.timeouts}")
    print(f"Bugs found:      {stats.bugs}")
    print(f"Total findings:  {len(stats.findings)}")
    print(f"{'='*40}\n")

    if stats.findings:
        print("FINDINGS SUMMARY:")
        for i, f in enumerate(stats.findings, 1):
            print(f"\n--- Finding {i}: {f.name} ---")
            print(f"Status: {f.status}")
            print(f"Type: {f.error_type}")
            print(f"Details: {f.details[:200]}")

"""
Fuzz4Py - Main fuzzer entry point.
Generates diverse Python programs and tests them against a Python interpreter
to find crashes, internal errors, and other bugs.
"""

import sys
import os
import time
import argparse
import random

# Add this directory to path so sibling modules can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generators import generate_all, gen_random_programs, gen_compile_edge_cases
from harness import (
    run_tests_subprocess, run_tests_inprocess, print_stats, FuzzStats
)


def merge_stats(stats_list):
    """Merge multiple FuzzStats objects."""
    merged = FuzzStats()
    for s in stats_list:
        merged.total += s.total
        merged.passed += s.passed
        merged.expected_errors += s.expected_errors
        merged.crashes += s.crashes
        merged.internal_errors += s.internal_errors
        merged.timeouts += s.timeouts
        merged.bugs += s.bugs
        merged.findings.extend(s.findings)
    return merged


def save_findings(stats, output_dir):
    """Save findings to files."""
    os.makedirs(output_dir, exist_ok=True)

    if not stats.findings:
        with open(os.path.join(output_dir, "no_findings.txt"), "w") as f:
            f.write(f"No findings in {stats.total} tests.\n")
        return

    for i, finding in enumerate(stats.findings, 1):
        # Save the source code
        src_path = os.path.join(output_dir, f"finding_{i}_{finding.name}.py")
        with open(src_path, "w") as f:
            f.write(f"# Finding: {finding.name}\n")
            f.write(f"# Status: {finding.status}\n")
            f.write(f"# Error type: {finding.error_type}\n")
            f.write(f"# Details: {finding.details}\n")
            f.write(f"# Exit code: {finding.exit_code}\n")
            f.write(f"#\n")
            f.write(finding.source)

        # Save the details
        detail_path = os.path.join(output_dir, f"finding_{i}_{finding.name}.txt")
        with open(detail_path, "w") as f:
            f.write(f"Name: {finding.name}\n")
            f.write(f"Status: {finding.status}\n")
            f.write(f"Error type: {finding.error_type}\n")
            f.write(f"Exit code: {finding.exit_code}\n")
            f.write(f"Duration: {finding.duration:.2f}s\n")
            f.write(f"\n--- Details ---\n{finding.details}\n")
            f.write(f"\n--- Stdout ---\n{finding.stdout}\n")
            f.write(f"\n--- Stderr ---\n{finding.stderr}\n")
            f.write(f"\n--- Source ---\n{finding.source}\n")

    # Summary file
    with open(os.path.join(output_dir, "summary.txt"), "w") as f:
        f.write(f"CPython 3.13 Fuzzer Results\n")
        f.write(f"Python: {sys.version}\n")
        f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"\n")
        f.write(f"Total tests: {stats.total}\n")
        f.write(f"Passed: {stats.passed}\n")
        f.write(f"Expected errors: {stats.expected_errors}\n")
        f.write(f"Crashes: {stats.crashes}\n")
        f.write(f"Internal errors: {stats.internal_errors}\n")
        f.write(f"Timeouts: {stats.timeouts}\n")
        f.write(f"Bugs: {stats.bugs}\n")
        f.write(f"Total findings: {len(stats.findings)}\n")
        f.write(f"\nFindings:\n")
        for i, finding in enumerate(stats.findings, 1):
            f.write(f"\n{i}. {finding.name} ({finding.status})\n")
            f.write(f"   Type: {finding.error_type}\n")
            f.write(f"   Details: {finding.details[:200]}\n")


def main():
    parser = argparse.ArgumentParser(description="CPython 3.13 Fuzzer")
    parser.add_argument("--python", default=sys.executable,
                       help="Path to Python executable to fuzz")
    parser.add_argument("--timeout", type=int, default=30,
                       help="Timeout per test in seconds")
    parser.add_argument("--output", default="cpython_fuzzer/results",
                       help="Output directory for findings")
    parser.add_argument("--workers", type=int, default=None,
                       help="Number of parallel workers")
    parser.add_argument("--random-count", type=int, default=500,
                       help="Number of random programs to generate")
    parser.add_argument("--seed", type=int, default=None,
                       help="Random seed for reproducibility")
    parser.add_argument("--compile-only", action="store_true",
                       help="Only test compilation (in-process, faster)")
    parser.add_argument("--category", type=str, default=None,
                       help="Only run a specific generator category")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    print(f"CPython 3.13 Fuzzer")
    print(f"Python: {sys.version}")
    print(f"Executable: {args.python}")
    print(f"Timeout: {args.timeout}s")
    print(f"Output: {args.output}")
    print()

    # Generate all test cases
    print("Generating test cases...")
    all_cases = generate_all()
    print(f"Generated {len(all_cases)} test cases")

    all_stats = []

    if args.compile_only:
        # Phase 1: In-process compile testing (fast)
        print("\n--- Phase 1: In-process compile testing ---")
        # Filter to compile-related cases only
        compile_cases = [(n, s) for n, s in all_cases if 'compile' in n or 'fstring' in n]
        stats = run_tests_inprocess(compile_cases)
        print_stats(stats, "In-process compile")
        all_stats.append(stats)
    else:
        # Full subprocess testing
        print(f"\n--- Running all {len(all_cases)} tests via subprocess ---")
        stats = run_tests_subprocess(
            all_cases,
            python_exe=args.python,
            timeout=args.timeout,
            max_workers=args.workers
        )
        print_stats(stats, "Subprocess execution")
        all_stats.append(stats)

    # Merge and save
    merged = merge_stats(all_stats)
    save_findings(merged, args.output)

    print(f"\nResults saved to {args.output}/")

    if merged.findings:
        print(f"\n{'!'*60}")
        print(f"FOUND {len(merged.findings)} POTENTIAL BUG(S)!")
        print(f"{'!'*60}")
        return 1
    else:
        print("\nNo bugs found in this run.")
        return 0


if __name__ == "__main__":
    sys.exit(main())

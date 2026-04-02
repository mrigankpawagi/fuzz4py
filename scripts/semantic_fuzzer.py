"""
Semantic correctness fuzzer for CPython 3.13.
Tests for subtle bugs: incorrect results, wrong error attributes,
AST round-trip inconsistencies, optimizer bugs, and new 3.13 feature edge cases.
"""

import sys
import os
import ast
import dis
import types
import gc
import weakref
import marshal
import symtable
import traceback
import textwrap
import io
import copy
import re
import threading
import time
import subprocess
import tempfile
import struct
import collections
import functools
import itertools
import random


class Finding:
    def __init__(self, category, name, details, code=""):
        self.category = category
        self.name = name
        self.details = details
        self.code = code

    def __repr__(self):
        return f"Finding({self.category}, {self.name}): {self.details[:100]}"


class SemanticFuzzer:
    def __init__(self):
        self.findings = []
        self.tests_run = 0

    def report(self, category, name, details, code=""):
        f = Finding(category, name, details, code)
        self.findings.append(f)
        print(f"\n  !!! FINDING: [{category}] {name}")
        print(f"      {details[:200]}")

    def ok(self):
        self.tests_run += 1

    # ==========================================
    # 1. AST Round-Trip Testing
    # ==========================================
    def test_ast_roundtrip(self):
        """Test that ast.parse -> ast.unparse -> ast.parse preserves semantics."""
        print("  Testing AST round-trip...")

        # Programs that should round-trip correctly
        programs = [
            "x = 1",
            "x = 1 + 2 * 3",
            "x = (1 + 2) * 3",
            "x = -1",
            "x = ~1",
            "x = not True",
            "x = 1 if True else 2",
            "x = [1, 2, 3]",
            "x = (1, 2, 3)",
            "x = {1, 2, 3}",
            "x = {1: 2, 3: 4}",
            "x = {**{1: 2}, **{3: 4}}",
            "x = [*[1, 2], *[3, 4]]",
            "x = f'{1 + 2}'",
            "x = f'{1 + 2!r}'",
            "x = f'{1 + 2:.2f}'",
            "x = f'{1 + 2!r:.10}'",
            "x = b'hello'",
            "x = rb'hello'",
            "x = 'a' 'b' 'c'",
            "x = 1, 2, 3",
            "x = (1,)",
            "x = ...",
            "x = None",
            "x = True",
            "x = False",
            "x: int = 1",
            "x: list[int] = []",
            "del x",
            "a, b = 1, 2",
            "a, *b = [1, 2, 3]",
            "*a, b = [1, 2, 3]",
            "a, *b, c = [1, 2, 3, 4]",
            "(a, b), c = (1, 2), 3",
            "def f(): pass",
            "def f(x): return x",
            "def f(x, y=1): return x + y",
            "def f(*args): return args",
            "def f(**kwargs): return kwargs",
            "def f(x, /, y, *, z): pass",
            "def f(x: int, y: str = '') -> bool: pass",
            "async def f(): pass",
            "async def f(): await g()",
            "lambda: None",
            "lambda x: x",
            "lambda x, y=1: x + y",
            "lambda *a, **k: (a, k)",
            "lambda x, /, y, *, z: x",
            "class C: pass",
            "class C(A, B): pass",
            "class C(metaclass=M): pass",
            "class C:\n x = 1",
            "class C:\n def f(self): pass",
            "@dec\ndef f(): pass",
            "@dec1\n@dec2\ndef f(): pass",
            "@a.b.c\ndef f(): pass",
            "if True:\n pass",
            "if True:\n pass\nelse:\n pass",
            "if True:\n pass\nelif False:\n pass\nelse:\n pass",
            "for x in range(10):\n pass",
            "for x in range(10):\n pass\nelse:\n pass",
            "while True:\n break",
            "while True:\n break\nelse:\n pass",
            "try:\n pass\nexcept:\n pass",
            "try:\n pass\nexcept Exception:\n pass",
            "try:\n pass\nexcept Exception as e:\n pass",
            "try:\n pass\nexcept (ValueError, TypeError):\n pass",
            "try:\n pass\nexcept:\n pass\nelse:\n pass",
            "try:\n pass\nfinally:\n pass",
            "try:\n pass\nexcept:\n pass\nfinally:\n pass",
            "with x:\n pass",
            "with x as y:\n pass",
            "with x as y, z as w:\n pass",
            "import os",
            "import os.path",
            "from os import path",
            "from os import path as p",
            "from os import *",
            "from . import x",
            "from .. import x",
            "from .mod import x",
            "assert True",
            "assert True, 'msg'",
            "raise ValueError",
            "raise ValueError('msg')",
            "raise ValueError from exc",
            "global x",
            "x = 1\ndef f():\n nonlocal x",  # This would fail, skip
            "pass",
            "x = 1; y = 2",
            "x = [i for i in range(10)]",
            "x = [i for i in range(10) if i % 2 == 0]",
            "x = {i: i**2 for i in range(10)}",
            "x = {i for i in range(10)}",
            "x = (i for i in range(10))",
            "x = [i for i in range(10) for j in range(i)]",
            "(x := 1)",
            "match x:\n case 1:\n  pass",
            "match x:\n case _:\n  pass",
            "match x:\n case [a, *b]:\n  pass",
            "match x:\n case {1: x}:\n  pass",
            "match x:\n case int(v):\n  pass",
            "match x:\n case 1 | 2 | 3:\n  pass",
            "match x:\n case x if x > 0:\n  pass",
            "type Alias = int",
            "type Alias[T] = list[T]",
            "class C[T]: pass",
            "def f[T](x: T) -> T: return x",
            "try:\n raise ExceptionGroup('e', [ValueError()])\nexcept* ValueError:\n pass",
        ]

        for prog in programs:
            try:
                tree1 = ast.parse(prog)
                unparsed = ast.unparse(tree1)
                tree2 = ast.parse(unparsed)

                # Compare ASTs by dumping
                dump1 = ast.dump(tree1, indent=2)
                dump2 = ast.dump(tree2, indent=2)

                if dump1 != dump2:
                    # Check if the difference is semantically meaningful
                    # Some differences are expected (e.g., parenthesization)
                    # So we compare by compiling and checking bytecode
                    try:
                        code1 = compile(tree1, "<test>", "exec")
                        code2 = compile(tree2, "<test>", "exec")

                        # Compare by executing
                        ns1, ns2 = {}, {}
                        try:
                            exec(code1, ns1)
                        except Exception:
                            pass
                        try:
                            exec(code2, ns2)
                        except Exception:
                            pass

                        # Filter out builtins for comparison
                        ns1.pop('__builtins__', None)
                        ns2.pop('__builtins__', None)

                        if ns1 != ns2:
                            self.report("ast_roundtrip", f"semantic_diff",
                                f"AST round-trip changed semantics:\n"
                                f"  Original: {prog!r}\n"
                                f"  Unparsed: {unparsed!r}\n"
                                f"  ns1: {ns1}\n  ns2: {ns2}",
                                prog)
                        else:
                            self.ok()
                    except SyntaxError:
                        # If one compiles and the other doesn't, that's a bug
                        self.report("ast_roundtrip", f"compile_diff",
                            f"AST round-trip broke compilation:\n"
                            f"  Original: {prog!r}\n  Unparsed: {unparsed!r}",
                            prog)
                else:
                    self.ok()
            except SyntaxError:
                self.ok()  # Some programs are intentionally invalid
            except Exception as e:
                if isinstance(e, SystemError):
                    self.report("ast_roundtrip", "system_error",
                        f"SystemError during AST round-trip: {e}", prog)
                self.ok()

    # ==========================================
    # 2. Error Attribute Correctness
    # ==========================================
    def test_error_attributes(self):
        """Test that SyntaxError attributes are correct in all cases."""
        print("  Testing error attributes...")

        # Each tuple: (code, expected_lineno, expected_offset_range)
        error_cases = [
            # (code, expected_lineno, min_offset, max_offset, optional_msg_fragment)
            ("x y", 1, 1, 4, "invalid syntax"),
            ("1 +", 1, 1, 4, None),
            ("def def", 1, 1, 8, None),
            ("x = (1 +\n)", 2, None, None, None),
            ("\n\nx y", 3, 1, 4, None),
            ("  x y", 1, 1, 6, None),
            ("x = 1\ny z", 2, 1, 4, None),
        ]

        for case in error_cases:
            code = case[0]
            expected_lineno = case[1]

            for filename in ["<string>", "<test>", "", "nonexistent.py"]:
                for mode in ["exec", "single"]:
                    try:
                        compile(code, filename, mode)
                        self.ok()
                    except SyntaxError as e:
                        # Check lineno
                        if e.lineno is not None:
                            if expected_lineno is not None and e.lineno != expected_lineno:
                                self.report("error_attrs", f"wrong_lineno",
                                    f"Wrong lineno: got {e.lineno}, expected {expected_lineno}\n"
                                    f"  code={code!r}, filename={filename!r}, mode={mode!r}",
                                    code)
                            elif e.lineno <= 0:
                                self.report("error_attrs", f"invalid_lineno",
                                    f"Invalid lineno: {e.lineno}\n"
                                    f"  code={code!r}, filename={filename!r}, mode={mode!r}",
                                    code)
                            else:
                                self.ok()
                        else:
                            self.ok()

                        # Check offset
                        if e.offset is not None and e.offset < 0:
                            self.report("error_attrs", f"negative_offset",
                                f"Negative offset: {e.offset}\n"
                                f"  code={code!r}, filename={filename!r}, mode={mode!r}",
                                code)

                        # Check text is set
                        if e.text is None and e.lineno is not None:
                            self.report("error_attrs", f"missing_text",
                                f"Missing text for error at line {e.lineno}\n"
                                f"  code={code!r}, filename={filename!r}, mode={mode!r}",
                                code)

                        # Check that text contains the actual source line
                        if e.text is not None and e.lineno is not None:
                            source_lines = code.split('\n')
                            if 0 < e.lineno <= len(source_lines):
                                actual_line = source_lines[e.lineno - 1]
                                if actual_line.strip() and actual_line not in e.text:
                                    # The text doesn't match the actual source line
                                    self.report("error_attrs", f"wrong_text",
                                        f"Error text doesn't match source line\n"
                                        f"  Expected line: {actual_line!r}\n"
                                        f"  Got text: {e.text!r}\n"
                                        f"  code={code!r}, filename={filename!r}",
                                        code)
                    except Exception as e:
                        if isinstance(e, SystemError):
                            self.report("error_attrs", f"system_error",
                                f"SystemError: {e}\n  code={code!r}", code)
                        self.ok()

    # ==========================================
    # 3. Compile Consistency Testing
    # ==========================================
    def test_compile_consistency(self):
        """Test that compile() produces consistent results across modes."""
        print("  Testing compile consistency...")

        programs = [
            "x = 1 + 2 * 3",
            "x = [i**2 for i in range(10)]",
            "x = {k: v for k, v in enumerate('abc')}",
            "def f(n): return n * 2\nx = f(21)",
            "x = (lambda n: n ** 2)(6)",
            "x = sum(range(100))",
            "x = sorted([3,1,4,1,5,9])",
            "x = list(filter(lambda n: n%2==0, range(20)))",
            "x = list(map(str, range(10)))",
            "x = dict(zip('abc', range(3)))",
        ]

        for prog in programs:
            try:
                # Method 1: compile string directly
                code1 = compile(prog, "<test1>", "exec")
                ns1 = {}
                exec(code1, ns1)
                ns1.pop('__builtins__', None)

                # Method 2: compile via AST
                tree = ast.parse(prog)
                code2 = compile(tree, "<test2>", "exec")
                ns2 = {}
                exec(code2, ns2)
                ns2.pop('__builtins__', None)

                # Method 3: compile with optimize=1
                code3 = compile(prog, "<test3>", "exec", optimize=1)
                ns3 = {}
                exec(code3, ns3)
                ns3.pop('__builtins__', None)

                # Method 4: compile with optimize=2
                code4 = compile(prog, "<test4>", "exec", optimize=2)
                ns4 = {}
                exec(code4, ns4)
                ns4.pop('__builtins__', None)

                # Compare results (filter functions since they can't be compared)
                for key in ns1:
                    if callable(ns1.get(key)):
                        continue
                    vals = [ns1.get(key), ns2.get(key), ns3.get(key), ns4.get(key)]
                    if not all(v == vals[0] for v in vals):
                        self.report("compile_consistency", "result_mismatch",
                            f"Different results for {prog!r}:\n"
                            f"  Direct: {ns1.get(key)}\n"
                            f"  AST: {ns2.get(key)}\n"
                            f"  Opt1: {ns3.get(key)}\n"
                            f"  Opt2: {ns4.get(key)}",
                            prog)
                self.ok()
            except Exception as e:
                if isinstance(e, SystemError):
                    self.report("compile_consistency", "system_error",
                        f"SystemError: {e}", prog)
                self.ok()

    # ==========================================
    # 4. PEP 667 - locals() Semantics (3.13)
    # ==========================================
    def test_pep667_locals(self):
        """Test PEP 667 changes to locals() in 3.13."""
        print("  Testing PEP 667 locals() semantics...")

        # In 3.13, locals() returns a snapshot, not a live view
        # Changes to the returned dict should not affect local variables

        test_code = textwrap.dedent("""
        def test_locals_snapshot():
            x = 1
            d = locals()
            d['x'] = 999
            # In 3.13, x should still be 1 (PEP 667)
            return x, d['x']

        result = test_locals_snapshot()
        """)

        try:
            ns = {}
            exec(test_code, ns)
            x_val, d_val = ns['result']
            # In 3.13 with PEP 667, x should be 1
            if x_val != 1:
                self.report("pep667", "locals_mutation",
                    f"locals() mutation affected local variable: x={x_val} (expected 1)",
                    test_code)
            self.ok()
        except Exception as e:
            if isinstance(e, SystemError):
                self.report("pep667", "system_error", f"SystemError: {e}", test_code)
            self.ok()

        # Test locals() in different scopes
        test_cases = [
            # Test locals() in comprehension
            textwrap.dedent("""
            def test():
                x = 42
                result = [locals() for _ in range(1)]
                return x, result
            result = test()
            """),

            # Test locals() with closure
            textwrap.dedent("""
            def test():
                x = 42
                def inner():
                    return locals()
                return inner()
            result = test()
            """),

            # Test locals() after del
            textwrap.dedent("""
            def test():
                x = 42
                d = locals()
                del x
                d2 = locals()
                return 'x' in d, 'x' in d2
            result = test()
            """),

            # Test locals() with *args and **kwargs
            textwrap.dedent("""
            def test(*args, **kwargs):
                return locals()
            result = test(1, 2, a=3)
            """),

            # Test locals() in exec
            textwrap.dedent("""
            def test():
                exec("y = 99")
                return locals()
            result = test()
            """),
        ]

        for code in test_cases:
            try:
                ns = {}
                exec(code, ns)
                self.ok()
            except Exception as e:
                if isinstance(e, SystemError):
                    self.report("pep667", "system_error", f"SystemError: {e}", code)
                self.ok()

    # ==========================================
    # 5. Monitoring API (PEP 669) Edge Cases
    # ==========================================
    def test_monitoring_api(self):
        """Test the sys.monitoring API (PEP 669)."""
        print("  Testing monitoring API...")

        try:
            E = sys.monitoring.events

            # Test tool registration
            TOOL_ID = 3  # Use a tool ID that's unlikely to conflict
            try:
                sys.monitoring.use_tool_id(TOOL_ID, "fuzzer_test")

                # Register callbacks for various events
                events_seen = []

                def line_callback(code, line_number):
                    events_seen.append(('line', line_number))
                    return sys.monitoring.DISABLE

                def call_callback(code, instruction_offset, callable, arg0):
                    events_seen.append(('call', str(callable)[:50]))

                def return_callback(code, instruction_offset, retval):
                    events_seen.append(('return', retval))

                sys.monitoring.register_callback(TOOL_ID, E.LINE, line_callback)
                sys.monitoring.register_callback(TOOL_ID, E.CALL, call_callback)
                sys.monitoring.register_callback(TOOL_ID, E.PY_RETURN, return_callback)

                # Enable events
                sys.monitoring.set_events(TOOL_ID, E.LINE | E.CALL | E.PY_RETURN)

                # Run some code
                def test_func():
                    x = 1
                    y = 2
                    return x + y

                result = test_func()
                assert result == 3

                # Disable events
                sys.monitoring.set_events(TOOL_ID, 0)

                # Unregister callbacks
                sys.monitoring.register_callback(TOOL_ID, E.LINE, None)
                sys.monitoring.register_callback(TOOL_ID, E.CALL, None)
                sys.monitoring.register_callback(TOOL_ID, E.PY_RETURN, None)

                sys.monitoring.free_tool_id(TOOL_ID)
                self.ok()

            except Exception as e:
                try:
                    sys.monitoring.set_events(TOOL_ID, 0)
                    sys.monitoring.free_tool_id(TOOL_ID)
                except Exception:
                    pass
                if isinstance(e, SystemError):
                    self.report("monitoring", "system_error",
                        f"SystemError in monitoring API: {e}")
                self.ok()

        except AttributeError:
            self.ok()  # monitoring API not available

        # Test monitoring with generators
        try:
            TOOL_ID = 3
            sys.monitoring.use_tool_id(TOOL_ID, "fuzzer_gen_test")

            events = []
            def line_cb(code, line):
                events.append(('line', line))

            sys.monitoring.register_callback(TOOL_ID, E.LINE, line_cb)
            sys.monitoring.set_events(TOOL_ID, E.LINE)

            def gen():
                yield 1
                yield 2

            list(gen())

            sys.monitoring.set_events(TOOL_ID, 0)
            sys.monitoring.register_callback(TOOL_ID, E.LINE, None)
            sys.monitoring.free_tool_id(TOOL_ID)
            self.ok()
        except Exception as e:
            try:
                sys.monitoring.set_events(TOOL_ID, 0)
                sys.monitoring.free_tool_id(TOOL_ID)
            except Exception:
                pass
            if isinstance(e, SystemError):
                self.report("monitoring", "generator_error",
                    f"SystemError monitoring generators: {e}")
            self.ok()

        # Test monitoring with async
        try:
            import asyncio
            TOOL_ID = 3
            sys.monitoring.use_tool_id(TOOL_ID, "fuzzer_async_test")

            events = []
            def line_cb(code, line):
                events.append(line)

            sys.monitoring.register_callback(TOOL_ID, E.LINE, line_cb)
            sys.monitoring.set_events(TOOL_ID, E.LINE)

            async def async_test():
                await asyncio.sleep(0)
                return 42

            asyncio.run(async_test())

            sys.monitoring.set_events(TOOL_ID, 0)
            sys.monitoring.register_callback(TOOL_ID, E.LINE, None)
            sys.monitoring.free_tool_id(TOOL_ID)
            self.ok()
        except Exception as e:
            try:
                sys.monitoring.set_events(TOOL_ID, 0)
                sys.monitoring.free_tool_id(TOOL_ID)
            except Exception:
                pass
            if isinstance(e, SystemError):
                self.report("monitoring", "async_error",
                    f"SystemError monitoring async: {e}")
            self.ok()

        # Test monitoring callback that raises
        try:
            TOOL_ID = 3
            sys.monitoring.use_tool_id(TOOL_ID, "fuzzer_raise_test")

            def raising_cb(code, line):
                raise ValueError("callback error")

            sys.monitoring.register_callback(TOOL_ID, E.LINE, raising_cb)
            sys.monitoring.set_events(TOOL_ID, E.LINE)

            try:
                x = 1 + 2  # Should trigger callback
            except ValueError:
                pass

            sys.monitoring.set_events(TOOL_ID, 0)
            sys.monitoring.register_callback(TOOL_ID, E.LINE, None)
            sys.monitoring.free_tool_id(TOOL_ID)
            self.ok()
        except Exception as e:
            try:
                sys.monitoring.set_events(TOOL_ID, 0)
                sys.monitoring.free_tool_id(TOOL_ID)
            except Exception:
                pass
            if isinstance(e, SystemError):
                self.report("monitoring", "raising_callback_error",
                    f"SystemError with raising callback: {e}")
            self.ok()

    # ==========================================
    # 6. Symtable Edge Cases
    # ==========================================
    def test_symtable(self):
        """Test symtable module edge cases."""
        print("  Testing symtable...")

        programs = [
            "x = 1",
            "def f(x): return x",
            "class C:\n x = 1",
            "def f():\n x = 1\n def g():\n  return x\n return g",
            "import os",
            "from os import path",
            "global x",
            "def f():\n x = 1\n def g():\n  nonlocal x\n  x = 2",
            "x = [i for i in range(10)]",
            "def f(*a, **k): pass",
            "async def f(): await g()",
            "class C[T]: pass",
            "def f[T](x: T) -> T: return x",
            "type Alias = int",
            "match x:\n case 1: pass",
            "try:\n pass\nexcept* ValueError:\n pass",
        ]

        for prog in programs:
            try:
                st = symtable.symtable(prog, "<test>", "exec")
                # Walk all symbols
                for sym in st.get_symbols():
                    sym.get_name()
                    sym.is_referenced()
                    sym.is_imported()
                    sym.is_parameter()
                    sym.is_global()
                    sym.is_declared_global()
                    sym.is_local()
                    sym.is_free()
                    sym.is_assigned()
                    sym.is_namespace()
                    sym.get_namespaces()

                # Walk children
                for child in st.get_children():
                    for sym in child.get_symbols():
                        sym.get_name()
                self.ok()
            except SyntaxError:
                self.ok()  # Some programs need context
            except SystemError as e:
                self.report("symtable", "system_error",
                    f"SystemError: {e}", prog)
            except Exception:
                self.ok()

    # ==========================================
    # 7. Optimizer Correctness
    # ==========================================
    def test_optimizer_correctness(self):
        """Test that the optimizer doesn't change program semantics."""
        print("  Testing optimizer correctness...")

        # Programs where optimization should not change behavior
        programs = [
            ("x = 1 + 2", {"x": 3}),
            ("x = 2 ** 10", {"x": 1024}),
            ("x = 'a' * 3", {"x": "aaa"}),
            ("x = True and False", {"x": False}),
            ("x = True or False", {"x": True}),
            ("x = not True", {"x": False}),
            ("x = 1 if True else 2", {"x": 1}),
            ("x = 1 if False else 2", {"x": 2}),
            ("x = (1, 2, 3)", {"x": (1, 2, 3)}),
            ("x = [1, 2, 3]; x = tuple(x)", {"x": (1, 2, 3)}),
            ("x = 10 // 3", {"x": 3}),
            ("x = 10 % 3", {"x": 1}),
            ("x = -(-5)", {"x": 5}),
            ("x = ~~5", {"x": 5}),
            ("x = 0 or 42", {"x": 42}),
            ("x = 42 or 0", {"x": 42}),
            ("x = 0 and 42", {"x": 0}),
            ("x = 42 and 0", {"x": 0}),
        ]

        for prog, expected in programs:
            for opt in [0, 1, 2]:
                try:
                    code = compile(prog, "<test>", "exec", optimize=opt)
                    ns = {}
                    exec(code, ns)
                    ns.pop('__builtins__', None)

                    for key, val in expected.items():
                        if key in ns and ns[key] != val:
                            self.report("optimizer", f"wrong_result_opt{opt}",
                                f"Optimizer level {opt} changed result for {prog!r}:\n"
                                f"  Expected {key}={val!r}, got {ns[key]!r}",
                                prog)
                    self.ok()
                except Exception as e:
                    if isinstance(e, SystemError):
                        self.report("optimizer", "system_error",
                            f"SystemError at opt level {opt}: {e}", prog)
                    self.ok()

    # ==========================================
    # 8. Code Object Edge Cases
    # ==========================================
    def test_code_objects(self):
        """Test code object manipulation and edge cases."""
        print("  Testing code objects...")

        # Test code.replace() with various modifications
        def original():
            x = 1
            y = 2
            return x + y

        code = original.__code__

        # Replace with valid modifications
        replacements = [
            {"co_name": "renamed"},
            {"co_filename": "new_file.py"},
            {"co_qualname": "new.qualname"},
        ]

        for kwargs in replacements:
            try:
                new_code = code.replace(**kwargs)
                # Create new function with modified code
                new_func = types.FunctionType(new_code, original.__globals__)
                result = new_func()
                if result != 3:
                    self.report("code_objects", f"replace_broke_semantics",
                        f"code.replace({kwargs}) changed result from 3 to {result}")
                self.ok()
            except SystemError as e:
                self.report("code_objects", "replace_system_error",
                    f"SystemError with code.replace({kwargs}): {e}")
            except Exception:
                self.ok()

        # Test marshal round-trip of code objects
        try:
            code = compile("def f(): return 42", "<test>", "exec")
            marshaled = marshal.dumps(code)
            restored = marshal.loads(marshaled)
            ns = {}
            exec(restored, ns)
            assert ns['f']() == 42
            self.ok()
        except SystemError as e:
            self.report("code_objects", "marshal_roundtrip",
                f"SystemError in marshal round-trip: {e}")

        # Test code with co_linetable edge cases (new in 3.12+)
        try:
            # Compile code with many lines
            lines = ["x = " + str(i) for i in range(1000)]
            code = compile("\n".join(lines), "<test>", "exec")
            # Check that line table is valid
            for inst in dis.get_instructions(code):
                if inst.starts_line is not None:
                    if inst.starts_line < 0:
                        self.report("code_objects", "negative_line",
                            f"Negative line number in instruction: {inst}")
            self.ok()
        except SystemError as e:
            self.report("code_objects", "linetable_error",
                f"SystemError with large line table: {e}")

    # ==========================================
    # 9. __static_attributes__ and __firstlineno__ (3.13)
    # ==========================================
    def test_class_new_attrs(self):
        """Test __static_attributes__ and __firstlineno__ (new in 3.13)."""
        print("  Testing class new attributes...")

        test_code = textwrap.dedent("""
        class Simple:
            x = 1
            def __init__(self):
                self.y = 2

        class WithSlots:
            __slots__ = ('a', 'b')
            def __init__(self):
                self.a = 1

        class Nested:
            class Inner:
                z = 3

        class WithClassVar:
            x: int = 1
            y: str = "hello"

        class Generic[T]:
            value: T
            def __init__(self, val: T):
                self.value = val
        """)

        try:
            ns = {}
            exec(test_code, ns)

            for class_name in ['Simple', 'WithSlots', 'Nested', 'WithClassVar', 'Generic']:
                cls = ns[class_name]

                # Check __static_attributes__ (new in 3.13)
                if hasattr(cls, '__static_attributes__'):
                    sa = cls.__static_attributes__
                    if not isinstance(sa, tuple):
                        self.report("class_attrs", "static_attrs_type",
                            f"{class_name}.__static_attributes__ is {type(sa)}, expected tuple")

                # Check __firstlineno__ (new in 3.13)
                if hasattr(cls, '__firstlineno__'):
                    fl = cls.__firstlineno__
                    if not isinstance(fl, int) or fl < 0:
                        self.report("class_attrs", "firstlineno_invalid",
                            f"{class_name}.__firstlineno__ = {fl}")

            self.ok()
        except SystemError as e:
            self.report("class_attrs", "system_error", f"SystemError: {e}", test_code)
        except Exception:
            self.ok()

    # ==========================================
    # 10. Traceback edge cases
    # ==========================================
    def test_traceback_edge_cases(self):
        """Test traceback with unusual exception chains and frames."""
        print("  Testing traceback edge cases...")

        # Test traceback with very deep exception chain
        try:
            def create_chain(n):
                if n == 0:
                    raise ValueError("base")
                try:
                    create_chain(n - 1)
                except Exception as e:
                    raise RuntimeError(f"level {n}") from e

            try:
                create_chain(20)
            except RuntimeError as e:
                # Format the traceback
                tb_str = traceback.format_exception(type(e), e, e.__traceback__)
                assert len(tb_str) > 0
            self.ok()
        except SystemError as e:
            self.report("traceback", "deep_chain_error",
                f"SystemError formatting deep exception chain: {e}")

        # Test traceback with ExceptionGroup
        try:
            try:
                raise ExceptionGroup("eg", [
                    ValueError("v1"),
                    ExceptionGroup("inner", [TypeError("t1"), KeyError("k1")]),
                ])
            except ExceptionGroup as eg:
                tb_str = traceback.format_exception(type(eg), eg, eg.__traceback__)
                assert len(tb_str) > 0
            self.ok()
        except SystemError as e:
            self.report("traceback", "exception_group_error",
                f"SystemError formatting ExceptionGroup traceback: {e}")

        # Test traceback.format_exception with None traceback
        try:
            try:
                raise ValueError("test")
            except ValueError as e:
                # Clear the traceback
                e.__traceback__ = None
                tb_str = traceback.format_exception(type(e), e, None)
                assert len(tb_str) > 0
            self.ok()
        except SystemError as e:
            self.report("traceback", "none_traceback_error",
                f"SystemError with None traceback: {e}")

    # ==========================================
    # 11. dis module edge cases
    # ==========================================
    def test_dis_edge_cases(self):
        """Test dis module with unusual code."""
        print("  Testing dis module...")

        programs = [
            "match x:\n case 1 | 2 | 3: pass\n case _: pass",
            "type Alias[T] = list[T]",
            "class C[T, U, *Vs, **P]: pass",
            "try:\n raise ExceptionGroup('e', [ValueError()])\nexcept* ValueError: pass",
            "[x for x in range(10) if (y := x) > 5]",
            "async def f():\n async for x in aiter:\n  pass",
            "def f(x, /, y, *, z): pass",
            "f'{1 + 2!r:.10}'",
        ]

        for prog in programs:
            try:
                code = compile(prog, "<test>", "exec")
                output = io.StringIO()
                dis.dis(code, file=output)

                # Also test get_instructions
                instructions = list(dis.get_instructions(code))
                for inst in instructions:
                    # Verify instruction attributes are valid
                    assert isinstance(inst.opname, str)
                    assert isinstance(inst.offset, int)
                    assert inst.offset >= 0

                # Test Bytecode object
                bc = dis.Bytecode(code)
                list(bc)

                self.ok()
            except SyntaxError:
                self.ok()
            except SystemError as e:
                self.report("dis", "system_error",
                    f"SystemError disassembling: {e}", prog)
            except Exception:
                self.ok()

    # ==========================================
    # 12. Random AST generation and compilation
    # ==========================================
    def test_random_ast(self):
        """Generate random valid ASTs and test compilation."""
        print("  Testing random AST generation...")

        random.seed(42)

        def random_expr(depth=0, max_depth=5):
            """Generate a random expression AST node."""
            if depth >= max_depth:
                # Terminal: constant
                return ast.Constant(value=random.choice([
                    0, 1, -1, 42, 3.14, True, False, None, "hello", b"bytes",
                ]))

            choice = random.randint(0, 10)
            if choice <= 2:
                return ast.Constant(value=random.choice([0, 1, -1, 42, 3.14, True, False, None, "x"]))
            elif choice == 3:
                return ast.BinOp(
                    left=random_expr(depth + 1, max_depth),
                    op=random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv(), ast.Mod()])(),
                    right=random_expr(depth + 1, max_depth),
                )
            elif choice == 4:
                return ast.UnaryOp(
                    op=random.choice([ast.UAdd(), ast.USub(), ast.Not(), ast.Invert()])(),
                    operand=random_expr(depth + 1, max_depth),
                )
            elif choice == 5:
                return ast.BoolOp(
                    op=random.choice([ast.And(), ast.Or()])(),
                    values=[random_expr(depth + 1, max_depth) for _ in range(random.randint(2, 4))],
                )
            elif choice == 6:
                return ast.Compare(
                    left=random_expr(depth + 1, max_depth),
                    ops=[random.choice([ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt()])()],
                    comparators=[random_expr(depth + 1, max_depth)],
                )
            elif choice == 7:
                return ast.IfExp(
                    test=random_expr(depth + 1, max_depth),
                    body=random_expr(depth + 1, max_depth),
                    orelse=random_expr(depth + 1, max_depth),
                )
            elif choice == 8:
                return ast.Tuple(
                    elts=[random_expr(depth + 1, max_depth) for _ in range(random.randint(0, 3))],
                    ctx=ast.Load(),
                )
            elif choice == 9:
                return ast.List(
                    elts=[random_expr(depth + 1, max_depth) for _ in range(random.randint(0, 3))],
                    ctx=ast.Load(),
                )
            else:
                return ast.Dict(
                    keys=[random_expr(depth + 1, max_depth) for _ in range(random.randint(0, 2))],
                    values=[random_expr(depth + 1, max_depth) for _ in range(random.randint(0, 2))],
                )

        for i in range(200):
            try:
                expr = random_expr()
                node = ast.Expression(body=expr)
                ast.fix_missing_locations(node)
                code = compile(node, f"<random_{i}>", "eval")
                try:
                    eval(code)
                except (TypeError, ValueError, ZeroDivisionError, OverflowError, NameError):
                    pass  # Expected runtime errors
                self.ok()
            except (TypeError, RecursionError):
                self.ok()  # Some random ASTs are invalid
            except SystemError as e:
                self.report("random_ast", f"system_error_{i}",
                    f"SystemError compiling random AST: {e}")
            except Exception:
                self.ok()

    # ==========================================
    # 13. marshal fuzzing
    # ==========================================
    def test_marshal_fuzzing(self):
        """Fuzz marshal.loads with slightly corrupted data."""
        print("  Testing marshal fuzzing...")

        random.seed(42)

        # Start with valid marshaled objects
        valid_objects = [
            None, True, False, 0, 1, -1, 2**30, 3.14,
            "", "hello", b"bytes", (), (1, 2, 3),
            [], [1, 2], {}, {1: 2}, set(), frozenset(),
        ]

        for obj in valid_objects:
            try:
                data = marshal.dumps(obj)
                # Mutate random bytes
                for _ in range(10):
                    mutated = bytearray(data)
                    if len(mutated) > 0:
                        pos = random.randint(0, len(mutated) - 1)
                        mutated[pos] = random.randint(0, 255)
                        try:
                            marshal.loads(bytes(mutated))
                        except (ValueError, TypeError, EOFError, MemoryError, OverflowError):
                            pass  # Expected
                        except SystemError as e:
                            self.report("marshal_fuzz", "system_error",
                                f"SystemError with corrupted marshal data: {e}\n"
                                f"Original obj: {obj!r}")
                self.ok()
            except Exception:
                self.ok()

        # Fuzz marshal with code objects
        try:
            code = compile("x = 1", "<test>", "exec")
            data = marshal.dumps(code)
            for _ in range(20):
                mutated = bytearray(data)
                if len(mutated) > 1:
                    pos = random.randint(1, len(mutated) - 1)
                    mutated[pos] = random.randint(0, 255)
                    try:
                        obj = marshal.loads(bytes(mutated))
                        if isinstance(obj, types.CodeType):
                            try:
                                exec(obj)
                            except Exception:
                                pass  # Expected
                    except (ValueError, TypeError, EOFError, MemoryError, OverflowError):
                        pass
                    except SystemError as e:
                        self.report("marshal_fuzz", "code_system_error",
                            f"SystemError with corrupted code marshal: {e}")
            self.ok()
        except Exception:
            self.ok()

    # ==========================================
    # 14. Specializing interpreter stress test
    # ==========================================
    def test_specialization(self):
        """Test the specializing interpreter (PEP 659)."""
        print("  Testing specializing interpreter...")

        # The specializing interpreter optimizes bytecode based on observed types
        # We test by running functions many times with different types

        def add(a, b):
            return a + b

        # Run with ints (should specialize for ints)
        for _ in range(200):
            assert add(1, 2) == 3

        # Now run with floats (should despecialize or respecialize)
        for _ in range(200):
            assert add(1.0, 2.0) == 3.0

        # Now run with strings
        for _ in range(200):
            assert add("hello", " world") == "hello world"

        # Now mix types rapidly
        type_pairs = [
            (1, 2), (1.0, 2.0), ("a", "b"),
            ([1], [2]), ((1,), (2,)),
        ]
        for _ in range(200):
            a, b = random.choice(type_pairs)
            try:
                add(a, b)
            except TypeError:
                pass

        self.ok()

        # Test attribute access specialization
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Point(1, 2)
        for _ in range(200):
            assert p.x == 1
            assert p.y == 2

        # Change __class__
        class Point3D:
            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

        try:
            p.__class__ = Point3D
            p.z = 3
            for _ in range(100):
                assert p.x == 1
                assert p.z == 3
        except TypeError:
            pass

        self.ok()

        # Test subscript specialization
        d = {"a": 1, "b": 2}
        for _ in range(200):
            assert d["a"] == 1

        lst = [1, 2, 3]
        for _ in range(200):
            assert lst[0] == 1

        # Mix subscript types
        containers = [d, lst, (1, 2, 3)]
        keys = ["a", 0, 1]
        for _ in range(200):
            c = random.choice(containers)
            k = random.choice(keys)
            try:
                c[k]
            except (KeyError, IndexError, TypeError):
                pass

        self.ok()

    # ==========================================
    # 15. Complex interaction tests
    # ==========================================
    def test_complex_interactions(self):
        """Test complex interactions between features."""
        print("  Testing complex interactions...")

        # Test: monitoring + generators + exception groups
        try:
            events = []
            TOOL_ID = 3
            E = sys.monitoring.events

            sys.monitoring.use_tool_id(TOOL_ID, "interaction_test")

            def line_cb(code, line):
                events.append(('line', line))

            sys.monitoring.register_callback(TOOL_ID, E.LINE, line_cb)
            sys.monitoring.set_events(TOOL_ID, E.LINE)

            def gen_with_exception():
                yield 1
                raise ValueError("test")

            try:
                for val in gen_with_exception():
                    pass
            except ValueError:
                pass

            sys.monitoring.set_events(TOOL_ID, 0)
            sys.monitoring.register_callback(TOOL_ID, E.LINE, None)
            sys.monitoring.free_tool_id(TOOL_ID)
            self.ok()
        except Exception as e:
            try:
                sys.monitoring.set_events(TOOL_ID, 0)
                sys.monitoring.free_tool_id(TOOL_ID)
            except Exception:
                pass
            if isinstance(e, SystemError):
                self.report("interaction", "monitoring_gen_eg",
                    f"SystemError in monitoring+generator+exception: {e}")
            self.ok()

        # Test: type params + match + async
        test_code = textwrap.dedent("""
        import asyncio

        class Container[T]:
            def __init__(self, value: T):
                self.value = value

        async def process[T](container: Container[T]) -> T:
            match container:
                case Container(value=int(x)):
                    return x * 2
                case Container(value=str(s)):
                    return s.upper()
                case _:
                    return container.value

        async def main():
            c1 = Container(21)
            result1 = await process(c1)
            assert result1 == 42

            c2 = Container("hello")
            result2 = await process(c2)
            assert result2 == "HELLO"

        asyncio.run(main())
        """)

        try:
            exec(test_code)
            self.ok()
        except SystemError as e:
            self.report("interaction", "type_match_async",
                f"SystemError with type params + match + async: {e}")
        except Exception:
            self.ok()

        # Test: walrus + except* + f-string
        test_code2 = textwrap.dedent("""
        try:
            raise ExceptionGroup("eg", [ValueError("v1"), TypeError("t1")])
        except* ValueError as eg:
            if (count := len(eg.exceptions)) > 0:
                msg = f"Caught {count} ValueError(s): {eg.exceptions[0]!r}"
        except* TypeError:
            pass
        """)

        try:
            exec(test_code2)
            self.ok()
        except SystemError as e:
            self.report("interaction", "walrus_except_star_fstring",
                f"SystemError with walrus + except* + f-string: {e}")
        except Exception:
            self.ok()

    # ==========================================
    # 16. Edge cases in newer builtins / stdlib
    # ==========================================
    def test_newer_stdlib(self):
        """Test newer stdlib additions and changes."""
        print("  Testing newer stdlib...")

        # Test typing module edge cases
        try:
            from typing import TypeVar, ParamSpec, TypeVarTuple, TypeAlias
            from typing import Annotated, TypeGuard, TypeIs, assert_type
            from typing import override, dataclass_transform

            T = TypeVar('T')
            P = ParamSpec('P')
            Ts = TypeVarTuple('Ts')

            # TypeIs (PEP 742, 3.13)
            def is_str(x: object) -> TypeIs[str]:
                return isinstance(x, str)

            assert is_str("hello")
            assert not is_str(42)

            self.ok()
        except ImportError:
            self.ok()
        except SystemError as e:
            self.report("newer_stdlib", "typing_error",
                f"SystemError with typing: {e}")
        except Exception:
            self.ok()

        # Test dataclasses with newer features
        try:
            from dataclasses import dataclass, field

            @dataclass
            class Point[T]:
                x: T
                y: T

            p = Point(1, 2)
            assert p.x == 1
            assert p.y == 2

            @dataclass
            class Config:
                name: str = "default"
                values: list = field(default_factory=list)

            c = Config()
            assert c.name == "default"
            assert c.values == []

            self.ok()
        except SystemError as e:
            self.report("newer_stdlib", "dataclass_error",
                f"SystemError with dataclasses: {e}")
        except Exception:
            self.ok()

        # Test functools.cache (3.9+) edge cases
        try:
            @functools.cache
            def fib(n):
                if n < 2:
                    return n
                return fib(n - 1) + fib(n - 2)

            assert fib(10) == 55
            assert fib(30) == 832040
            fib.cache_clear()

            self.ok()
        except SystemError as e:
            self.report("newer_stdlib", "cache_error",
                f"SystemError with functools.cache: {e}")

    def run_all(self):
        """Run all semantic tests."""
        print(f"CPython 3.13 Semantic Correctness Fuzzer")
        print(f"Python: {sys.version}")
        print()

        test_methods = [
            self.test_ast_roundtrip,
            self.test_error_attributes,
            self.test_compile_consistency,
            self.test_pep667_locals,
            self.test_monitoring_api,
            self.test_symtable,
            self.test_optimizer_correctness,
            self.test_code_objects,
            self.test_class_new_attrs,
            self.test_traceback_edge_cases,
            self.test_dis_edge_cases,
            self.test_random_ast,
            self.test_marshal_fuzzing,
            self.test_specialization,
            self.test_complex_interactions,
            self.test_newer_stdlib,
        ]

        for method in test_methods:
            try:
                method()
            except Exception as e:
                print(f"  ERROR in {method.__name__}: {e}")
                if isinstance(e, SystemError):
                    self.report("runner", method.__name__,
                        f"Unhandled SystemError: {e}")

        print(f"\n{'='*60}")
        print(f"Tests run: {self.tests_run}")
        print(f"Findings: {len(self.findings)}")

        if self.findings:
            print(f"\nFINDINGS:")
            for i, f in enumerate(self.findings, 1):
                print(f"\n--- Finding {i} ---")
                print(f"Category: {f.category}")
                print(f"Name: {f.name}")
                print(f"Details: {f.details}")
                if f.code:
                    print(f"Code:\n{textwrap.indent(f.code[:300], '  ')}")
        else:
            print("No issues found.")
        print(f"{'='*60}")

        return self.findings


if __name__ == "__main__":
    fuzzer = SemanticFuzzer()
    findings = fuzzer.run_all()
    sys.exit(1 if findings else 0)

"""
Aggressive CPython 3.13 fuzzer targeting areas most likely to have bugs.
Focuses on: parser edge cases, compiler/optimizer bugs, interaction bugs,
and features new in 3.12/3.13.
"""

import sys
import os
import ast
import types
import gc
import weakref
import traceback
import textwrap
import struct
import copy
import io
import marshal
import dis
import re
import threading
import time
import pickle
import json
import functools
import itertools
import operator
import collections
import array
import bisect
import heapq
import random
import contextlib
import subprocess
import tempfile


def make_test(code, name):
    """Create a test case dict."""
    return {"name": name, "code": code}


def run_in_subprocess(code, timeout=15):
    """Run code in a subprocess and return (exit_code, stdout, stderr)."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        temp_path = f.name
    try:
        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True, text=True, timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -999, "", "TIMEOUT"
    finally:
        try:
            os.unlink(temp_path)
        except:
            pass


class AggressiveFuzzer:
    """Aggressively fuzzes CPython with targeted test cases."""

    def __init__(self):
        self.findings = []
        self.tests_run = 0

    def report(self, name, details, code=""):
        """Report a finding."""
        self.findings.append({
            "name": name,
            "details": details,
            "code": code
        })
        print(f"\n  *** FINDING: {name} ***")
        print(f"  {details}")
        if code:
            print(f"  Code: {code[:200]}")

    def check_subprocess(self, code, name, timeout=15):
        """Run code in subprocess and check for crashes."""
        self.tests_run += 1
        exit_code, stdout, stderr = run_in_subprocess(code, timeout)

        # Check for crashes
        unsigned = exit_code & 0xFFFFFFFF if exit_code < 0 else exit_code
        crash_codes = {
            0xC0000005: "ACCESS_VIOLATION",
            0xC0000409: "STACK_BUFFER_OVERRUN",
            0xC000001D: "ILLEGAL_INSTRUCTION",
            0xC00000FD: "STACK_OVERFLOW",
            0xC0000374: "HEAP_CORRUPTION",
        }
        if unsigned in crash_codes:
            self.report(name, f"CRASH: {crash_codes[unsigned]} (exit code {exit_code})", code)
            return True

        # Check for fatal errors
        stderr_lower = stderr.lower()
        if "fatal python error" in stderr_lower:
            self.report(name, f"FATAL ERROR: {stderr[:300]}", code)
            return True

        if "systemerror" in stderr_lower:
            for line in stderr.split('\n'):
                if 'systemerror' in line.lower() and 'except' not in line.lower():
                    self.report(name, f"SystemError: {stderr[:300]}", code)
                    return True

        if exit_code == -999:
            return False  # timeout, not a bug

        return False

    def test_parser_edge_cases(self):
        """Aggressive parser edge cases."""
        print("  Testing parser edge cases...")

        # PEG parser stress tests
        cases = [
            # Extremely deep nesting
            ("parser_deep_parens", "(" * 500 + "1" + ")" * 500),
            ("parser_deep_brackets", "[" * 200 + "1" + "]" * 200),

            # Complex expressions
            ("parser_complex_ternary", " if ".join(["True"] * 50) + " else False" * 49),
            ("parser_complex_or", " or ".join(["x"] * 200)),
            ("parser_complex_and", " and ".join(["x"] * 200)),
            ("parser_complex_compare", " < ".join([str(i) for i in range(100)]),),

            # Assignment targets
            ("parser_star_assign_1", "(a, *b, *c) = [1,2,3]"),  # Two stars - should error
            ("parser_nested_star", "(*a,) = (*b,) = [1,2,3]"),

            # Decorator edge cases
            ("parser_dec_complex", "@(x := lambda f: (y := f))\ndef g(): pass"),
            ("parser_dec_await", "async def outer():\n @(await coro)\n def f(): pass"),

            # Very complex type annotations
            ("parser_type_complex",
             "x: dict[str, list[tuple[int, ...]]] | None = None"),
            ("parser_type_union_many",
             "x: " + " | ".join(f"Type{i}" for i in range(100)) + " = None"),

            # Unusual string concatenation
            ("parser_str_concat", " ".join([f'"{i}"' for i in range(100)])),

            # Multiline constructs
            ("parser_multiline_dict", "x = {\n" + ",\n".join(f"  {i}: {i}" for i in range(500)) + "\n}"),
            ("parser_multiline_list", "x = [\n" + ",\n".join(f"  {i}" for i in range(500)) + "\n]"),

            # f-string stress
            ("parser_fstring_deep", 'f"{ f"{ f"{ f"{ f"{ 1 }" }" }" }" }"'),
            ("parser_fstring_many_exprs", 'f"' + ''.join(f'{{{i}}}' for i in range(100)) + '"'),

            # Match statement with complex patterns
            ("parser_match_complex", """
match (1, 2, {"a": [3, 4]}):
    case (int(x), int(y), {"a": [int(z), *rest]}) if x + y > 0:
        pass
    case _:
        pass
"""),
            # Walrus in unusual positions
            ("parser_walrus_nested", "[(y := x) for x in range(10) if (z := y) > 0]"),
            ("parser_walrus_lambda", "(lambda: (x := 1))()"),

            # Multiple assignment with type annotations
            ("parser_annotated_multi", "x: int = y: str = 1"),

            # Generator expressions in various contexts
            ("parser_genexpr_call", "list(x for x in range(10))"),
            ("parser_genexpr_add", "sum(x**2 for x in range(10))"),

            # Complex comprehensions
            ("parser_nested_comp", "[[[k for k in range(j)] for j in range(i)] for i in range(5)]"),

            # Type parameter syntax (PEP 695)
            ("parser_type_param_complex",
             "class C[T: (int, str), U: float, *Vs, **P]:\n    pass"),
            ("parser_type_alias_recursive",
             "type Tree[T] = T | list[Tree[T]]"),
            ("parser_generic_nested",
             "class Outer[T]:\n    class Inner[U]:\n        def method[V](self, x: T, y: U) -> V: ..."),

            # except* in unusual positions
            ("parser_except_star_nested", """
try:
    try:
        raise ExceptionGroup("eg", [ValueError(1)])
    except* ValueError as eg1:
        try:
            raise ExceptionGroup("eg2", [TypeError(2)])
        except* TypeError as eg2:
            pass
except BaseException:
    pass
"""),
        ]

        for name, code in cases:
            self.check_subprocess(code, name)

    def test_compiler_optimizer(self):
        """Test the compiler/optimizer (peephole optimizer, etc.)."""
        print("  Testing compiler/optimizer...")

        cases = [
            # Constant folding edge cases
            ("opt_const_fold_1", "x = " + " + ".join(["1"] * 1000)),
            ("opt_const_fold_2", "x = " + " * ".join(["2"] * 100)),
            ("opt_const_fold_str", 'x = ' + ' + '.join(['"a"'] * 500)),
            ("opt_const_fold_tuple", 'x = (' + ', '.join(['1'] * 1000) + ',)'),

            # Dead code elimination
            ("opt_dead_code", """
def f():
    return 1
    x = 2  # dead code
    y = 3  # dead code
    return y  # dead code
"""),

            # Jump optimization
            ("opt_jump", """
def f(x):
    if x:
        if x:
            if x:
                if x:
                    return 1
    return 0
"""),

            # Loop optimization
            ("opt_loop", """
def f():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                pass
"""),

            # Generator optimization
            ("opt_generator", """
def f():
    return list(x for x in range(1000) if x % 2 == 0)
f()
"""),

            # Complex default arguments
            ("opt_defaults", """
def f(a=[], b={}, c=set(), d=(), e=frozenset()):
    return (a, b, c, d, e)
"""),

            # Annotation processing
            ("opt_annotations", """
def f(x: 'complex_type[int, str]', y: dict[str, list[int]] = {}) -> tuple[int, ...]:
    pass
"""),

            # __debug__ optimization
            ("opt_debug", """
if __debug__:
    x = 1
else:
    x = 2
"""),
        ]

        for name, code in cases:
            self.check_subprocess(code, name)

    def test_runtime_edge_cases(self):
        """Test runtime behavior edge cases."""
        print("  Testing runtime edge cases...")

        cases = [
            # Dynamic attribute access chain
            ("rt_attr_chain", """
class A:
    class B:
        class C:
            class D:
                x = 42
assert A.B.C.D.x == 42
"""),

            # __getattr__ / __getattribute__ interaction
            ("rt_getattr_interaction", """
class C:
    def __getattribute__(self, name):
        if name == 'x':
            return 42
        return super().__getattribute__(name)
    def __getattr__(self, name):
        if name == 'y':
            return 99
        raise AttributeError(name)
c = C()
assert c.x == 42
assert c.y == 99
try:
    c.z
except AttributeError:
    pass
"""),

            # __del__ ordering with weak references
            ("rt_del_weakref", """
import gc, weakref
order = []
class C:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        order.append(self.name)
c1 = C("first")
c2 = C("second")
r1 = weakref.ref(c1)
r2 = weakref.ref(c2)
c1.other = c2
c2.other = c1
del c1, c2
gc.collect()
"""),

            # __missing__ in dict subclass
            ("rt_dict_missing", """
class AutoDict(dict):
    def __missing__(self, key):
        self[key] = AutoDict()
        return self[key]
d = AutoDict()
d['a']['b']['c'] = 42
assert d['a']['b']['c'] == 42
"""),

            # __instancecheck__ and __subclasscheck__
            ("rt_instance_check", """
class AlwaysTrueMeta(type):
    def __instancecheck__(cls, instance):
        return True
    def __subclasscheck__(cls, subclass):
        return True
class AlwaysTrue(metaclass=AlwaysTrueMeta):
    pass
assert isinstance(42, AlwaysTrue)
assert isinstance("hello", AlwaysTrue)
assert issubclass(int, AlwaysTrue)
"""),

            # super() without arguments in various contexts
            ("rt_super_complex", """
class A:
    def method(self):
        return 'A'
class B(A):
    def method(self):
        return super().method() + 'B'
class C(A):
    def method(self):
        return super().method() + 'C'
class D(B, C):
    def method(self):
        return super().method() + 'D'
assert D().method() == 'ACBD'
"""),

            # Closure over loop variable
            ("rt_closure_loop", """
funcs = [lambda i=i: i for i in range(10)]
assert [f() for f in funcs] == list(range(10))

# Without default arg (capturing loop variable)
funcs2 = []
for i in range(10):
    def f(x=i):
        return x
    funcs2.append(f)
assert [f() for f in funcs2] == list(range(10))
"""),

            # Generator send/throw/close interactions
            ("rt_gen_complex", """
def gen():
    try:
        val = yield 'start'
        while True:
            try:
                val = yield f'got {val}'
            except ValueError:
                val = yield 'caught ValueError'
    except GeneratorExit:
        pass  # Don't yield after GeneratorExit

g = gen()
assert next(g) == 'start'
assert g.send(1) == 'got 1'
assert g.send(2) == 'got 2'
assert g.throw(ValueError) == 'caught ValueError'
g.close()
"""),

            # Coroutine lifecycle
            ("rt_coro_lifecycle", """
import asyncio
async def coro():
    return 42
c = coro()
try:
    c.send(None)
except StopIteration as e:
    assert e.value == 42
"""),

            # Class with both __slots__ and __dict__
            ("rt_slots_dict", """
class C:
    __slots__ = ('x',)
    def __init__(self):
        self.x = 1

class D(C):
    pass  # D gets __dict__ since it doesn't define __slots__

d = D()
d.x = 1
d.y = 2  # Goes to __dict__
assert d.x == 1
assert d.y == 2
"""),

            # Multiple inheritance with C3 linearization edge cases
            ("rt_mro_complex", """
class O: pass
class A(O): pass
class B(O): pass
class C(O): pass
class D(A, B): pass
class E(B, C): pass
class F(D, E): pass
# F's MRO should be computable
mro = F.__mro__
assert F in mro
assert object in mro
"""),

            # __init_subclass__ with kwargs
            ("rt_init_subclass_kwargs", """
class Plugin:
    plugins = {}
    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if name:
            Plugin.plugins[name] = cls

class MyPlugin(Plugin, name="my_plugin"):
    pass

assert Plugin.plugins == {"my_plugin": MyPlugin}
"""),

            # Dynamic type() with complex namespace
            ("rt_dynamic_type", """
ns = {
    '__init__': lambda self, x: setattr(self, 'x', x),
    '__repr__': lambda self: f'Dynamic({self.x})',
    '__eq__': lambda self, other: isinstance(other, type(self)) and self.x == other.x,
    '__hash__': lambda self: hash(self.x),
}
Dynamic = type('Dynamic', (object,), ns)
d = Dynamic(42)
assert repr(d) == 'Dynamic(42)'
assert d == Dynamic(42)
assert hash(d) == hash(42)
"""),

            # Context manager edge cases
            ("rt_contextmgr_throw", """
class ThrowingCM:
    def __enter__(self):
        return self
    def __exit__(self, *args):
        raise RuntimeError("exit error")

try:
    with ThrowingCM():
        raise ValueError("body error")
except RuntimeError as e:
    assert str(e) == "exit error"
"""),

            # Exception chaining
            ("rt_exception_chain", """
try:
    try:
        raise ValueError("original")
    except ValueError:
        raise TypeError("secondary") from None
except TypeError as e:
    assert e.__cause__ is None
    assert e.__suppress_context__ is True
"""),

            # Very deep exception chain
            ("rt_deep_exception_chain", """
def create_chain(n):
    if n == 0:
        raise ValueError("base")
    try:
        create_chain(n - 1)
    except Exception as e:
        raise RuntimeError(f"level {n}") from e

try:
    create_chain(50)
except RuntimeError as e:
    # Walk the chain
    count = 0
    exc = e
    while exc is not None:
        count += 1
        exc = exc.__cause__
    assert count == 51, f"Expected 51, got {count}"
"""),
        ]

        for name, code in cases:
            self.check_subprocess(code, name)

    def test_new_313_features(self):
        """Test features new or changed in Python 3.12/3.13."""
        print("  Testing 3.12/3.13 features...")

        cases = [
            # Type parameter syntax (PEP 695) - new in 3.12
            ("313_type_alias", """
type Vector = list[float]
type Matrix[T] = list[list[T]]
type Recursive[T] = T | list[Recursive[T]]
"""),

            ("313_generic_class", """
class Stack[T]:
    def __init__(self):
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
    def pop(self) -> T:
        return self._items.pop()

s = Stack[int]()
s.push(1)
assert s.pop() == 1
"""),

            ("313_generic_func", """
def first[T](lst: list[T]) -> T:
    return lst[0]
assert first([1, 2, 3]) == 1
assert first(["a", "b"]) == "a"
"""),

            ("313_type_param_bound", """
class Comparable[T: (int, float, str)]:
    def __init__(self, val: T):
        self.val = val
    def compare(self, other: T) -> bool:
        return self.val < other
"""),

            ("313_paramspec", """
from typing import Callable
def decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet(name: str) -> str:
    return f"Hello, {name}!"

assert greet("World") == "Hello, World!"
"""),

            ("313_typevartuple", """
def multi_len[*Ts](*args: *Ts) -> int:
    return len(args)
assert multi_len(1, "two", 3.0) == 3
"""),

            # Exception groups (PEP 654) - new in 3.11
            ("313_taskgroup", """
import asyncio
async def worker(n):
    if n == 3:
        raise ValueError(f"error in worker {n}")
    return n

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(worker(i)) for i in range(5)]
    except* ValueError as eg:
        assert len(eg.exceptions) == 1
    except* Exception:
        pass

asyncio.run(main())
"""),

            # f-string changes (3.12 - unlimited nesting, backslash, comments)
            ("313_fstring_new", """
# Nested f-strings
x = 42
result = f"{ f"{ f"{ x }" }" }"
assert result == "42"

# Backslash in f-string expression
newline = f"{'\\n'}"
assert newline == "\\n"

# Multi-line f-string expression
result = f"{
    1 +
    2 +
    3
}"
assert result == "6"
"""),

            # Per-interpreter GIL (3.12/3.13) - test interpreters module
            ("313_interpreters", """
try:
    import _interpreters
    # Create a sub-interpreter
    interp_id = _interpreters.create()
    _interpreters.run_string(interp_id, "x = 42")
    _interpreters.destroy(interp_id)
except (ImportError, ModuleNotFoundError):
    pass  # Module may not be available
except Exception as e:
    pass  # OK, just testing it doesn't crash
"""),

            # Improved error messages (3.12/3.13)
            ("313_error_messages", """
import ast
# Test that error messages are reasonable
test_cases = [
    ("x = ", "expected"),
    ("def f(x, x): pass", "duplicate"),
    ("class 123: pass", "invalid"),
    ("del ()", "invalid"),
]
for code, _ in test_cases:
    try:
        compile(code, "<test>", "exec")
    except SyntaxError as e:
        # Just make sure it doesn't crash
        assert e.msg is not None
        assert isinstance(e.lineno, int)
"""),

            # Dead batteries (deprecated modules in 3.13)
            ("313_deprecated_modules", """
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    deprecated = [
        'aifc', 'audioop', 'cgi', 'cgitb', 'chunk',
        'imghdr', 'mailcap', 'msilib', 'nis', 'nntplib',
        'ossaudiodev', 'pipes', 'sndhdr', 'spwd', 'sunau',
        'telnetlib', 'uu', 'xdrlib',
    ]
    for mod in deprecated:
        try:
            __import__(mod)
        except (ImportError, ModuleNotFoundError, OSError):
            pass
"""),

            # TypedDict (improvements in 3.12+)
            ("313_typeddict", """
from typing import TypedDict, Required, NotRequired

class Movie(TypedDict):
    title: str
    year: int
    rating: NotRequired[float]

m: Movie = {"title": "Test", "year": 2024}
assert m["title"] == "Test"
"""),

            # Buffer protocol (PEP 688, 3.12)
            ("313_buffer_protocol", """
class MyBuffer:
    def __init__(self, data: bytes):
        self._data = data
    def __buffer__(self, flags: int) -> memoryview:
        return memoryview(self._data)

try:
    b = MyBuffer(b"hello")
    mv = memoryview(b)
    assert bytes(mv) == b"hello"
    mv.release()
except TypeError:
    pass  # May not work in all versions
"""),

            # Perf profiling support (3.12)
            ("313_perf_maps", """
import sys
try:
    sys.activate_stack_trampoline("perf")
except (AttributeError, ValueError, RuntimeError):
    pass  # May not be available on Windows
"""),

            # Comprehension inlining (3.12 optimization)
            ("313_comp_inline", """
x = 10
result = [x for x in range(5)]
# In 3.12+, comprehension is inlined, so x should be overwritten
# But the spec says comprehension variables don't leak
assert x == 10  # x should not be affected
"""),

            # Immortal objects (3.12+)
            ("313_immortal", """
import sys
# None, True, False should be immortal in 3.12+
assert sys.getrefcount(None) > 0
assert sys.getrefcount(True) > 0
assert sys.getrefcount(False) > 0
# Small integers should be immortal
assert sys.getrefcount(0) > 0
assert sys.getrefcount(1) > 0
"""),

            # Monitoring API (PEP 669, 3.12)
            ("313_monitoring", """
import sys
try:
    events = sys.monitoring.events
    sys.monitoring.use_tool_id(0, "test_tool")
    def callback(*args):
        pass
    sys.monitoring.register_callback(0, events.LINE, callback)
    sys.monitoring.set_events(0, events.LINE)

    x = 1 + 2

    sys.monitoring.set_events(0, 0)
    sys.monitoring.free_tool_id(0)
except (AttributeError, ValueError):
    pass
"""),
        ]

        for name, code in cases:
            self.check_subprocess(code, name)

    def test_crash_vectors(self):
        """Test known crash vectors and dangerous patterns."""
        print("  Testing crash vectors...")

        cases = [
            # Stack overflow via recursion
            ("crash_recursion_1", """
import sys
sys.setrecursionlimit(100000)
def f(): f()
try:
    f()
except RecursionError:
    pass
"""),

            # Stack overflow via __repr__
            ("crash_repr_cycle", """
import sys
sys.setrecursionlimit(200)
class C:
    def __repr__(self):
        return repr(self)
try:
    repr(C())
except RecursionError:
    pass
"""),

            # Stack overflow via __str__
            ("crash_str_cycle", """
import sys
sys.setrecursionlimit(200)
class C:
    def __str__(self):
        return str(self)
try:
    str(C())
except RecursionError:
    pass
"""),

            # Memory pressure
            ("crash_memory", """
try:
    x = [0] * (10**8)
except MemoryError:
    pass
"""),

            # __del__ during interpreter shutdown
            ("crash_del_shutdown", """
import atexit
class C:
    def __del__(self):
        try:
            import sys
        except ImportError:
            pass
c = C()
"""),

            # Signal handling edge cases (not really applicable on Windows)
            ("crash_signal", """
import signal
def handler(signum, frame):
    pass
old = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGINT, old)
"""),

            # Compile with specific flags
            ("crash_compile_flags", """
import ast
flags = ast.PyCF_ALLOW_TOP_LEVEL_AWAIT | ast.PyCF_ONLY_AST
code = compile("async def f(): await x", "<test>", "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
exec(code)
"""),

            # Thread + GC interaction
            ("crash_thread_gc", """
import threading, gc
class C:
    def __del__(self):
        pass

def worker():
    for _ in range(1000):
        c = C()
        del c
    gc.collect()

threads = [threading.Thread(target=worker) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
"""),

            # eval() with custom __getitem__ on globals
            ("crash_eval_custom_globals", """
class FakeGlobals(dict):
    def __getitem__(self, key):
        if key == '__builtins__':
            return __builtins__
        raise KeyError(key)
    def __contains__(self, key):
        return key == '__builtins__'

try:
    eval("1 + 2", FakeGlobals())
except Exception:
    pass
"""),

            # Concurrent import
            ("crash_concurrent_import", """
import threading
import importlib

def import_worker():
    for _ in range(10):
        try:
            importlib.import_module('json')
            importlib.import_module('collections')
        except Exception:
            pass

threads = [threading.Thread(target=import_worker) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
"""),

            # Very long traceback
            ("crash_long_traceback", """
import sys
sys.setrecursionlimit(500)
def f(n):
    if n <= 0:
        raise ValueError("deep")
    f(n - 1)

try:
    f(400)
except (ValueError, RecursionError):
    pass
"""),

            # Object with __del__ that creates reference cycles
            ("crash_del_cycle_creation", """
import gc
refs = []
class Cycler:
    def __del__(self):
        # Create a new cycle during __del__
        a = Cycler.__new__(Cycler)
        b = Cycler.__new__(Cycler)
        a.ref = b
        b.ref = a
        refs.append(a)

for _ in range(100):
    c = Cycler()
    del c
gc.collect()
gc.collect()
"""),

            # Multiple inheritance with conflicting __slots__
            ("crash_slots_conflict", """
class A:
    __slots__ = ('x',)
class B:
    __slots__ = ('y',)
class C(A, B):
    __slots__ = ('z',)
c = C()
c.x = 1
c.y = 2
c.z = 3
"""),

            # sys.settrace with generator
            ("crash_trace_generator", """
import sys
def tracer(frame, event, arg):
    return tracer
sys.settrace(tracer)
try:
    def gen():
        yield 1
        yield 2
    list(gen())
finally:
    sys.settrace(None)
"""),

            # sys.settrace with exception
            ("crash_trace_exception", """
import sys
calls = []
def tracer(frame, event, arg):
    calls.append(event)
    if event == 'exception':
        return tracer
    return tracer

sys.settrace(tracer)
try:
    try:
        raise ValueError("test")
    except ValueError:
        pass
finally:
    sys.settrace(None)
"""),

            # Complex __init_subclass__ chain
            ("crash_init_subclass_chain", """
class A:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
class B(A):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
class C(B):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
class D(C): pass
class E(D): pass
"""),

            # __prepare__ metaclass
            ("crash_metaclass_prepare", """
class OrderedMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return {}

class C(metaclass=OrderedMeta):
    x = 1
    y = 2
    z = 3
"""),
        ]

        for name, code in cases:
            self.check_subprocess(code, name)

    def test_bytecode_edge_cases(self):
        """Test bytecode/code object edge cases that might expose bugs."""
        print("  Testing bytecode edge cases...")

        cases = [
            # exec with code that creates closures
            ("bytecode_closure_exec", """
code = '''
def outer():
    x = 42
    def inner():
        return x
    return inner()
result = outer()
'''
ns = {}
exec(code, ns)
assert ns['result'] == 42
"""),

            # Nested comprehensions with closures
            ("bytecode_nested_comp", """
def f():
    x = 10
    return [[x + j for j in range(i)] for i in range(5)]
result = f()
assert result == [[], [10], [10, 11], [10, 11, 12], [10, 11, 12, 13]]
"""),

            # Lambda in comprehension
            ("bytecode_lambda_comp", """
funcs = [lambda x=i: x for i in range(5)]
assert [f() for f in funcs] == [0, 1, 2, 3, 4]
"""),

            # Generator with yield in try/finally
            ("bytecode_gen_finally", """
def gen():
    try:
        yield 1
        yield 2
    finally:
        pass

g = gen()
assert next(g) == 1
g.close()  # Should trigger finally
"""),

            # Async generator with cleanup
            ("bytecode_async_gen_cleanup", """
import asyncio

async def agen():
    try:
        yield 1
        yield 2
    finally:
        pass

async def main():
    ag = agen()
    val = await ag.__anext__()
    assert val == 1
    await ag.aclose()

asyncio.run(main())
"""),

            # Extended unpacking in various contexts
            ("bytecode_unpack", """
# Extended unpacking
a, *b, c = range(10)
assert a == 0
assert b == list(range(1, 9))
assert c == 9

# Nested unpacking
(a, b), (c, d) = [1, 2], [3, 4]
assert (a, b, c, d) == (1, 2, 3, 4)

# Star in nested
(a, *b), c = [1, 2, 3], 4
assert (a, b, c) == (1, [2, 3], 4)
"""),

            # try/except/else/finally with various flows
            ("bytecode_try_flows", """
result = []
def test(should_raise):
    try:
        result.append('try')
        if should_raise:
            raise ValueError("test")
    except ValueError:
        result.append('except')
    else:
        result.append('else')
    finally:
        result.append('finally')

result.clear()
test(False)
assert result == ['try', 'else', 'finally']

result.clear()
test(True)
assert result == ['try', 'except', 'finally']
"""),

            # for/else and while/else
            ("bytecode_loop_else", """
# for/else - else runs when loop completes normally
for i in range(5):
    if i == 10:
        break
else:
    x = "no break"
assert x == "no break"

# for/else - else doesn't run after break
for i in range(5):
    if i == 3:
        break
else:
    x = "shouldn't reach"
assert i == 3
"""),
        ]

        for name, code in cases:
            self.check_subprocess(code, name)

    def test_edge_case_interactions(self):
        """Test interactions between multiple features."""
        print("  Testing feature interactions...")

        cases = [
            # Pattern matching + exception groups
            ("interact_match_except", """
import asyncio

async def failing():
    raise ValueError("test")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(failing())
    except* ValueError as eg:
        match eg:
            case ExceptionGroup():
                pass

asyncio.run(main())
"""),

            # Type params + decorators
            ("interact_type_dec", """
def logged(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@logged
def identity[T](x: T) -> T:
    return x

assert identity(42) == 42
"""),

            # Walrus + match
            ("interact_walrus_match", """
data = [1, 2, 3]
match (length := len(data)):
    case 3:
        assert length == 3
    case _:
        assert False
"""),

            # Generator + tracing
            ("interact_gen_trace", """
import sys
events = []
def tracer(frame, event, arg):
    if frame.f_code.co_name == 'gen':
        events.append(event)
    return tracer

def gen():
    yield 1
    yield 2

sys.settrace(tracer)
try:
    list(gen())
finally:
    sys.settrace(None)
"""),

            # f-string + pattern matching
            ("interact_fstring_match", """
value = 42
match f"value is {value}":
    case "value is 42":
        result = True
    case _:
        result = False
assert result
"""),

            # Exception group + context manager
            ("interact_eg_cm", """
class MyCM:
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False  # Don't suppress

try:
    with MyCM():
        raise ExceptionGroup("eg", [ValueError(1), TypeError(2)])
except ExceptionGroup as eg:
    assert len(eg.exceptions) == 2
"""),

            # Comprehension + walrus + closure
            ("interact_comp_walrus_closure", """
def f():
    results = [(y := x, x + y) for x in range(5)]
    return results, y  # y should be accessible here (in 3.12+ due to inlining?)

try:
    result = f()
except NameError:
    pass  # y might not be accessible depending on version
"""),

            # Nested match with type params
            ("interact_nested_match_type", """
class Container[T]:
    def __init__(self, value: T):
        self.value = value

match Container(42):
    case Container(value=int(x)):
        assert x == 42
    case _:
        pass
"""),

            # Multiple decorators + generic
            ("interact_multi_dec_generic", """
def dec1(f): return f
def dec2(f): return f
def dec3(f): return f

@dec1
@dec2
@dec3
def f[T](x: T) -> T:
    return x

assert f(42) == 42
"""),

            # async + match + except*
            ("interact_async_match_except", """
import asyncio

async def categorize_errors():
    try:
        raise ExceptionGroup("errors", [
            ValueError("v1"),
            TypeError("t1"),
            KeyError("k1"),
        ])
    except* ValueError as eg:
        for exc in eg.exceptions:
            match exc:
                case ValueError(args=(msg,)):
                    assert msg == "v1"
    except* (TypeError, KeyError):
        pass

asyncio.run(categorize_errors())
"""),
        ]

        for name, code in cases:
            self.check_subprocess(code, name)

    def run_all(self):
        """Run all aggressive tests."""
        print(f"Aggressive CPython 3.13 Fuzzer")
        print(f"Python: {sys.version}")
        print()

        self.test_parser_edge_cases()
        self.test_compiler_optimizer()
        self.test_runtime_edge_cases()
        self.test_new_313_features()
        self.test_crash_vectors()
        self.test_bytecode_edge_cases()
        self.test_edge_case_interactions()

        print(f"\n{'='*60}")
        print(f"Tests run: {self.tests_run}")
        print(f"Findings: {len(self.findings)}")
        if self.findings:
            print(f"\nFINDINGS:")
            for i, f in enumerate(self.findings, 1):
                print(f"\n--- Finding {i}: {f['name']} ---")
                print(f"Details: {f['details']}")
                if f['code']:
                    print(f"Code:\n{textwrap.indent(f['code'][:300], '  ')}")
        else:
            print("No bugs found.")
        print(f"{'='*60}")

        return self.findings


if __name__ == "__main__":
    fuzzer = AggressiveFuzzer()
    findings = fuzzer.run_all()
    sys.exit(1 if findings else 0)

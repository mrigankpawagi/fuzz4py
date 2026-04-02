"""
Deep/targeted fuzzing for CPython 3.13 internals.
These tests go deeper into CPython-specific behavior that's more likely to trigger bugs.
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
import ctypes
import dis
import copy
import io
import marshal
import importlib
import threading
import time


def test_compile_error_attributes():
    """Test that compile() produces correct SyntaxError attributes in all cases."""
    findings = []

    # Test various error-producing code strings
    error_cases = [
        "x y",
        "def def",
        "class class",
        "1 +",
        "if",
        "for",
        "while",
        "((",
        "))",
        "[[",
        "]]",
        "{{",
        "}}",
        "def f(x, x): pass",
        "lambda x, x: x",
        "f(x for x in range(10), 1)",
        "from import x",
        "@\ndef f(): pass",
        "def f(/):\n pass",
        "nonlocal x",
        "x = (yield)",
        "del ()",
        "x: int = y := 1",
    ]

    for code in error_cases:
        for filename in ["<string>", "<test>", "test.py", ""]:
            for mode in ["exec", "single"]:
                try:
                    compile(code, filename, mode)
                except SyntaxError as e:
                    # Verify attributes are sensible
                    if e.lineno is not None and e.lineno < 0:
                        findings.append(f"Negative lineno {e.lineno} for {code!r} with filename={filename!r}")
                    if e.offset is not None and e.offset < 0:
                        findings.append(f"Negative offset {e.offset} for {code!r} with filename={filename!r}")
                    if e.text is not None and e.lineno is not None:
                        text_lines = e.text.split('\n')
                        # offset should not exceed text length + reasonable margin
                        if e.offset is not None and len(text_lines) > 0:
                            first_line_len = len(text_lines[0])
                            if e.offset > first_line_len + 100 and first_line_len > 0:
                                findings.append(
                                    f"Suspicious offset {e.offset} (text len {first_line_len}) "
                                    f"for {code!r} with filename={filename!r}"
                                )
                except Exception as e:
                    if isinstance(e, SystemError):
                        findings.append(f"SystemError during compile({code!r}, {filename!r}, {mode!r}): {e}")

    return findings


def test_ast_manipulation():
    """Test AST manipulation edge cases."""
    findings = []

    # Create and compile unusual ASTs
    try:
        # AST with no body
        mod = ast.Module(body=[], type_ignores=[])
        compile(mod, "<test>", "exec")
    except Exception as e:
        if isinstance(e, SystemError):
            findings.append(f"SystemError compiling empty Module: {e}")

    # AST with unusual node values
    try:
        # Constant with unusual value
        node = ast.Expression(body=ast.Constant(value=object()))
        ast.fix_missing_locations(node)
        try:
            compile(node, "<test>", "eval")
        except TypeError:
            pass  # Expected
        except SystemError as e:
            findings.append(f"SystemError compiling Constant(object()): {e}")
    except Exception:
        pass

    # AST with mismatched types
    try:
        # FunctionDef with non-string name
        node = ast.Module(
            body=[ast.FunctionDef(
                name=42,  # Should be string
                args=ast.arguments(
                    posonlyargs=[], args=[], vararg=None,
                    kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]
                ),
                body=[ast.Pass()],
                decorator_list=[],
                returns=None,
                type_comment=None,
            )],
            type_ignores=[]
        )
        ast.fix_missing_locations(node)
        try:
            compile(node, "<test>", "exec")
        except TypeError:
            pass  # Expected
        except SystemError as e:
            findings.append(f"SystemError compiling FunctionDef(name=42): {e}")
    except Exception:
        pass

    # AST with negative line numbers
    try:
        node = ast.Module(
            body=[ast.Expr(value=ast.Constant(value=1))],
            type_ignores=[]
        )
        node.body[0].lineno = -1
        node.body[0].col_offset = -1
        node.body[0].end_lineno = -1
        node.body[0].end_col_offset = -1
        node.body[0].value.lineno = -1
        node.body[0].value.col_offset = -1
        node.body[0].value.end_lineno = -1
        node.body[0].value.end_col_offset = -1
        try:
            compile(node, "<test>", "exec")
        except (ValueError, SystemError) as e:
            if isinstance(e, SystemError):
                findings.append(f"SystemError compiling AST with negative lineno: {e}")
    except Exception:
        pass

    # AST with very large line numbers
    try:
        node = ast.Module(
            body=[ast.Expr(value=ast.Constant(value=1))],
            type_ignores=[]
        )
        ast.fix_missing_locations(node)
        node.body[0].lineno = 2**31
        node.body[0].value.lineno = 2**31
        try:
            compile(node, "<test>", "exec")
        except (OverflowError, ValueError, SystemError) as e:
            if isinstance(e, SystemError):
                findings.append(f"SystemError compiling AST with huge lineno: {e}")
    except Exception:
        pass

    # Walk and modify AST
    try:
        code = "x = 1 + 2 * 3"
        tree = ast.parse(code)
        # Replace all numbers with 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                node.value = 0
        compile(tree, "<test>", "exec")
    except SystemError as e:
        findings.append(f"SystemError after AST modification: {e}")

    # Compile with ast.PyCF_ONLY_AST and then compile the result
    try:
        tree = compile("x = 1 + 2", "<test>", "exec", flags=ast.PyCF_ONLY_AST)
        compile(tree, "<test>", "exec")
    except SystemError as e:
        findings.append(f"SystemError with PyCF_ONLY_AST round-trip: {e}")

    return findings


def test_code_object_manipulation():
    """Test code object edge cases."""
    findings = []

    # Replace code with mismatched parameters
    try:
        def f(x, y):
            return x + y

        code = f.__code__

        # Replace with different argument count but same code
        try:
            new_code = code.replace(co_argcount=0)
            f.__code__ = new_code
            try:
                f(1, 2)
            except TypeError:
                pass
        except (ValueError, SystemError) as e:
            if isinstance(e, SystemError):
                findings.append(f"SystemError replacing co_argcount: {e}")

        # Restore
        f.__code__ = code
    except Exception:
        pass

    # Test marshal round-trip of code objects
    try:
        code = compile("x = 1 + 2", "<test>", "exec")
        marshaled = marshal.dumps(code)
        restored = marshal.loads(marshaled)
        ns = {}
        exec(restored, ns)
        assert ns["x"] == 3
    except SystemError as e:
        findings.append(f"SystemError in code marshal round-trip: {e}")

    # Test deeply nested code objects
    try:
        # Create deeply nested functions
        code = "def f0():\n"
        for i in range(1, 50):
            code += "  " * i + f"def f{i}():\n"
        code += "  " * 50 + "return 42\n"
        for i in range(49, -1, -1):
            code += "  " * (i + 1) + f"return f{i+1}()\n" if i < 49 else ""

        compile(code, "<test>", "exec")
    except (RecursionError, SystemError) as e:
        if isinstance(e, SystemError):
            findings.append(f"SystemError compiling deeply nested functions: {e}")

    # Test exec with restricted globals
    try:
        code = compile("import os", "<test>", "exec")
        ns = {"__builtins__": {"__import__": lambda *a, **k: None}}
        try:
            exec(code, ns)
        except (ImportError, TypeError):
            pass
        except SystemError as e:
            findings.append(f"SystemError exec with restricted builtins: {e}")
    except Exception:
        pass

    return findings


def test_gc_edge_cases():
    """Test garbage collector edge cases."""
    findings = []

    # Test GC with weakref callbacks creating new cycles
    try:
        collected = []

        class CycleCreator:
            def __init__(self):
                self.ref = None

        def callback(ref):
            # Create a new cycle during GC callback
            a = CycleCreator()
            b = CycleCreator()
            a.ref = b
            b.ref = a
            collected.append((a, b))

        for _ in range(100):
            c = CycleCreator()
            weakref.ref(c, callback)
            del c

        gc.collect()
    except SystemError as e:
        findings.append(f"SystemError in GC weakref callback: {e}")
    except Exception:
        pass

    # Test GC with __del__ that accesses dying objects
    try:
        class Accessor:
            partner = None
            def __del__(self):
                try:
                    if self.partner is not None:
                        _ = self.partner.__class__
                except (ReferenceError, AttributeError):
                    pass

        for _ in range(100):
            a = Accessor()
            b = Accessor()
            a.partner = weakref.ref(b)
            b.partner = weakref.ref(a)
            del a, b

        gc.collect()
    except SystemError as e:
        findings.append(f"SystemError in GC __del__ accessing dying objects: {e}")
    except Exception:
        pass

    # Test gc.get_objects() during GC
    try:
        class GCInspector:
            def __del__(self):
                try:
                    # Inspect GC state during finalization
                    gc.get_objects()
                except Exception:
                    pass

        for _ in range(50):
            g = GCInspector()
            del g

        gc.collect()
    except SystemError as e:
        findings.append(f"SystemError calling gc.get_objects() during GC: {e}")
    except Exception:
        pass

    return findings


def test_descriptor_edge_cases():
    """Test descriptor protocol edge cases."""
    findings = []

    # Data descriptor with __set__ raising
    try:
        class BadDescriptor:
            def __get__(self, obj, objtype=None):
                raise SystemError("shouldn't reach here")
            def __set__(self, obj, value):
                raise SystemError("shouldn't reach here")
            def __delete__(self, obj):
                raise SystemError("shouldn't reach here")

        class C:
            x = BadDescriptor()

        c = C()
        try:
            c.x
        except SystemError:
            pass  # This is expected since our descriptor raises it
        try:
            c.x = 1
        except SystemError:
            pass
        try:
            del c.x
        except SystemError:
            pass
    except Exception:
        pass

    # __getattribute__ override
    try:
        class Tricky:
            def __getattribute__(self, name):
                if name == "__class__":
                    return type(self)
                raise AttributeError(name)

        t = Tricky()
        try:
            repr(t)
        except (AttributeError, RecursionError):
            pass
    except SystemError as e:
        findings.append(f"SystemError with __getattribute__ override: {e}")

    # Descriptor that returns different type
    try:
        class TypeChangingDesc:
            def __get__(self, obj, objtype=None):
                return 42  # Return int instead of descriptor

        class C:
            method = TypeChangingDesc()

        c = C()
        assert c.method == 42
    except SystemError as e:
        findings.append(f"SystemError with type-changing descriptor: {e}")

    # __set_name__ that modifies the class
    try:
        class SelfModifying:
            def __set_name__(self, owner, name):
                # Add more attributes during class creation
                setattr(owner, name + "_copy", self)

        class C:
            x = SelfModifying()
    except SystemError as e:
        findings.append(f"SystemError with self-modifying __set_name__: {e}")

    return findings


def test_frame_manipulation():
    """Test frame object edge cases."""
    findings = []

    # Access frame locals during trace
    try:
        results = []

        def tracer(frame, event, arg):
            if event == 'call':
                # Modify locals during trace
                frame.f_locals['injected'] = True
            return tracer

        old_trace = sys.gettrace()
        sys.settrace(tracer)
        try:
            def test_func():
                x = 1
                return x
            test_func()
        finally:
            sys.settrace(old_trace)
    except SystemError as e:
        findings.append(f"SystemError during frame local modification in trace: {e}")
    except Exception:
        pass

    # Trace function that throws
    try:
        def bad_tracer(frame, event, arg):
            raise ValueError("tracer error")

        old_trace = sys.gettrace()
        sys.settrace(bad_tracer)
        try:
            x = 1 + 2  # This should trigger the tracer
        except ValueError:
            pass
        finally:
            sys.settrace(old_trace)
    except SystemError as e:
        findings.append(f"SystemError with throwing tracer: {e}")
    except Exception:
        pass

    # Generator frame inspection
    try:
        def gen():
            yield 1
            yield 2

        g = gen()
        frame = g.gi_frame
        assert frame is not None
        next(g)
        frame = g.gi_frame
        assert frame is not None
        next(g)
        try:
            next(g)
        except StopIteration:
            pass
        assert g.gi_frame is None
    except SystemError as e:
        findings.append(f"SystemError during generator frame inspection: {e}")

    return findings


def test_import_edge_cases():
    """Test import system edge cases."""
    findings = []

    # Import with unusual module names
    try:
        try:
            __import__("")
        except (ImportError, ValueError, ModuleNotFoundError):
            pass
        except SystemError as e:
            findings.append(f"SystemError importing empty string: {e}")
    except Exception:
        pass

    # Import with dots
    try:
        try:
            __import__(".")
        except (ImportError, ValueError, ModuleNotFoundError):
            pass
        except SystemError as e:
            findings.append(f"SystemError importing '.': {e}")
    except Exception:
        pass

    # Import with null byte
    try:
        try:
            __import__("test\x00module")
        except (ImportError, ValueError, ModuleNotFoundError):
            pass
        except SystemError as e:
            findings.append(f"SystemError importing null byte name: {e}")
    except Exception:
        pass

    # Circular import simulation
    try:
        code = textwrap.dedent("""
        import sys
        import types
        mod = types.ModuleType("circular_test")
        mod.__file__ = "<test>"
        sys.modules["circular_test"] = mod
        exec("import circular_test", mod.__dict__)
        del sys.modules["circular_test"]
        """)
        exec(code)
    except (ImportError, RecursionError):
        pass
    except SystemError as e:
        findings.append(f"SystemError in circular import: {e}")

    return findings


def test_type_edge_cases():
    """Test type system edge cases."""
    findings = []

    # Dynamic type creation with type()
    try:
        # Create a type with __slots__ that conflicts with dict
        T = type("T", (object,), {"__slots__": ("__dict__",)})
        t = T()
        t.x = 1
    except (TypeError, SystemError) as e:
        if isinstance(e, SystemError):
            findings.append(f"SystemError creating type with __dict__ slot: {e}")

    # Type with metaclass conflict
    try:
        class M1(type): pass
        class M2(type): pass
        class A(metaclass=M1): pass
        class B(metaclass=M2): pass
        try:
            class C(A, B): pass
        except TypeError:
            pass  # Expected
        except SystemError as e:
            findings.append(f"SystemError with metaclass conflict: {e}")
    except Exception:
        pass

    # __class__ assignment
    try:
        class A:
            x = 1
        class B:
            y = 2
        a = A()
        try:
            a.__class__ = B
            assert isinstance(a, B)
        except TypeError:
            pass  # May not be allowed
        except SystemError as e:
            findings.append(f"SystemError with __class__ assignment: {e}")
    except Exception:
        pass

    # Dynamic type with unusual __bases__
    try:
        class Base: pass
        class Child(Base): pass
        try:
            Child.__bases__ = (object,)  # Remove Base from bases
        except TypeError:
            pass
        except SystemError as e:
            findings.append(f"SystemError modifying __bases__: {e}")
    except Exception:
        pass

    # Type with __new__ returning wrong type
    try:
        class Tricky:
            def __new__(cls):
                return 42  # Return int instead of Tricky instance

        t = Tricky()
        assert t == 42
    except SystemError as e:
        findings.append(f"SystemError with __new__ returning wrong type: {e}")

    # __subclasshook__ edge cases
    try:
        import abc

        class MyABC(abc.ABC):
            @classmethod
            def __subclasshook__(cls, subclass):
                return True  # Everything is a subclass

        assert issubclass(int, MyABC)
        assert isinstance(42, MyABC)
    except SystemError as e:
        findings.append(f"SystemError with __subclasshook__: {e}")

    return findings


def test_string_interning():
    """Test string interning edge cases."""
    findings = []

    try:
        # Intern strings of various types
        import sys
        s1 = sys.intern("hello")
        s2 = sys.intern("hello")
        assert s1 is s2

        # Intern long strings
        long_s = "x" * 10000
        s3 = sys.intern(long_s)
        s4 = sys.intern(long_s)
        assert s3 is s4

        # Intern empty string
        s5 = sys.intern("")
        s6 = sys.intern("")
        assert s5 is s6

        # Intern string with null bytes
        try:
            s7 = sys.intern("hello\x00world")
        except Exception:
            pass

    except SystemError as e:
        findings.append(f"SystemError during string interning: {e}")

    return findings


def test_threading_edge_cases():
    """Test threading edge cases (relevant to 3.13's free-threading work)."""
    findings = []

    # Concurrent dict modification
    try:
        import threading
        d = {}
        errors = []

        def writer():
            for i in range(1000):
                d[i] = i
                if i % 3 == 0:
                    try:
                        del d[i]
                    except KeyError:
                        pass

        def reader():
            for _ in range(1000):
                try:
                    list(d.items())
                    list(d.keys())
                    list(d.values())
                    len(d)
                except RuntimeError:
                    pass  # dictionary changed size during iteration

        threads = [threading.Thread(target=writer) for _ in range(4)]
        threads += [threading.Thread(target=reader) for _ in range(4)]

        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=10)

    except SystemError as e:
        findings.append(f"SystemError in concurrent dict access: {e}")
    except Exception:
        pass

    # Concurrent list modification
    try:
        lst = []
        def list_writer():
            for i in range(1000):
                lst.append(i)
                if len(lst) > 10:
                    try:
                        lst.pop(0)
                    except IndexError:
                        pass

        threads = [threading.Thread(target=list_writer) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=10)
    except SystemError as e:
        findings.append(f"SystemError in concurrent list access: {e}")
    except Exception:
        pass

    return findings


def test_special_method_interactions():
    """Test interactions between special methods."""
    findings = []

    # __hash__ and __eq__ inconsistency
    try:
        class BadHash:
            def __init__(self, val):
                self.val = val
            def __hash__(self):
                return 1  # All objects hash to 1
            def __eq__(self, other):
                return isinstance(other, BadHash) and self.val == other.val

        d = {}
        for i in range(100):
            d[BadHash(i)] = i
        assert len(d) == 100
    except SystemError as e:
        findings.append(f"SystemError with hash collision stress: {e}")

    # __format__ edge cases
    try:
        class BadFormat:
            def __format__(self, spec):
                if spec:
                    raise ValueError("bad spec")
                return "formatted"

        f"{BadFormat()}"
        try:
            f"{BadFormat():x}"
        except ValueError:
            pass
    except SystemError as e:
        findings.append(f"SystemError with __format__: {e}")

    # __contains__ that modifies the container
    try:
        class MutatingContainer:
            def __init__(self):
                self.items = list(range(10))
            def __contains__(self, item):
                self.items.append(item)
                return item in self.items
            def __iter__(self):
                return iter(self.items)

        c = MutatingContainer()
        5 in c
        list(c)
    except SystemError as e:
        findings.append(f"SystemError with mutating __contains__: {e}")

    # __getitem__ that returns self
    try:
        class SelfReturning:
            def __getitem__(self, key):
                return self
            def __len__(self):
                return 1

        s = SelfReturning()
        assert s[0] is s
        assert s[0][0][0] is s
    except SystemError as e:
        findings.append(f"SystemError with self-returning __getitem__: {e}")

    return findings


def test_ctypes_edge_cases():
    """Test ctypes edge cases."""
    findings = []

    try:
        import ctypes

        # Create a buffer and manipulate it
        buf = ctypes.create_string_buffer(100)
        buf.value = b"hello"
        assert buf.value == b"hello"

        # Array edge cases
        IntArray = ctypes.c_int * 10
        arr = IntArray()
        for i in range(10):
            arr[i] = i
        assert list(arr) == list(range(10))

        # Struct with packed fields
        class PackedStruct(ctypes.Structure):
            _pack_ = 1
            _fields_ = [
                ("a", ctypes.c_uint8),
                ("b", ctypes.c_uint32),
                ("c", ctypes.c_uint8),
            ]

        s = PackedStruct()
        s.a = 1
        s.b = 2
        s.c = 3
        assert ctypes.sizeof(s) == 6  # packed

    except SystemError as e:
        findings.append(f"SystemError with ctypes: {e}")
    except Exception:
        pass

    return findings


def test_copy_edge_cases():
    """Test copy/deepcopy edge cases."""
    findings = []

    # Deepcopy of recursive structure
    try:
        a = [1, 2, 3]
        a.append(a)
        b = copy.deepcopy(a)
        assert b[3] is b
    except SystemError as e:
        findings.append(f"SystemError deepcopy recursive list: {e}")

    # Deepcopy of class with __reduce__
    try:
        class CustomReduce:
            def __init__(self, val):
                self.val = val
            def __reduce__(self):
                return (CustomReduce, (self.val,))
            def __eq__(self, other):
                return isinstance(other, CustomReduce) and self.val == other.val

        c = CustomReduce(42)
        c2 = copy.deepcopy(c)
        assert c == c2
    except SystemError as e:
        findings.append(f"SystemError deepcopy with __reduce__: {e}")

    # Copy of frozen set containing unusual items
    try:
        fs = frozenset([1, "2", (3, 4), frozenset([5, 6])])
        fs2 = copy.copy(fs)
        assert fs == fs2
    except SystemError as e:
        findings.append(f"SystemError copying frozenset: {e}")

    return findings


def test_marshal_edge_cases():
    """Test marshal module edge cases."""
    findings = []

    # Marshal various types
    try:
        test_values = [
            None, True, False,
            0, 1, -1, 2**30, -(2**30), 2**31, -(2**31),
            0.0, 1.0, -1.0, float('inf'), float('-inf'),
            # float('nan'),  # NaN != NaN breaks assertion
            "", "hello", "x" * 10000,
            b"", b"hello", b"x" * 10000,
            (), (1, 2, 3), (1, (2, (3,))),
            [], [1, 2, 3],
            {}, {1: 2, 3: 4},
            set(), {1, 2, 3},
            frozenset(), frozenset([1, 2, 3]),
        ]

        for val in test_values:
            marshaled = marshal.dumps(val)
            restored = marshal.loads(marshaled)
            assert type(val) == type(restored), f"Type mismatch: {type(val)} != {type(restored)}"
            if val == val:  # Skip NaN
                assert val == restored, f"Value mismatch: {val!r} != {restored!r}"
    except SystemError as e:
        findings.append(f"SystemError in marshal round-trip: {e}")

    # Marshal code objects
    try:
        code = compile("x = 1 + 2", "<test>", "exec")
        marshaled = marshal.dumps(code)
        restored = marshal.loads(marshaled)
        ns = {}
        exec(restored, ns)
        assert ns["x"] == 3
    except SystemError as e:
        findings.append(f"SystemError marshaling code object: {e}")

    return findings


def test_disassembly_edge_cases():
    """Test dis module edge cases."""
    findings = []

    try:
        # Disassemble various constructs
        codes = [
            "x = 1",
            "def f(x): return x + 1",
            "class C: pass",
            "[x for x in range(10)]",
            "lambda x: x + 1",
            "async def f(): await g()",
            "def f(): yield from range(10)",
            "match x:\n case 1: pass\n case _: pass",
            "type Alias = int",
        ]

        for code in codes:
            try:
                compiled = compile(code, "<test>", "exec")
                output = io.StringIO()
                dis.dis(compiled, file=output)
                # Also test dis.get_instructions
                list(dis.get_instructions(compiled))
            except SyntaxError:
                pass
            except SystemError as e:
                findings.append(f"SystemError disassembling {code!r}: {e}")
    except Exception:
        pass

    return findings


def run_all_deep_tests():
    """Run all deep/targeted tests and collect findings."""
    all_findings = []

    test_functions = [
        ("compile_error_attributes", test_compile_error_attributes),
        ("ast_manipulation", test_ast_manipulation),
        ("code_object_manipulation", test_code_object_manipulation),
        ("gc_edge_cases", test_gc_edge_cases),
        ("descriptor_edge_cases", test_descriptor_edge_cases),
        ("frame_manipulation", test_frame_manipulation),
        ("import_edge_cases", test_import_edge_cases),
        ("type_edge_cases", test_type_edge_cases),
        ("string_interning", test_string_interning),
        ("threading_edge_cases", test_threading_edge_cases),
        ("special_method_interactions", test_special_method_interactions),
        ("ctypes_edge_cases", test_ctypes_edge_cases),
        ("copy_edge_cases", test_copy_edge_cases),
        ("marshal_edge_cases", test_marshal_edge_cases),
        ("disassembly_edge_cases", test_disassembly_edge_cases),
    ]

    for name, func in test_functions:
        print(f"  Running {name}...", end=" ", flush=True)
        try:
            findings = func()
            if findings:
                print(f"FOUND {len(findings)} issue(s)!")
                for f in findings:
                    print(f"    - {f}")
                all_findings.extend([(name, f) for f in findings])
            else:
                print("OK")
        except Exception as e:
            print(f"ERROR: {e}")
            if isinstance(e, SystemError):
                all_findings.append((name, f"Unhandled SystemError: {e}"))

    return all_findings


if __name__ == "__main__":
    print(f"CPython 3.13 Deep Fuzzer")
    print(f"Python: {sys.version}")
    print(f"Executable: {sys.executable}")
    print()

    print("Running deep/targeted tests...")
    findings = run_all_deep_tests()

    print(f"\n{'='*60}")
    if findings:
        print(f"FOUND {len(findings)} POTENTIAL ISSUE(S)!")
        for name, finding in findings:
            print(f"\n  [{name}] {finding}")
    else:
        print("No issues found in deep tests.")
    print(f"{'='*60}")

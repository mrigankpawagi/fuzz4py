"""
Code generators for CPython 3.13 fuzzing.
Each generator yields (name, source_code) tuples.
"""

import random
import string
import itertools
import sys


def _rand_ident(min_len=1, max_len=10):
    """Random valid Python identifier."""
    first = random.choice(string.ascii_letters + '_')
    rest = ''.join(random.choices(string.ascii_letters + string.digits + '_', k=random.randint(min_len - 1, max_len - 1)))
    return first + rest


def _rand_unicode_ident():
    """Random Python identifier using unicode characters."""
    # Valid Python identifier unicode ranges
    ranges = [
        (0x00C0, 0x00D6), (0x00D8, 0x00F6), (0x00F8, 0x00FF),
        (0x0100, 0x017F),  # Latin Extended-A
        (0x0370, 0x03FF),  # Greek
        (0x0400, 0x04FF),  # Cyrillic
        (0x4E00, 0x4E50),  # CJK (small range)
        (0x1D400, 0x1D419),  # Mathematical bold
    ]
    r = random.choice(ranges)
    first = chr(random.randint(r[0], r[1]))
    length = random.randint(1, 5)
    rest = ''
    for _ in range(length):
        r2 = random.choice(ranges)
        rest += chr(random.randint(r2[0], r2[1]))
    return first + rest


def _rand_int():
    """Random integer literal."""
    choices = [
        str(random.randint(-1000, 1000)),
        str(random.randint(0, 2**63)),
        '0x' + hex(random.randint(0, 2**32))[2:],
        '0o' + oct(random.randint(0, 2**16))[2:],
        '0b' + bin(random.randint(0, 2**16))[2:],
        str(10 ** random.randint(50, 300)),
        '0',
        '-0',
        str(2**31 - 1),
        str(2**31),
        str(2**63 - 1),
        str(2**63),
        str(-(2**63)),
    ]
    return random.choice(choices)


def _rand_string():
    """Random string literal."""
    quote = random.choice(["'", '"', "'''", '"""'])
    content_choices = [
        '',
        'hello',
        '\\n\\t\\r\\\\',
        '\\x00\\x01\\xff',
        '\\u0000\\u1234\\uffff',
        '\\U00010000\\U0001f600',
        '\\N{SNOWMAN}',
        '\\ ',
        '\\' + str(random.randint(0, 7)) * 3,
        'a' * random.randint(100, 1000),
        ''.join(chr(random.randint(32, 126)) for _ in range(random.randint(1, 50))),
    ]
    content = random.choice(content_choices)
    prefix = random.choice(['', 'b', 'r', 'rb', 'br', 'u', 'f', 'rf', 'fr', 'F', 'R', 'B', 'U'])
    if prefix.lower().startswith(('b', 'rb', 'br')):
        content = content.replace('\\u', 'u').replace('\\U', 'U').replace('\\N', 'N')
    return f"{prefix}{quote}{content}{quote}"


# ========== Generator: compile/ast edge cases ==========

def gen_compile_edge_cases():
    """Generate edge cases for compile() and ast.parse()."""
    cases = []

    # Empty and whitespace
    for src in ['', ' ', '\n', '\t', '\r\n', '  \n  \n  ', '\t\t\n']:
        cases.append(('compile_empty', src))

    # Null bytes
    cases.append(('compile_null_1', 'x = 1\x00'))
    cases.append(('compile_null_2', '\x00x = 1'))
    cases.append(('compile_null_3', 'x = "\x00"'))

    # Very long lines
    cases.append(('compile_long_line', 'x = ' + '+'.join(['1'] * 5000)))
    cases.append(('compile_long_name', 'x' * 10000 + ' = 1'))

    # Deeply nested expressions
    for depth in [50, 100, 200, 500]:
        cases.append((f'compile_nested_parens_{depth}', '(' * depth + '1' + ')' * depth))
        cases.append((f'compile_nested_lists_{depth}', '[' * depth + '1' + ']' * depth))
        cases.append((f'compile_nested_tuples_{depth}', '(' * depth + '1,' + ')' * depth))
        cases.append((f'compile_nested_dicts_{depth}', '{' * depth + '1:2' + '}' * depth))

    # Deeply nested if/else
    for depth in [20, 50, 100]:
        code = ''
        for i in range(depth):
            code += '  ' * i + f'if True:\n'
        code += '  ' * depth + 'pass\n'
        cases.append((f'compile_nested_if_{depth}', code))

    # Deeply nested try/except
    for depth in [20, 50]:
        code = ''
        for i in range(depth):
            code += '  ' * i + 'try:\n'
        code += '  ' * depth + 'pass\n'
        for i in range(depth - 1, -1, -1):
            code += '  ' * i + 'except:\n' + '  ' * (i + 1) + 'pass\n'
        cases.append((f'compile_nested_try_{depth}', code))

    # Many arguments
    for n in [100, 255, 256, 300]:
        args = ', '.join(f'a{i}' for i in range(n))
        cases.append((f'compile_many_args_{n}', f'def f({args}): pass'))
        cases.append((f'compile_many_kwargs_{n}', f'def f({", ".join(f"a{i}=0" for i in range(n))}): pass'))

    # Many decorators
    for n in [50, 100]:
        decs = '\n'.join(f'@dec{i}' for i in range(n))
        cases.append((f'compile_many_decorators_{n}', f'{decs}\ndef f(): pass'))

    # Complex decorators
    cases.append(('compile_complex_dec_1', '@(lambda f: f)\ndef g(): pass'))
    cases.append(('compile_complex_dec_2', '@a.b.c.d.e\ndef g(): pass'))
    cases.append(('compile_complex_dec_3', '@(x := lambda f: f)\ndef g(): pass'))
    cases.append(('compile_complex_dec_4', '@a[0]\ndef g(): pass'))
    cases.append(('compile_complex_dec_5', '@a()()()\ndef g(): pass'))

    # Encoding edge cases
    cases.append(('compile_encoding_1', '# -*- coding: utf-8 -*-\nx = 1'))
    cases.append(('compile_encoding_2', '# -*- coding: ascii -*-\nx = 1'))
    cases.append(('compile_encoding_3', '# -*- coding: latin-1 -*-\nx = 1'))
    cases.append(('compile_encoding_4', '# vim: set fileencoding=utf-8 :\nx = 1'))

    # Star expressions
    cases.append(('compile_star_1', 'a, *b, c = [1, 2, 3, 4]'))
    cases.append(('compile_star_2', '(*a,) = [1, 2, 3]'))
    cases.append(('compile_star_3', '[*a] = [1, 2, 3]'))

    # Walrus operator edge cases
    cases.append(('compile_walrus_1', '(x := 1)'))
    cases.append(('compile_walrus_2', 'if (x := 1): pass'))
    cases.append(('compile_walrus_3', '[y := x for x in range(5)]'))
    cases.append(('compile_walrus_4', '(y := x for x in range(5))'))

    # Multiple assignments
    cases.append(('compile_multi_assign', 'a = b = c = d = e = f = g = 1'))

    # Augmented assignments with complex targets
    cases.append(('compile_aug_assign', 'a, = [1]\n'))

    # Yield edge cases
    cases.append(('compile_yield_1', 'def f(): x = yield'))
    cases.append(('compile_yield_2', 'def f(): x = yield 1'))
    cases.append(('compile_yield_3', 'def f(): yield from []'))
    cases.append(('compile_yield_4', 'def f(): x = yield from []'))

    # Async edge cases
    cases.append(('compile_async_1', 'async def f(): await g()'))
    cases.append(('compile_async_2', 'async def f():\n async for x in y: pass'))
    cases.append(('compile_async_3', 'async def f():\n async with x: pass'))
    cases.append(('compile_async_4', 'async def f(): return [x async for x in y]'))

    # Lambda edge cases
    cases.append(('compile_lambda_1', 'lambda: None'))
    cases.append(('compile_lambda_2', 'lambda *a, **k: a'))
    cases.append(('compile_lambda_3', 'lambda x=lambda y: y: x'))
    cases.append(('compile_lambda_4', 'lambda x, /, y, *, z: x'))

    # Multiple statements on one line
    cases.append(('compile_multiline_1', 'a = 1; b = 2; c = 3'))
    cases.append(('compile_multiline_2', 'if True: pass; pass'))
    cases.append(('compile_multiline_3', 'if True: pass\nelse: pass'))

    # Unusual but valid syntax
    cases.append(('compile_unusual_1', 'x = ...'))
    cases.append(('compile_unusual_2', 'x = NotImplemented'))
    cases.append(('compile_unusual_3', '...'))
    cases.append(('compile_unusual_4', 'pass;pass;pass'))
    cases.append(('compile_unusual_5', 'x = (1,2,3,)'))
    cases.append(('compile_unusual_6', 'x = {**{}, **{}}'))

    # Compile modes
    for mode in ['exec', 'eval', 'single']:
        cases.append((f'compile_mode_{mode}_1', 'x = 1' if mode != 'eval' else '1+1'))

    # compile() with different flags
    # These are tested differently in the harness

    # Comments edge cases
    cases.append(('compile_comment_1', '# ' + 'x' * 10000))
    cases.append(('compile_comment_2', '#\n' * 1000))
    cases.append(('compile_comment_3', '# \xff\n' if sys.platform != 'win32' else '# comment\n'))

    # Line continuations
    cases.append(('compile_continuation_1', 'x = \\\n1'))
    cases.append(('compile_continuation_2', 'x = \\\n\\\n\\\n1'))
    cases.append(('compile_continuation_3', 'x = 1 + \\\n2 + \\\n3'))

    # Semicolons
    cases.append(('compile_semicolons', ';'.join(['pass'] * 100)))

    return cases


# ========== Generator: f-string edge cases ==========

def gen_fstring_cases():
    """Generate f-string edge cases (parser was rewritten in 3.12)."""
    cases = []

    # Basic f-string edge cases
    cases.append(('fstring_empty', "f''"))
    cases.append(('fstring_just_expr', "f'{1}'"))
    cases.append(('fstring_nested_quotes', 'f"{"hello"}"'))
    cases.append(('fstring_nested_quotes_2', "f'{\"hello\"}'"))

    # Nested f-strings (new in 3.12 - unlimited nesting)
    cases.append(('fstring_nested_1', "f'{f\"{1}\"}'"))
    cases.append(('fstring_nested_2', "f'{f\"{f\\'{1}\\'}\"}'" ))
    cases.append(('fstring_nested_3', 'f"{ f"{ f"{ 1 }" }" }"'))

    # Deeply nested f-strings
    for depth in [5, 10, 15, 20]:
        s = '1'
        for _ in range(depth):
            s = f'f"{{{s}}}"'
        cases.append((f'fstring_deep_nest_{depth}', s))

    # f-strings with various expressions
    cases.append(('fstring_walrus', "f'{(x := 42)}'"))
    cases.append(('fstring_ternary', "f'{1 if True else 2}'"))
    cases.append(('fstring_lambda', "f'{(lambda: 1)()}'"))
    cases.append(('fstring_dict', "f'{ {1: 2} }'"))
    cases.append(('fstring_set', "f'{ {1, 2, 3} }'"))
    cases.append(('fstring_comprehension', "f'{[x for x in range(10)]}'"))
    cases.append(('fstring_dict_comp', "f'{ {k: v for k, v in [(1,2)]} }'"))
    cases.append(('fstring_genexpr', "f'{list(x for x in range(5))}'"))
    cases.append(('fstring_slice', "f'{[1,2,3][1:]}'"))
    cases.append(('fstring_star', "f'{*[1,2],}'"))
    cases.append(('fstring_star_2', "f'{[*[1,2]]}'"))

    # Format specs
    cases.append(('fstring_format_1', "f'{42:.2f}'"))
    cases.append(('fstring_format_2', "f'{42:>10}'"))
    cases.append(('fstring_format_3', "f'{42:0{10}d}'"))
    cases.append(('fstring_format_4', 'f\'{42:{"d"}}\''))
    cases.append(('fstring_format_5', 'f\'{42:{f"{3}"}d}\''))

    # Conversion flags
    cases.append(('fstring_conv_1', "f'{42!r}'"))
    cases.append(('fstring_conv_2', "f'{42!s}'"))
    cases.append(('fstring_conv_3', "f'{42!a}'"))
    cases.append(('fstring_conv_4', "f'{42!r:.10}'"))

    # Multiline f-strings
    cases.append(('fstring_multiline_1', 'f"""{\n1\n}"""'))
    cases.append(('fstring_multiline_2', 'f"""{# comment\n1\n}"""'))

    # f-strings with backslashes (allowed in 3.12+)
    cases.append(('fstring_backslash_1', "f'{\"\\n\"}'"))
    cases.append(('fstring_backslash_2', "f'{chr(10)}'"))

    # Empty expression
    # cases.append(('fstring_empty_expr', "f'{}'"))  # This is a syntax error

    # f-string with = (debug)
    cases.append(('fstring_debug_1', "x = 42; f'{x=}'"))
    cases.append(('fstring_debug_2', "x = 42; f'{x = }'"))
    cases.append(('fstring_debug_3', "x = 42; f'{x=!r}'"))
    cases.append(('fstring_debug_4', "x = 42; f'{x=:.2f}'"))

    # f-string concatenation
    cases.append(('fstring_concat_1', "f'a' f'b'"))
    cases.append(('fstring_concat_2', "f'a' 'b'"))
    cases.append(('fstring_concat_3', "'a' f'b'"))
    cases.append(('fstring_concat_4', "f'a' f'b' f'c'"))

    # Very long f-strings
    cases.append(('fstring_long_1', "f'{'+''.join('x' for _ in range(1000))}'"))
    cases.append(('fstring_long_expr', "f'{" + "+".join(["1"] * 500) + "}'"))

    return cases


# ========== Generator: pattern matching edge cases ==========

def gen_pattern_matching_cases():
    """Generate pattern matching (PEP 634) edge cases."""
    cases = []

    # Basic patterns
    cases.append(('match_literal', 'match 42:\n case 42: pass\n case _: pass'))
    cases.append(('match_none', 'match None:\n case None: pass'))
    cases.append(('match_bool', 'match True:\n case True: pass\n case False: pass'))

    # Capture patterns
    cases.append(('match_capture', 'match 42:\n case x: pass'))

    # Sequence patterns
    cases.append(('match_seq_1', 'match [1,2,3]:\n case [a, b, c]: pass'))
    cases.append(('match_seq_star', 'match [1,2,3]:\n case [a, *b, c]: pass'))
    cases.append(('match_seq_nested', 'match [[1],[2]]:\n case [[a], [b]]: pass'))
    cases.append(('match_seq_empty', 'match []:\n case []: pass'))

    # Mapping patterns
    cases.append(('match_map_1', 'match {"a": 1}:\n case {"a": x}: pass'))
    cases.append(('match_map_rest', 'match {"a": 1, "b": 2}:\n case {"a": x, **rest}: pass'))
    cases.append(('match_map_nested', 'match {"a": {"b": 1}}:\n case {"a": {"b": x}}: pass'))

    # Class patterns
    cases.append(('match_class_1', 'match 42:\n case int(x): pass'))
    cases.append(('match_class_2', 'match "hi":\n case str() as s: pass'))
    cases.append(('match_class_kw', '''
class C:
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
match C(1, 2):
    case C(x=a, y=b): pass
'''))

    # OR patterns
    cases.append(('match_or', 'match 42:\n case 1 | 2 | 3 | 42: pass'))
    cases.append(('match_or_capture', 'match 42:\n case (1 | 2 | 3) as x: pass'))

    # AS patterns
    cases.append(('match_as', 'match [1, 2]:\n case [1, x] as y: pass'))

    # Guard
    cases.append(('match_guard', 'match 42:\n case x if x > 0: pass'))
    cases.append(('match_guard_complex', 'match 42:\n case x if (y := x) > 0: pass'))

    # Nested match
    cases.append(('match_nested', '''
match (1, 2):
    case (a, b):
        match a:
            case 1: pass
            case _: pass
'''))

    # Many cases
    many_cases = '\n'.join(f' case {i}: pass' for i in range(200))
    cases.append(('match_many_cases', f'match 42:\n{many_cases}\n case _: pass'))

    # Complex nested patterns
    cases.append(('match_complex_1', '''
match {"users": [{"name": "Alice", "age": 30}]}:
    case {"users": [{"name": str(name), "age": int(age)}, *rest]}:
        pass
    case _:
        pass
'''))

    # Pattern matching with classes that have __match_args__
    cases.append(('match_match_args', '''
class Point:
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

match Point(1, 2):
    case Point(0, 0): pass
    case Point(x, 0): pass
    case Point(0, y): pass
    case Point(x, y) if x == y: pass
    case Point(x, y): pass
'''))

    # Match with star in weird positions
    cases.append(('match_star_weird', 'match [1,2,3,4,5]:\n case [*x]: pass'))
    cases.append(('match_star_only', 'match [1]:\n case [*_]: pass'))

    # Match with complex keys in mapping
    cases.append(('match_complex_key', 'match {True: 1}:\n case {True: x}: pass'))
    cases.append(('match_complex_key_2', 'match {0: "a", 1: "b"}:\n case {0: x, 1: y}: pass'))
    cases.append(('match_none_key', 'match {None: 1}:\n case {None: x}: pass'))

    # Wildcard
    cases.append(('match_wildcard', 'match 42:\n case _: pass'))
    cases.append(('match_wildcard_nested', 'match [1, 2]:\n case [_, _]: pass'))

    return cases


# ========== Generator: type parameter edge cases (PEP 695) ==========

def gen_type_param_cases():
    """Generate type parameter syntax edge cases (PEP 695, new in 3.12)."""
    cases = []

    # Basic type aliases
    cases.append(('type_alias_1', 'type Alias = int'))
    cases.append(('type_alias_2', 'type Alias = int | str'))
    cases.append(('type_alias_3', 'type Alias = list[int]'))

    # Generic type aliases
    cases.append(('type_alias_generic', 'type Alias[T] = list[T]'))
    cases.append(('type_alias_multi', 'type Alias[T, U] = dict[T, U]'))
    cases.append(('type_alias_bound', 'type Alias[T: int] = list[T]'))
    cases.append(('type_alias_constraint', 'type Alias[T: (int, str)] = list[T]'))

    # Generic classes
    cases.append(('generic_class_1', 'class C[T]: pass'))
    cases.append(('generic_class_2', 'class C[T, U, V]: pass'))
    cases.append(('generic_class_bound', 'class C[T: int]: pass'))
    cases.append(('generic_class_constraint', 'class C[T: (int, str)]: pass'))

    # Generic functions
    cases.append(('generic_func_1', 'def f[T](x: T) -> T: return x'))
    cases.append(('generic_func_2', 'def f[T, U](x: T, y: U) -> T | U: return x'))

    # ParamSpec and TypeVarTuple
    cases.append(('generic_paramspec', 'def f[**P](x: P) -> None: pass'))
    cases.append(('generic_typevartuple', 'def f[*Ts](x: tuple[*Ts]) -> None: pass'))
    cases.append(('generic_all_kinds', 'def f[T, **P, *Ts](x: T) -> None: pass'))

    # Complex type expressions
    cases.append(('type_complex_1', 'type Alias = int | str | None'))
    cases.append(('type_complex_2', 'type Alias = list[int] | tuple[str, ...]'))
    cases.append(('type_complex_3', 'type Alias[T] = dict[str, list[T]] | None'))

    # Nested generics
    cases.append(('type_nested', 'class Outer[T]:\n class Inner[U]: pass'))
    cases.append(('type_nested_func', 'class C[T]:\n def f[U](self, x: U) -> T | U: ...'))

    # Self-referential type aliases
    cases.append(('type_self_ref', 'type Tree[T] = T | list[Tree[T]]'))
    cases.append(('type_mutual', 'type A = int | B\ntype B = str | A'))

    # Type alias in various scopes
    cases.append(('type_in_func', 'def f():\n type T = int\n return T'))
    cases.append(('type_in_class', 'class C:\n type T = int'))
    cases.append(('type_in_if', 'if True:\n type T = int'))

    # Edge: many type parameters
    params = ', '.join(f'T{i}' for i in range(50))
    cases.append(('type_many_params', f'class C[{params}]: pass'))

    # Type aliases with forward references
    cases.append(('type_forward', 'type A = "B"\nclass B: pass'))

    return cases


# ========== Generator: exception group edge cases ==========

def gen_exception_group_cases():
    """Generate exception group (PEP 654) edge cases."""
    cases = []

    # Basic ExceptionGroup
    cases.append(('exgrp_basic', '''
try:
    raise ExceptionGroup("eg", [ValueError(1), TypeError(2)])
except* ValueError as e:
    pass
except* TypeError as e:
    pass
'''))

    # Nested ExceptionGroups
    cases.append(('exgrp_nested', '''
try:
    raise ExceptionGroup("outer", [
        ExceptionGroup("inner1", [ValueError(1)]),
        ExceptionGroup("inner2", [TypeError(2)]),
    ])
except* ValueError:
    pass
except* TypeError:
    pass
'''))

    # except* with multiple exception types
    cases.append(('exgrp_multi', '''
try:
    raise ExceptionGroup("eg", [ValueError(1), TypeError(2), KeyError(3)])
except* (ValueError, TypeError):
    pass
except* KeyError:
    pass
'''))

    # Deeply nested
    code = 'eg = ExceptionGroup("l0", [ValueError(0)])\n'
    for i in range(1, 20):
        code += f'eg = ExceptionGroup("l{i}", [eg])\n'
    code += 'try:\n    raise eg\nexcept* ValueError:\n    pass\n'
    cases.append(('exgrp_deep', code))

    # Many exceptions in group
    excs = ', '.join(f'ValueError({i})' for i in range(100))
    cases.append(('exgrp_many', f'''
try:
    raise ExceptionGroup("eg", [{excs}])
except* ValueError:
    pass
'''))

    # except* and regular except interaction
    cases.append(('exgrp_mix', '''
try:
    try:
        raise ExceptionGroup("eg", [ValueError(1)])
    except* ValueError:
        raise TypeError("from except*")
except TypeError:
    pass
'''))

    # ExceptionGroup subclass
    cases.append(('exgrp_subclass', '''
class MyGroup(ExceptionGroup):
    pass

try:
    raise MyGroup("eg", [ValueError(1)])
except* ValueError:
    pass
'''))

    # except* with re-raise
    cases.append(('exgrp_reraise', '''
try:
    try:
        raise ExceptionGroup("eg", [ValueError(1), TypeError(2)])
    except* ValueError:
        raise
except* ValueError:
    pass
'''))

    # Empty exception group (should raise)
    cases.append(('exgrp_empty', '''
try:
    raise ExceptionGroup("eg", [])
except (ValueError, TypeError):
    pass
'''))

    # BaseExceptionGroup
    cases.append(('exgrp_base', '''
try:
    raise BaseExceptionGroup("eg", [KeyboardInterrupt()])
except* KeyboardInterrupt:
    pass
'''))

    return cases


# ========== Generator: object protocol edge cases ==========

def gen_object_protocol_cases():
    """Generate edge cases for Python's object protocol."""
    cases = []

    # __del__ edge cases
    cases.append(('obj_del_cycle', '''
import gc
class C:
    def __del__(self):
        pass
a = C()
b = C()
a.ref = b
b.ref = a
del a, b
gc.collect()
'''))

    cases.append(('obj_del_resurrect', '''
import gc
holder = []
class C:
    def __del__(self):
        holder.append(self)
c = C()
del c
gc.collect()
'''))

    cases.append(('obj_del_exception', '''
import gc
class C:
    def __del__(self):
        raise RuntimeError("in __del__")
c = C()
del c
gc.collect()
'''))

    # __hash__ edge cases
    cases.append(('obj_hash_neg1', '''
class C:
    def __hash__(self):
        return -1  # CPython converts -1 to -2
c = C()
assert hash(c) == -2
'''))

    cases.append(('obj_hash_huge', '''
class C:
    def __hash__(self):
        return 2**100
c = C()
hash(c)
{c: 1}
'''))

    # __eq__ with side effects
    cases.append(('obj_eq_side_effect', '''
class C:
    def __eq__(self, other):
        raise RuntimeError("eq!")
    def __hash__(self):
        return 1
d = {}
try:
    d[C()] = 1
    d[C()] = 2
except RuntimeError:
    pass
'''))

    # __bool__ edge cases
    cases.append(('obj_bool_raises', '''
class C:
    def __bool__(self):
        raise ValueError("bool!")
c = C()
try:
    if c: pass
except ValueError:
    pass
'''))

    # __len__ returning unusual values
    cases.append(('obj_len_negative', '''
class C:
    def __len__(self):
        return -1
try:
    len(C())
except ValueError:
    pass
'''))

    cases.append(('obj_len_huge', '''
class C:
    def __len__(self):
        return 2**100
try:
    len(C())
except OverflowError:
    pass
'''))

    cases.append(('obj_len_float', '''
class C:
    def __len__(self):
        return 1.5
try:
    len(C())
except TypeError:
    pass
'''))

    # __index__ edge cases
    cases.append(('obj_index_huge', '''
class C:
    def __index__(self):
        return 2**1000
x = [1, 2, 3]
try:
    x[C()]
except (IndexError, OverflowError):
    pass
'''))

    # __getattr__ infinite recursion
    cases.append(('obj_getattr_recurse', '''
import sys
sys.setrecursionlimit(50)
class C:
    def __getattr__(self, name):
        return getattr(self, name)
try:
    C().x
except RecursionError:
    pass
finally:
    sys.setrecursionlimit(1000)
'''))

    # Descriptor protocol
    cases.append(('obj_descriptor_data', '''
class Desc:
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, objtype=None):
        return getattr(obj, f"_{self.name}", None)
    def __set__(self, obj, value):
        setattr(obj, f"_{self.name}", value)
    def __delete__(self, obj):
        delattr(obj, f"_{self.name}")

class C:
    x = Desc()

c = C()
c.x = 42
assert c.x == 42
del c.x
assert c.x is None
'''))

    # Metaclass edge cases
    cases.append(('obj_metaclass_1', '''
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        cls.created = True
        return cls

class C(metaclass=Meta):
    pass

assert C.created
'''))

    cases.append(('obj_metaclass_conflict', '''
class Meta1(type): pass
class Meta2(type): pass
class A(metaclass=Meta1): pass
class B(metaclass=Meta2): pass
try:
    class C(A, B): pass
except TypeError:
    pass
'''))

    # __init_subclass__
    cases.append(('obj_init_subclass', '''
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.initialized = True

class Child(Base):
    pass

assert Child.initialized
'''))

    # __set_name__
    cases.append(('obj_set_name', '''
class Desc:
    def __set_name__(self, owner, name):
        self.name = name
        self.owner = owner

class C:
    x = Desc()

assert C.x.name == "x"
assert C.x.owner is C
'''))

    # __class_getitem__
    cases.append(('obj_class_getitem', '''
class C:
    def __class_getitem__(cls, item):
        return f"C[{item}]"
assert C[int] == "C[<class 'int'>]"
'''))

    # __mro_entries__
    cases.append(('obj_mro_entries', '''
class MyBase:
    def __mro_entries__(self, bases):
        return (int,)
try:
    class C(MyBase()):
        pass
except TypeError:
    pass
'''))

    # __slots__ edge cases
    cases.append(('obj_slots_1', '''
class C:
    __slots__ = ('x', 'y')
c = C()
c.x = 1
c.y = 2
try:
    c.z = 3
except AttributeError:
    pass
'''))

    cases.append(('obj_slots_inherit', '''
class A:
    __slots__ = ('x',)
class B(A):
    __slots__ = ('x', 'y')
b = B()
b.x = 1
b.y = 2
'''))

    # __repr__ cycle
    cases.append(('obj_repr_cycle', '''
class C:
    def __repr__(self):
        return repr(self.ref)
a = C()
b = C()
a.ref = b
b.ref = a
try:
    repr(a)
except RecursionError:
    pass
'''))

    # Multiple inheritance MRO edge cases
    cases.append(('obj_mro_complex', '''
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
assert D.__mro__ == (D, B, C, A, object)
'''))

    cases.append(('obj_mro_impossible', '''
class A: pass
class B(A): pass
try:
    class C(A, B): pass
except TypeError:
    pass
'''))

    return cases


# ========== Generator: unicode edge cases ==========

def gen_unicode_cases():
    """Generate unicode edge cases."""
    cases = []

    # Unicode identifiers
    cases.append(('unicode_ident_1', '\u00e9 = 1'))  # é
    cases.append(('unicode_ident_2', '\u03b1 = 1'))  # α
    cases.append(('unicode_ident_3', '\u4e2d = 1'))  # 中
    cases.append(('unicode_ident_4', '\U0001d400 = 1'))  # 𝐀 (mathematical bold A)
    cases.append(('unicode_ident_5', '\u0410 = 1'))  # А (Cyrillic A)

    # Unicode normalization
    cases.append(('unicode_norm_1', '\u00e9 = 1\nassert \u0065\u0301 == 1'))  # é vs e + combining accent

    # Unicode string operations
    cases.append(('unicode_str_1', 's = "\\U0001f600"\nassert len(s) == 1'))
    cases.append(('unicode_str_2', 's = "\\U0001f600\\U0001f601"\nassert len(s) == 2'))

    # Unicode in various positions
    cases.append(('unicode_class', 'class \u00c7lass: pass'))
    cases.append(('unicode_func', 'def \u0192unc(): pass'))
    cases.append(('unicode_import', 'try:\n import \u00e9\nexcept (ImportError, ModuleNotFoundError):\n pass'))

    # Confusable characters
    cases.append(('unicode_confuse', 'A = 1\n\u0410 = 2\nassert A != \u0410 or A == \u0410'))

    # Zero-width characters
    cases.append(('unicode_zw_1', '# zero\u200bwidth'))  # Zero-width space in comment
    cases.append(('unicode_zw_2', 'x = "a\u200bb"'))  # In string

    # Right-to-left
    cases.append(('unicode_rtl', 'x = "\u202eHello"'))

    # BOM
    cases.append(('unicode_bom', '\ufeffx = 1'))  # BOM at start

    # Surrogates (should be rejected)
    cases.append(('unicode_surrogate', '''
try:
    s = "\\ud800"
except Exception:
    pass
'''))

    # Unicode escapes in source
    cases.append(('unicode_escape_1', 'x = "\\N{SNOWMAN}"'))
    cases.append(('unicode_escape_2', 'x = "\\N{GREEK SMALL LETTER ALPHA}"'))

    return cases


# ========== Generator: GC/memory edge cases ==========

def gen_gc_cases():
    """Generate garbage collector and memory edge cases."""
    cases = []

    # GC with weakrefs
    cases.append(('gc_weakref', '''
import weakref
import gc
class C:
    pass
c = C()
r = weakref.ref(c)
del c
gc.collect()
assert r() is None
'''))

    # Weakref callback during GC
    cases.append(('gc_weakref_callback', '''
import weakref
import gc
collected = []
class C:
    pass
def callback(ref):
    collected.append(1)
c = C()
r = weakref.ref(c, callback)
del c
gc.collect()
assert len(collected) == 1
'''))

    # GC with __del__ creating new refs
    cases.append(('gc_del_new_ref', '''
import gc
saved = []
class C:
    def __del__(self):
        saved.append(self)
class D:
    pass
c = C()
c.d = D()
c.d.c = c
del c
gc.collect()
'''))

    # Disable/enable GC
    cases.append(('gc_disable', '''
import gc
gc.disable()
try:
    x = []
    for i in range(1000):
        y = []
        x.append(y)
        y.append(x)
finally:
    gc.enable()
    gc.collect()
'''))

    # GC callbacks
    cases.append(('gc_callback', '''
import gc
events = []
def cb(phase, info):
    events.append((phase, info))
gc.callbacks.append(cb)
try:
    gc.collect()
finally:
    gc.callbacks.remove(cb)
'''))

    # Finalizer ordering
    cases.append(('gc_finalizer_order', '''
import gc
order = []
class C:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        order.append(self.name)
a = C("a")
b = C("b")
a.ref = b
del a
del b
gc.collect()
'''))

    # gc.get_referrers / gc.get_referents
    cases.append(('gc_referrers', '''
import gc
class C: pass
c = C()
refs = gc.get_referrers(c)
gc.get_referents(c)
'''))

    return cases


# ========== Generator: code object edge cases ==========

def gen_code_object_cases():
    """Generate code object manipulation edge cases."""
    cases = []

    # code.replace() edge cases
    cases.append(('code_replace_name', '''
def f():
    return 42
code = f.__code__
new_code = code.replace(co_name="new_name")
f.__code__ = new_code
assert f() == 42
assert f.__code__.co_name == "new_name"
'''))

    cases.append(('code_replace_filename', '''
def f():
    return 42
code = f.__code__
new_code = code.replace(co_filename="new_file.py")
f.__code__ = new_code
assert f() == 42
'''))

    # Nested closures
    cases.append(('code_closure_deep', '''
def f():
    x = 1
    def g():
        y = x
        def h():
            z = y
            def i():
                return z
            return i
        return h
    return g
assert f()()()() == 1
'''))

    # Generator code objects
    cases.append(('code_gen', '''
def gen():
    yield 1
    yield 2
    return 3
g = gen()
assert next(g) == 1
assert next(g) == 2
try:
    next(g)
except StopIteration as e:
    assert e.value == 3
'''))

    # Async generator
    cases.append(('code_async_gen', '''
import asyncio
async def agen():
    yield 1
    yield 2

async def main():
    results = []
    async for x in agen():
        results.append(x)
    assert results == [1, 2]

asyncio.run(main())
'''))

    # exec/eval with various code objects
    cases.append(('code_exec_compiled', '''
code = compile("x = 42", "<test>", "exec")
ns = {}
exec(code, ns)
assert ns["x"] == 42
'''))

    cases.append(('code_eval_compiled', '''
code = compile("1 + 2", "<test>", "eval")
assert eval(code) == 3
'''))

    # Compile with optimize flag
    for opt in [0, 1, 2]:
        cases.append((f'code_optimize_{opt}', f'''
code = compile("assert False, 'test'", "<test>", "exec", optimize={opt})
ns = {{}}
try:
    exec(code, ns)
except AssertionError:
    pass
'''))

    # compile() with ast.PyCF flags
    cases.append(('code_flags_1', '''
import ast
code = compile("x = 1", "<test>", "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
exec(code)
'''))

    # Code with many constants
    cases.append(('code_many_consts', f'''
def f():
    return ({", ".join(str(i) for i in range(1000))},)
result = f()
assert len(result) == 1000
'''))

    # Code with many local variables
    n = 200
    lines = [f'    x{i} = {i}' for i in range(n)]
    lines.append(f'    return {"+".join(f"x{i}" for i in range(n))}')
    cases.append(('code_many_locals', f'def f():\n' + '\n'.join(lines) + '\nf()'))

    return cases


# ========== Generator: builtin function edge cases ==========

def gen_builtin_cases():
    """Generate edge cases for builtin functions."""
    cases = []

    # int() edge cases
    cases.append(('builtin_int_base', '''
for base in range(2, 37):
    int("10", base)
try:
    int("10", 1)
except ValueError:
    pass
try:
    int("10", 37)
except ValueError:
    pass
'''))

    cases.append(('builtin_int_huge', '''
x = int("9" * 10000)
str(x)
'''))

    cases.append(('builtin_int_underscores', '''
assert int("1_000_000") == 1000000
assert int("0x_ff", 16) == 255
assert int("0b_1010", 2) == 10
assert int("0o_77", 8) == 63
'''))

    # float() edge cases
    cases.append(('builtin_float_edge', '''
assert float("inf") == float("infinity")
assert float("-inf") == float("-infinity")
import math
assert math.isnan(float("nan"))
'''))

    # complex() edge cases
    cases.append(('builtin_complex', '''
assert complex("1+2j") == (1+2j)
assert complex("1") == (1+0j)
assert complex("2j") == 2j
try:
    complex("1 + 2j")  # spaces not allowed
except ValueError:
    pass
'''))

    # format() edge cases
    cases.append(('builtin_format_1', '''
format(42, "b")
format(42, "o")
format(42, "x")
format(42, "X")
format(42, "n")
format(42, "d")
format(3.14, ".2f")
format(3.14, ".2e")
format(3.14, ".2g")
format(3.14, ".2%")
format("hello", ">20")
format("hello", "^20")
format("hello", "<20")
'''))

    # eval/exec edge cases
    cases.append(('builtin_eval_globals', '''
result = eval("x + 1", {"x": 41})
assert result == 42
'''))

    cases.append(('builtin_exec_custom_ns', '''
ns = {"__builtins__": {}}
try:
    exec("print(1)", ns)
except (NameError, TypeError):
    pass
'''))

    cases.append(('builtin_exec_no_builtins', '''
ns = {"__builtins__": None}
try:
    exec("x = 1", ns)
except TypeError:
    pass
'''))

    # super() edge cases
    cases.append(('builtin_super', '''
class A:
    def method(self):
        return "A"
class B(A):
    def method(self):
        return super().method() + "B"
class C(A):
    def method(self):
        return super().method() + "C"
class D(B, C):
    def method(self):
        return super().method() + "D"
result = D().method()
assert result == "ACBD", f"Got {result}"
'''))

    # isinstance/issubclass with unusual args
    cases.append(('builtin_isinstance', '''
class Meta(type):
    def __instancecheck__(cls, instance):
        return True
class C(metaclass=Meta):
    pass
assert isinstance(42, C)
'''))

    cases.append(('builtin_issubclass', '''
class Meta(type):
    def __subclasscheck__(cls, subclass):
        return True
class C(metaclass=Meta):
    pass
assert issubclass(int, C)
'''))

    # sorted() with unusual key/cmp
    cases.append(('builtin_sorted_key', '''
class Uncomparable:
    def __lt__(self, other):
        raise TypeError("no")
try:
    sorted([Uncomparable(), Uncomparable()])
except TypeError:
    pass
'''))

    # vars(), dir() edge cases
    cases.append(('builtin_vars', '''
class C:
    def __init__(self):
        self.x = 1
c = C()
assert vars(c) == {"x": 1}
'''))

    # property edge cases
    cases.append(('builtin_property', '''
class C:
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x
c = C()
c.x = 42
assert c.x == 42
del c.x
try:
    c.x
except AttributeError:
    pass
'''))

    # staticmethod/classmethod edge cases
    cases.append(('builtin_staticmethod', '''
class C:
    @staticmethod
    def f():
        return 42
assert C.f() == 42
assert C().f() == 42
'''))

    return cases


# ========== Generator: compile() error attribute testing ==========

def gen_compile_error_attrs():
    """Test that compile() and ast.parse() produce correct error attributes.
    This is the area where the repo found its bug (#127927)."""
    cases = []

    # Various syntax errors with known positions
    error_codes = [
        ('1 +', 'unexpected EOF'),
        ('def', 'invalid syntax'),
        ('x y', 'invalid syntax'),
        ('class', 'invalid syntax'),
        ('if', 'invalid syntax'),
        ('return', 'outside function'),
        ('yield', 'outside function'),
        ('break', 'outside loop'),
        ('continue', 'outside loop'),
        ('import *', 'invalid syntax'),
        ('from import x', 'invalid syntax'),
        ('def f(x, x): pass', 'duplicate argument'),
        ('def f(**k, x): pass', 'invalid syntax'),
        ('x = (yield)', 'outside function'),
        ('async for x in y: pass', 'outside async'),
        ('await x', 'outside'),
        ('@\ndef f(): pass', 'invalid syntax'),
        ('f(x for x in range(10), 1)', 'Generator expression must be parenthesized'),
        ('{x for x in range(10): 1}', 'invalid syntax'),
    ]

    for i, (code, _expected_msg_part) in enumerate(error_codes):
        # Test with various filenames including the "self-referencing" filename trick
        cases.append((f'compile_err_attr_{i}_default', f'''
import ast
try:
    ast.parse({code!r})
except SyntaxError as e:
    pass  # Just checking it doesn't crash
'''))

        cases.append((f'compile_err_attr_{i}_custom', f'''
import ast
try:
    ast.parse({code!r}, filename="<custom>")
except SyntaxError as e:
    pass
'''))

    # Test compile() with matching filename (the bug from #127927)
    cases.append(('compile_err_self_ref', '''
import ast
import os
import sys

# Test: compile code with filename matching the current script
# This is the pattern that triggered bug #127927
code = "x y"
try:
    ast.parse(code, filename=__file__)
except SyntaxError as e:
    # The error attributes should refer to the code string, not the file
    pass
'''))

    # Test with various flag combinations
    import __future__
    flag_names = [name for name in dir(__future__) if not name.startswith('_')]
    cases.append(('compile_err_flags', '''
import __future__
import ast

code = "x y"  # syntax error
flags = 0
for name in dir(__future__):
    obj = getattr(__future__, name)
    if isinstance(obj, __future__._Feature):
        flags |= obj.compiler_flag

try:
    compile(code, "<test>", "exec", flags=flags)
except SyntaxError as e:
    pass
'''))

    return cases


# ========== Generator: random program generation ==========

def gen_random_programs(count=500):
    """Generate random Python programs by composing elements."""
    cases = []

    elements = {
        'assign': lambda: f'{_rand_ident()} = {_rand_int()}',
        'aug_assign': lambda: f'{_rand_ident()} = 0\n{_rand_ident()} += {_rand_int()}',
        'func_def': lambda: f'def {_rand_ident()}({", ".join(_rand_ident() for _ in range(random.randint(0, 5)))}):\n    return {_rand_int()}',
        'class_def': lambda: f'class {_rand_ident()}:\n    {_rand_ident()} = {_rand_int()}',
        'if_stmt': lambda: f'if {_rand_int()} > 0:\n    pass\nelse:\n    pass',
        'for_loop': lambda: f'for {_rand_ident()} in range({random.randint(0, 10)}):\n    pass',
        'while_loop': lambda: f'{_rand_ident()} = 0\nwhile {_rand_ident()} < {random.randint(1, 5)}:\n    {_rand_ident()} += 1',
        'try_except': lambda: f'try:\n    pass\nexcept Exception:\n    pass',
        'with_stmt': lambda: f'class CM:\n    def __enter__(self): return self\n    def __exit__(self, *a): pass\nwith CM(): pass',
        'list_comp': lambda: f'[{_rand_ident()} for {_rand_ident()} in range({random.randint(0, 10)})]',
        'dict_comp': lambda: f'{{{_rand_ident()}: {_rand_ident()} for {_rand_ident()} in range({random.randint(0, 10)})}}',
        'set_comp': lambda: f'{{{_rand_ident()} for {_rand_ident()} in range({random.randint(0, 10)})}}',
        'gen_expr': lambda: f'list({_rand_ident()} for {_rand_ident()} in range({random.randint(0, 10)}))',
        'lambda': lambda: f'(lambda {", ".join(_rand_ident() for _ in range(random.randint(0, 3)))}: {_rand_int()})()',
        'assert_stmt': lambda: f'assert True',
        'del_stmt': lambda: f'{_rand_ident()} = 1\ndel {_rand_ident()}',
        'global_stmt': lambda: f'def f():\n    global {_rand_ident()}\n    {_rand_ident()} = 1',
        'nonlocal_stmt': lambda: f'def f():\n    {_rand_ident()} = 1\n    def g():\n        nonlocal {_rand_ident()}\n        {_rand_ident()} = 2\n    g()',
        'decorator': lambda: f'def dec(f): return f\n@dec\ndef {_rand_ident()}(): pass',
        'starred': lambda: f'a, *b = [1, 2, 3, 4]',
        'walrus': lambda: f'if (x := {_rand_int()}) > 0: pass',
    }

    for i in range(count):
        # Pick 1-5 random elements and combine
        n = random.randint(1, 5)
        selected = random.choices(list(elements.values()), k=n)
        parts = []
        for gen_fn in selected:
            try:
                parts.append(gen_fn())
            except Exception:
                parts.append('pass')
        code = '\n'.join(parts)
        cases.append((f'random_prog_{i}', code))

    return cases


# ========== Generator: compile() differential testing ==========

def gen_compile_differential():
    """Generate cases for differential testing of compile() modes and flags."""
    cases = []

    # Test that compile + exec produces same result as direct exec
    test_codes = [
        'x = 1 + 2',
        'x = [i**2 for i in range(10)]',
        'x = {i: i**2 for i in range(10)}',
        'def f(n): return n * 2\nx = f(21)',
        'x = (lambda n: n * 2)(21)',
        'x = sum(range(100))',
        'x = list(map(lambda n: n**2, range(10)))',
        'x = sorted([3, 1, 4, 1, 5, 9], reverse=True)',
    ]

    for i, code in enumerate(test_codes):
        cases.append((f'diff_compile_{i}', f'''
ns1 = {{}}
ns2 = {{}}
exec({code!r}, ns1)
compiled = compile({code!r}, "<test>", "exec")
exec(compiled, ns2)
assert ns1.get("x") == ns2.get("x"), f"Direct: {{ns1.get('x')}}, Compiled: {{ns2.get('x')}}"
'''))

    # Test compile with different optimization levels
    for opt in [0, 1, 2]:
        cases.append((f'diff_optimize_{opt}', f'''
code = "x = sum(range(100))"
c = compile(code, "<test>", "exec", optimize={opt})
ns = {{}}
exec(c, ns)
assert ns["x"] == 4950
'''))

    return cases


# ========== Generator: sys/os edge cases ==========

def gen_sys_edge_cases():
    """Generate edge cases for sys module internals."""
    cases = []

    # sys.settrace edge cases
    cases.append(('sys_settrace', '''
import sys
events = []
def tracer(frame, event, arg):
    events.append(event)
    return tracer
sys.settrace(tracer)
try:
    x = 1 + 2
finally:
    sys.settrace(None)
'''))

    # sys.setprofile edge cases
    cases.append(('sys_setprofile', '''
import sys
events = []
def profiler(frame, event, arg):
    events.append(event)
sys.setprofile(profiler)
try:
    x = 1 + 2
finally:
    sys.setprofile(None)
'''))

    # sys.setrecursionlimit edge cases
    cases.append(('sys_recursion_low', '''
import sys
old = sys.getrecursionlimit()
sys.setrecursionlimit(10)
try:
    def f(): f()
    try:
        f()
    except RecursionError:
        pass
finally:
    sys.setrecursionlimit(old)
'''))

    # sys.getsizeof
    cases.append(('sys_getsizeof', '''
import sys
sys.getsizeof(0)
sys.getsizeof(1)
sys.getsizeof(2**100)
sys.getsizeof("")
sys.getsizeof("x" * 10000)
sys.getsizeof([])
sys.getsizeof(list(range(1000)))
sys.getsizeof({})
sys.getsizeof(dict.fromkeys(range(1000)))
'''))

    # Frame object edge cases
    cases.append(('sys_frame', '''
import sys
frame = sys._getframe(0)
assert frame.f_code.co_filename
assert frame.f_lineno > 0
assert frame.f_locals is not None
'''))

    return cases


# ========== Generator: struct/memoryview edge cases ==========

def gen_struct_cases():
    """Generate struct and memoryview edge cases."""
    cases = []

    # struct pack/unpack edge cases
    cases.append(('struct_basic', '''
import struct
for fmt in ["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q", "f", "d"]:
    val = struct.unpack(fmt, struct.pack(fmt, 0))[0]
'''))

    cases.append(('struct_padding', '''
import struct
struct.pack("bh", 1, 2)
struct.pack("=bh", 1, 2)
struct.pack("<bh", 1, 2)
struct.pack(">bh", 1, 2)
struct.pack("!bh", 1, 2)
'''))

    cases.append(('struct_overflow', '''
import struct
try:
    struct.pack("b", 128)
except struct.error:
    pass
try:
    struct.pack("B", 256)
except struct.error:
    pass
'''))

    # memoryview edge cases
    cases.append(('memoryview_basic', '''
b = bytearray(b"hello world")
mv = memoryview(b)
assert mv[0] == ord("h")
mv[0] = ord("H")
assert b[0] == ord("H")
mv.release()
'''))

    cases.append(('memoryview_slice', '''
b = bytearray(range(256))
mv = memoryview(b)
s = mv[10:20]
assert len(s) == 10
s.release()
mv.release()
'''))

    cases.append(('memoryview_cast', '''
import array
a = array.array("i", [1, 2, 3, 4])
mv = memoryview(a)
b = mv.cast("B")
assert len(b) == 16
b.release()
mv.release()
'''))

    cases.append(('memoryview_readonly', '''
b = bytes(b"hello")
mv = memoryview(b)
assert mv.readonly
try:
    mv[0] = 42
except TypeError:
    pass
mv.release()
'''))

    return cases


# ========== Generator: string method edge cases ==========

def gen_string_method_cases():
    """Generate string method edge cases."""
    cases = []

    # str.format edge cases
    cases.append(('str_format_nested', '''
"{0:{1}}".format("hello", ">20")
"{0:{1}.{2}}".format(3.14, 10, 2)
'''))

    cases.append(('str_format_recursive', '''
try:
    class C:
        def __format__(self, spec):
            return format(self, spec)
    format(C(), "")
except RecursionError:
    pass
'''))

    # str.encode edge cases
    cases.append(('str_encode_surrogates', '''
try:
    "\\ud800".encode("utf-8")
except UnicodeEncodeError:
    pass
"\\ud800".encode("utf-8", "surrogatepass")
'''))

    # str.translate edge cases
    cases.append(('str_translate', '''
table = str.maketrans({"a": "A", "b": None, "c": "CC"})
"abcdef".translate(table)
'''))

    # str % formatting edge cases
    cases.append(('str_percent_format', '''
"%s" % (42,)
"%(name)s" % {"name": "test"}
"%*d" % (10, 42)
"%.*f" % (2, 3.14)
'''))

    # str.split edge cases
    cases.append(('str_split_edge', '''
"".split()
"".split(",")
",".split(",")
",,".split(",")
"a,,b".split(",")
'''))

    return cases


# ========== Generator: regex edge cases ==========

def gen_regex_cases():
    """Generate regular expression edge cases."""
    cases = []

    # Complex patterns
    cases.append(('regex_backtrack', '''
import re
try:
    re.match("(a+)+b", "a" * 25, timeout=1)
except (re.error, TimeoutError):
    pass
except TypeError:
    # timeout parameter might not exist
    try:
        re.match("(a+)+b", "a" * 20)
    except re.error:
        pass
'''))

    # Lookahead/lookbehind
    cases.append(('regex_lookaround', '''
import re
assert re.search(r"(?<=a)b", "ab").group() == "b"
assert re.search(r"a(?=b)", "ab").group() == "a"
assert re.search(r"(?<!a)b", "cb").group() == "b"
assert re.search(r"a(?!b)", "ac").group() == "a"
'''))

    # Named groups
    cases.append(('regex_named_groups', '''
import re
m = re.match(r"(?P<first>\\w+) (?P<last>\\w+)", "John Doe")
assert m.group("first") == "John"
assert m.group("last") == "Doe"
'''))

    # Atomic groups / possessive quantifiers
    cases.append(('regex_atomic', '''
import re
try:
    re.compile(r"(?>a+)b")
except re.error:
    pass
'''))

    # Large number of groups
    cases.append(('regex_many_groups', '''
import re
pattern = "".join(f"(a)" for _ in range(100))
try:
    re.compile(pattern)
except re.error:
    pass
'''))

    # Unicode categories in regex
    cases.append(('regex_unicode', '''
import re
assert re.match(r"\\w+", "café").group() == "café"
assert re.match(r"\\d+", "٤٢")  # Arabic digits
'''))

    return cases


# ========== Generator: iterator protocol edge cases ==========

def gen_iterator_cases():
    """Generate iterator protocol edge cases."""
    cases = []

    # Iterator with __length_hint__
    cases.append(('iter_length_hint', '''
class MyIter:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i
    def __length_hint__(self):
        return self.n - self.i

it = MyIter(10)
list(it)
'''))

    # Iterator that raises in __next__
    cases.append(('iter_raise', '''
class BadIter:
    def __iter__(self):
        return self
    def __next__(self):
        raise RuntimeError("bad!")

try:
    list(BadIter())
except RuntimeError:
    pass
'''))

    # Iterator that lies about length
    cases.append(('iter_bad_length', '''
class LyingIter:
    def __init__(self):
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= 3:
            raise StopIteration
        self.i += 1
        return self.i
    def __length_hint__(self):
        return 1000000

list(LyingIter())
'''))

    # Reentrant iteration
    cases.append(('iter_reentrant', '''
class ReentrantList:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        for item in self.data:
            yield item
            if isinstance(item, list):
                yield from item

list(ReentrantList([1, [2, 3], 4]))
'''))

    # Generator with send/throw/close
    cases.append(('gen_send_throw', '''
def gen():
    try:
        x = yield 1
        yield x
    except GeneratorExit:
        return
    except ValueError:
        yield "caught"

g = gen()
assert next(g) == 1
assert g.send(42) == 42
g.close()

g2 = gen()
next(g2)
result = g2.throw(ValueError, "test")
assert result == "caught"
'''))

    return cases


# ========== Generator: edge cases in arithmetic/numeric ==========

def gen_numeric_cases():
    """Generate numeric edge cases."""
    cases = []

    # Integer edge cases
    cases.append(('num_large_int', '''
x = 10 ** 10000
y = x + 1
assert y > x
str(y)
'''))

    cases.append(('num_int_bit_ops', '''
x = (1 << 1000) - 1
y = x & (x >> 1)
z = x | (x << 1)
w = x ^ y
'''))

    # Float edge cases
    cases.append(('num_float_special', '''
import math
x = float("inf")
y = float("-inf")
z = float("nan")
assert x > 0
assert y < 0
assert z != z
assert not (z == z)
assert math.isinf(x)
assert math.isnan(z)
'''))

    cases.append(('num_float_precision', '''
assert 0.1 + 0.2 != 0.3
assert abs(0.1 + 0.2 - 0.3) < 1e-15
'''))

    # Division edge cases
    cases.append(('num_divmod', '''
for a in [0, 1, -1, 7, -7, 2**31, -(2**31)]:
    for b in [1, -1, 3, -3, 7, -7]:
        q, r = divmod(a, b)
        assert a == b * q + r
        assert 0 <= abs(r) < abs(b)
'''))

    # pow() edge cases
    cases.append(('num_pow', '''
assert pow(2, 10) == 1024
assert pow(2, 10, 1000) == 24
assert pow(2, -1) == 0.5
assert pow(0, 0) == 1
try:
    pow(0, -1)
except ZeroDivisionError:
    pass
'''))

    # Decimal edge cases
    cases.append(('num_decimal', '''
from decimal import Decimal, InvalidOperation, DivisionByZero
x = Decimal("0.1") + Decimal("0.2")
assert x == Decimal("0.3")
try:
    Decimal("1") / Decimal("0")
except DivisionByZero:
    pass
try:
    Decimal("nan") + Decimal("1")
except InvalidOperation:
    pass
'''))

    # Fraction edge cases
    cases.append(('num_fraction', '''
from fractions import Fraction
f = Fraction(1, 3) + Fraction(2, 3)
assert f == 1
f = Fraction(0, 1)
assert f == 0
try:
    Fraction(1, 0)
except ZeroDivisionError:
    pass
'''))

    return cases


# ========== Generator: async/await edge cases ==========

def gen_async_cases():
    """Generate async/await edge cases."""
    cases = []

    cases.append(('async_basic', '''
import asyncio
async def f():
    return 42
assert asyncio.run(f()) == 42
'''))

    cases.append(('async_gather', '''
import asyncio
async def f(n):
    await asyncio.sleep(0)
    return n
async def main():
    results = await asyncio.gather(f(1), f(2), f(3))
    assert results == [1, 2, 3]
asyncio.run(main())
'''))

    cases.append(('async_cancel', '''
import asyncio
async def long_task():
    await asyncio.sleep(100)
async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(0)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass
asyncio.run(main())
'''))

    cases.append(('async_exception_group', '''
import asyncio
async def fail(msg):
    raise ValueError(msg)
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fail("a"))
            tg.create_task(fail("b"))
    except* ValueError:
        pass
asyncio.run(main())
'''))

    cases.append(('async_contextmanager', '''
import asyncio
class AsyncCM:
    async def __aenter__(self):
        return self
    async def __aexit__(self, *args):
        pass
async def main():
    async with AsyncCM() as cm:
        pass
asyncio.run(main())
'''))

    return cases


# ========== Generator: pickle edge cases ==========

def gen_pickle_cases():
    """Generate pickle edge cases."""
    cases = []

    cases.append(('pickle_basic', '''
import pickle
for obj in [None, True, False, 0, 1, -1, 3.14, "hello", b"bytes", [], {}, set()]:
    assert pickle.loads(pickle.dumps(obj)) == obj or (obj != obj)
'''))

    cases.append(('pickle_recursive', '''
import pickle
x = []
x.append(x)
try:
    pickle.dumps(x)
except (RecursionError, ValueError):
    pass
'''))

    cases.append(('pickle_custom_reduce', '''
import pickle
class C:
    def __reduce__(self):
        return (C, ())
c = C()
c2 = pickle.loads(pickle.dumps(c))
assert isinstance(c2, C)
'''))

    cases.append(('pickle_protocols', '''
import pickle
for proto in range(pickle.HIGHEST_PROTOCOL + 1):
    data = pickle.dumps([1, 2, 3], protocol=proto)
    assert pickle.loads(data) == [1, 2, 3]
'''))

    return cases


# ========== Generator: collections edge cases ==========

def gen_collections_cases():
    """Generate edge cases for collections."""
    cases = []

    cases.append(('collections_deque', '''
from collections import deque
d = deque(maxlen=3)
for i in range(10):
    d.append(i)
assert list(d) == [7, 8, 9]
d.rotate(1)
assert list(d) == [9, 7, 8]
d.rotate(-1)
assert list(d) == [7, 8, 9]
'''))

    cases.append(('collections_defaultdict', '''
from collections import defaultdict
dd = defaultdict(list)
dd["a"].append(1)
dd["b"].append(2)
assert dd["c"] == []
'''))

    cases.append(('collections_counter', '''
from collections import Counter
c = Counter("abracadabra")
assert c.most_common(1) == [("a", 5)]
c.update("aaaa")
assert c["a"] == 9
'''))

    cases.append(('collections_chainmap', '''
from collections import ChainMap
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
c = ChainMap(a, b)
assert c["x"] == 1
assert c["y"] == 2  # from first map
assert c["z"] == 4
'''))

    cases.append(('collections_ordereddict', '''
from collections import OrderedDict
od = OrderedDict()
od["b"] = 2
od["a"] = 1
od["c"] = 3
assert list(od.keys()) == ["b", "a", "c"]
od.move_to_end("b")
assert list(od.keys()) == ["a", "c", "b"]
'''))

    return cases


# ========== Master generator ==========

def all_generators():
    """Return all generators."""
    return [
        ('compile_edge_cases', gen_compile_edge_cases),
        ('fstring_cases', gen_fstring_cases),
        ('pattern_matching', gen_pattern_matching_cases),
        ('type_params', gen_type_param_cases),
        ('exception_groups', gen_exception_group_cases),
        ('object_protocol', gen_object_protocol_cases),
        ('unicode', gen_unicode_cases),
        ('gc', gen_gc_cases),
        ('code_objects', gen_code_object_cases),
        ('builtins', gen_builtin_cases),
        ('compile_error_attrs', gen_compile_error_attrs),
        ('random_programs', gen_random_programs),
        ('compile_differential', gen_compile_differential),
        ('sys_edge_cases', gen_sys_edge_cases),
        ('struct_memoryview', gen_struct_cases),
        ('string_methods', gen_string_method_cases),
        ('regex', gen_regex_cases),
        ('iterators', gen_iterator_cases),
        ('numeric', gen_numeric_cases),
        ('async_await', gen_async_cases),
        ('pickle', gen_pickle_cases),
        ('collections', gen_collections_cases),
    ]


def generate_all():
    """Generate all test cases from all generators."""
    all_cases = []
    for name, gen_fn in all_generators():
        try:
            cases = gen_fn()
            all_cases.extend(cases)
        except Exception as e:
            print(f"Error in generator {name}: {e}")
    return all_cases

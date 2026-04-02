# `compile()` SyntaxError has incorrect attributes

**Interpreter:** CPython 3.11, 3.12, 3.13
**Severity:** MEDIUM
**Status:** Reported — [CPython Issue #127927](https://github.com/python/cpython/issues/127927)

## Description

When `compile()` or `ast.parse()` raises a `SyntaxError`, the exception's attributes (`lineno`, `offset`, `text`) are incorrect when the `filename` argument matches the name of the file currently being executed.

The `lineno` and `offset` point into the actual file on disk instead of the code string passed to `compile()`. If the offset in the code string exceeds the length of the corresponding line in the file, the offset is clamped to the file line length plus two.

## Expected Behavior

The `SyntaxError` attributes should always refer to the code string passed to `compile()`, regardless of the `filename` argument.

## Actual Behavior

When `filename` matches the current file, the traceback and error attributes point into the file itself:

```python
# In f.py:
import ast
ast.parse("x y", filename='f.py')
```

```
  File "f.py", line 1
    import ast
      ^
SyntaxError: invalid syntax
```

The error incorrectly points to line 1 of `f.py` rather than the code string `"x y"`.

## Reproducer

```python
import ast
code = "x y"
try:
    ast.parse(code, filename=__file__)
except SyntaxError as e:
    # e.lineno, e.offset, e.text refer to the file, not the code string
    print(f"lineno={e.lineno}, offset={e.offset}, text={e.text!r}")
```

## Versions Tested

- CPython 3.11: **affected**
- CPython 3.12: **affected**
- CPython 3.13: **affected** (partially fixed for `text` attribute)

"""
compile()/ast.parse() SyntaxError has incorrect attributes when filename
matches the current file.

Interpreter: CPython 3.11, 3.12, 3.13
Expected: SyntaxError attributes refer to the code string, not the file
Actual: lineno/offset/text point into the file on disk

See: https://github.com/python/cpython/issues/127927
"""

import ast

code = "x y"  # syntax error at offset 3

# When filename matches the current script, SyntaxError attributes are wrong
try:
    ast.parse(code, filename=__file__)
except SyntaxError as e:
    print(f"filename=__file__: lineno={e.lineno}, offset={e.offset}, text={e.text!r}")

# When filename is something else, attributes are correct
try:
    ast.parse(code, filename="<test>")
except SyntaxError as e:
    print(f"filename='<test>': lineno={e.lineno}, offset={e.offset}, text={e.text!r}")

# cpython py_compile
python fuzz4py/eval.py "./cpython/python -m py_compile" --timeout=30 --output="fuzz4py/resources/cpython_py_compile"

# cpython ast
python fuzz4py/eval.py "./cpython/python -m ast" --timeout=30 --output="fuzz4py/resources/cpython_ast"

# black
python fuzz4py/eval.py "black" --timeout=30 --output="fuzz4py/resources/black"

# pyflakes
python fuzz4py/eval.py "pyflakes" --timeout=30 --output="fuzz4py/resources/pyflakes"

# pylint
python fuzz4py/eval.py "pylint" --timeout=30 --output="fuzz4py/resources/pylint"

# mypy
python fuzz4py/eval.py "mypy" --timeout=30 --output="fuzz4py/resources/mypy"

# pycodestyle
python fuzz4py/eval.py "pycodestyle" --timeout=30 --output="fuzz4py/resources/pycodestyle"

# flake8
python fuzz4py/eval.py "flake8" --timeout=30 --output="fuzz4py/resources/flake8"

# ruff
python fuzz4py/eval.py "ruff check" --timeout=30 --output="fuzz4py/resources/ruff"

# astroid
python fuzz4py/eval.py "python -c 'import astroid; import sys; astroid.parse(open(sys.argv[1]).read())'" --timeout=30 --output="fuzz4py/resources/astroid"

# parso
python fuzz4py/eval.py "python -c 'import parso; import sys; parso.parse(open(sys.argv[1]).read())'" --timeout=30 --output="fuzz4py/resources/parso"

# pytype
python fuzz4py/eval.py "pytype" --timeout=30 --output="fuzz4py/resources/pytype"

# bandit
python fuzz4py/eval.py "bandit" --timeout=30 --output="fuzz4py/resources/bandit"

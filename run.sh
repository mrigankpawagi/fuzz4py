# cpython 3.13 py_compile
echo "Testing cpython 3.13 py_compile"
python fuzz4py/eval.py "python3.13 -m py_compile" --timeout=30 --output="fuzz4py/resources/cpython313_py_compile"

# cpython 3.13 ast
echo "Testing cpython3.13 ast"
python fuzz4py/eval.py "python3.13 -m ast" --timeout=30 --output="fuzz4py/resources/cpython313_ast"

# cpython 3.11 py_compile
echo "Testing cpython 3.11 py_compile"
python fuzz4py/eval.py "python3.11 -m py_compile" --timeout=30 --output="fuzz4py/resources/cpython311_py_compile"

# cpython 3.11 ast
echo "Testing cpython3.11 ast"
python fuzz4py/eval.py "python3.11 -m ast" --timeout=30 --output="fuzz4py/resources/cpython311_ast"

# cpython 3.12 py_compile
echo "Testing cpython 3.12 py_compile"
python fuzz4py/eval.py "python3.12 -m py_compile" --timeout=30 --output="fuzz4py/resources/cpython312_py_compile"

# cpython 3.12 ast
echo "Testing cpython3.12 ast"
python fuzz4py/eval.py "python3.12 -m ast" --timeout=30 --output="fuzz4py/resources/cpython312_ast"

# graalpy py_compile
echo "Testing graalpy py_compile"
python fuzz4py/eval.py "graalpy -m py_compile" --timeout=30 --output="fuzz4py/resources/graalpy_py_compile"

# graalpy ast
echo "Testing graalpy ast"
python fuzz4py/eval.py "graalpy -m ast" --timeout=30 --output="fuzz4py/resources/graalpy_ast"

# black
echo "Testing black"
python fuzz4py/eval.py "black" --timeout=30 --output="fuzz4py/resources/black"

# pyflakes
echo "Testing pyflakes"
python fuzz4py/eval.py "pyflakes" --timeout=30 --output="fuzz4py/resources/pyflakes"

# pylint
echo "Testing pylint"
python fuzz4py/eval.py "pylint" --timeout=30 --output="fuzz4py/resources/pylint"

# mypy
echo "Testing mypy"
python fuzz4py/eval.py "mypy" --timeout=30 --output="fuzz4py/resources/mypy"

# pycodestyle
echo "Testing pycodestyle"
python fuzz4py/eval.py "pycodestyle" --timeout=30 --output="fuzz4py/resources/pycodestyle"

# flake8
echo "Testing flake8"
python fuzz4py/eval.py "flake8" --timeout=30 --output="fuzz4py/resources/flake8"

# ruff
echo "Testing ruff"
python fuzz4py/eval.py "ruff check" --timeout=30 --output="fuzz4py/resources/ruff"

# astroid
echo "Testing astroid"
python fuzz4py/eval.py "python -c 'import astroid; import sys; astroid.parse(open(sys.argv[1]).read())'" --timeout=30 --output="fuzz4py/resources/astroid"

# parso
echo "Testing parso"
python fuzz4py/eval.py "python -c 'import parso; import sys; parso.parse(open(sys.argv[1]).read())'" --timeout=30 --output="fuzz4py/resources/parso"

# pytype
echo "Testing pytype"
python fuzz4py/eval.py "pytype" --timeout=30 --output="fuzz4py/resources/pytype"

# bandit
echo "Testing bandit"
python fuzz4py/eval.py "bandit" --timeout=30 --output="fuzz4py/resources/bandit"

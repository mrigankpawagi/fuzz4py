# Fuzz4Py
Fuzz4Py is a Python-based fuzzing framework designed to test and evaluate Python interpreters and libraries. By generating a wide range of inputs, Fuzz4Py can help identify bugs and vulnerabilities in Python code.

### What is Fuzzing?
Fuzzing is a software testing technique that involves bombarding a program with a large number of inputs to trigger unexpected behavior. This can help identify bugs and vulnerabilities.

This repository is inspired by [Fuzz4All](https://github.com/fuzz4all/fuzz4all/tree/main/Fuzz4All), [PyRTFuzz](https://github.com/awen-li/PyRTFuzz), and [DyFuzz](https://github.com/xiaxinmeng/DyFuzz).

## Bug Hall of Fame
The following are some of the bugs discovered by Fuzz4Py.

- [CPython Issue #127927](https://github.com/python/cpython/issues/127927) &mdash; `SyntaxError` raised from `compile` has incorrect attributes (line number, offset, or text) in multiple scenarios.

### Usage

> [!WARNING]
> This project is recommended to be run on Linux with Python 3.12 or later.

You must have CPython 3.11, CPython 3.12, CPython 3.13, and GraalPy installed on your system to run the tests.

```bash
python -m venv env && source env/bin/activate # Create a virtual environment
python -m pip install -r requirements.txt # Install dependencies
```

To install all the target python modules, run `python -m pip install -r modules.txt`.

Copy the `fuzz4py/sample.env` file to `fuzz4py/.env` and add your API key(s) from Google AI Studio. To run the library fuzzer at `libfuzzing/`, you need to clone [ghAIstwriter](https://github.com/mrigankpawagi/ghAIstwriter) into the `libfuzzing/` directory and set it up as per the instructions in that repository.

#### Distillation

```bash
python fuzz4py/distillation.py # distill parts of the Python documentation
```

> [!NOTE]
> The parts of Python documentation used for distillation were obtained from the plain text version of the [Python 3.13 documentation](https://docs.python.org/3/archives/python-3.13-docs-text.zip) (as of Dec 6, 2024). Some manually written fragments may also be included. The file `fuzz4py/documentation/index.txt` contains the list of documents to be used in a logical order.

The distilled prompt is saved in `fuzz4py/resources/prompt.txt`.

#### Input Generation

```bash
python fuzz4py/fuzzer.py [--prompt] [--inputs-directory] [--budget]
```

The generated inputs are saved in the directory specified by the `--inputs-directory` flag, which is by default set to `fuzz4py/inputs/`. A `log.txt` file is also generated in the same directory to keep track of the provenance of the generated inputs. The `--prompt` flag is an optional argument that specifies the path to the prompt file or the prompt string itself. It is by default set to `fuzz4py/resources/prompt.txt`. The `--budget` flag is an optional argument that specifies the number of inputs to generate and is by default set to 10. As such, the `Fuzzer` class in `fuzz4py/fuzzer.py` can be used to generate inputs as follows.

```python
from fuzz4py.fuzzer import Fuzzer

fuzzer = Fuzzer(system_prompt, inputs_directory="inputs", budget=10)
fuzzer.fuzz()
```

The `system_prompt` is provided before every prompt for generating inputs and is ideally the distilled prompt from the previous step. The `inputs_directory` is an optional argument that specifies the directory to save the generated inputs and is by default set to `fuzz4py/inputs/`. The `budget` is the number of inputs to generate and is by default set to 10.

#### Evaluation

```bash
python fuzz4py/eval.py path/to/python [--inputs] [--output] [--timeout]
```

The `path/to/python` is the path to the Python executable (in our case, CPython 3.13) to be fuzzed. The `--inputs` flag is an optional argument that specifies the directory containing the inputs to be used for evaluation and is by default set to `fuzz4py/inputs/`. The `--output` flag is an optional argument that specifies the directory to save the outputs of the evaluation and is by default set to `fuzz4py/resources`. The `--timeout` flag is an optional argument that specifies the timeout for each input in seconds and is by default set to 60.

> [!WARNING]
> LLM generated code may not be safe to run on your system. Use a secure environment like a container or a virtual machine to run the generated code.

# Fuzz4Py
Fuzzing Python. Inspired by [Fuzz4All](https://github.com/fuzz4all/fuzz4all).

### Usage

> [!WARNING]
> This project currently supports only Linux.

You must have [LLVM 18](https://github.com/python/cpython/blob/main/Tools/jit/README.md) installed on your system in order to build CPython 3.13 with the `--enable-experimental-jit` flag. Download and build [CPython](https://github.com/python/cpython) by running `./setup_cpython.sh`.

```bash
python -m venv env && source env/bin/activate # Create a virtual environment
python -m pip install -r requirements.txt # Install dependencies
```

Copy the `fuzz4py/sample.env` file to `fuzz4py/.env` and add your API key(s) from Google AI Studio.

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

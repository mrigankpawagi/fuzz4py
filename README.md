# Fuzz4Py
Fuzzing Python. Inspired by [Fuzz4All](https://github.com/fuzz4all/fuzz4all).

### Usage

> [!WARNING]
> This project currently supports only Linux.

You must have [LLVM 18](https://github.com/python/cpython/blob/main/Tools/jit/README.md) installed on your system in order to build Python 3.13 with the `--enable-experimental-jit` flag. Download and build [CPython](https://github.com/python/cpython) by running `./setup.sh`.

```bash
sudo -s # Run as root (for secure execution with PyJail)
python -m venv env && source env/bin/activate # Create a virtual environment
python -m pip install -r requirements.txt # Install dependencies
```

Copy the `fuzz4py/sample.env` file to `fuzz4py/.env` and add your API key from Google AI Studio.

#### Distillation

```bash
python fuzz4py/distillation.py # distill parts of the Python documentation
```

> [!NOTE]
> The parts of Python documentation used for distillation were obtained from the plain text version of the [Python 3.13 documentation](https://docs.python.org/3/archives/python-3.13-docs-text.zip) (as of Dec 6, 2024). The file `fuzz4py/documentation/index.txt` contains the list of documents to be used in a logical order.

The distilled prompt is saved in `fuzz4py/resources/prompt.txt`.

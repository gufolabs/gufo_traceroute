# Code Quality Guide

We share the common code quality standards between all Gufo Labs projects.

## Python Code Formatting

All Python code must be formatting using [Black][Black] code formatter
with settings defined in the project's `pyproject.toml` file.

## Python Docstrings

All Python functions and methods must be documenting using
Google docstrings format.

## Python Code Linting

All Python code must pass [Ruff][Ruff] tests with the project's settings.

## Python Code Static Checks

All python code must pass [Mypy][Mypy] type checks in the `strict` mode.

## Test Suite Coverage

The test suite must provide 100% code coverage whenever possible.

## Documentation Standards

* Documentation must be clean and mean.

[Black]: https://black.readthedocs.io/en/stable
[Ruff]: https://github.com/charliermarsh/ruff
[Mypy]: https://mypy.readthedocs.io/en/stable/

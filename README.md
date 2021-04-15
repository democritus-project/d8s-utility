# Democritus Utility

[![PyPI](https://img.shields.io/pypi/v/d8s-utility.svg)](https://pypi.python.org/pypi/d8s-utility)
[![CI](https://github.com/democritus-project/d8s-utility/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-utility/actions)
[![Lint](https://github.com/democritus-project/d8s-utility/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-utility/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-utility/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-utility)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with utility functions.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def copy_first_arg(func):
        """Decorator to make a copy of the first argument and pass into the func."""
    ```
  - ```python
    def has_more_than_one_item(thing: Any) -> bool:
        """Return whether or not the given thing has a length of at least one."""
    ```
  - ```python
    def has_one_or_more_items(thing: Any) -> bool:
        """Return whether or not the given thing has a length of at least one."""
    ```
  - ```python
    def has_one_item(thing: Any) -> bool:
        """Return whether or not the given thing has a length of at least one."""
    ```
  - ```python
    def request_or_read(path):
        """If the given path is a URL, request the URL and return the content; if the path exists read the file.
    
    Otherwise, just return the string and assume it is the input itself."""
    ```
  - ```python
    def request_or_read_first_arg(func):
        """If the first arg is a url - request the URL. If it is a file path, try to read the file.
    
    If it is neither a URL nor file path, return the content of the first arg."""
    ```
  - ```python
    def is_sorted(iterable, *, descending: bool = False) -> bool:
        """Return whether or not the iterable is sorted."""
    ```
  - ```python
    def first_unsorted_value(iterable, *, descending: bool = False) -> Any:
        """Return the first unsorted value in the iterable."""
    ```
  - ```python
    def last_unsorted_value(iterable, *, descending: bool = False) -> Any:
        """Return the last unsorted value in the iterable."""
    ```
  - ```python
    def unsorted_values(iterable, *, descending: bool = False) -> Iterable[Any]:
        """."""
    ```
  - ```python
    def sorted_values(iterable, *, descending: bool = False) -> Iterable[Any]:
        """."""
    ```
  - ```python
    def ignore_errors(function, *args, **kwargs):
        """."""
    ```
  - ```python
    def zip_if_same_length(*iterables, debug_failure: bool = False):
        """Zip the given iterables if they are the same length.
    
    If they are not the same length, raise an assertion error."""
    ```
  - ```python
    def unique_items(iterable_a: Any, iterable_b: Any) -> Dict[str, Set[Any]]:
        """Find the values unique to iterable_a and iterable_b (relative to one another)."""
    ```
  - ```python
    def prettify(thing: Any, *args):
        """."""
    ```
  - ```python
    def pretty_print(thing: Any, *args):
        """."""
    ```
  - ```python
    def subprocess_run(command, input_=None):
        """Run the given command as if it were run in a command line."""
    ```
  - ```python
    def stringify_first_arg(func):
        """Decorator to convert the first argument to a string."""
    ```
  - ```python
    def retry_if_no_result(wait_seconds=10):
        """Decorator to call the given function and recall it if it returns nothing."""
    ```
  - ```python
    def map_first_arg(func):
        """If the first argument is a list or tuple, iterate through each item in the list and send it to the function."""
    ```
  - ```python
    def repeat_concurrently(n: int = 10):
        """Repeat the decorated function concurrently n times."""
    ```
  - ```python
    def validate_keyword_arg_value(
        keyword: str, valid_keyword_values: Iterable[Any], fail_if_keyword_not_found: bool = True
    ):
        """Validate that the value for the given keyword is in the list of valid_keyword_values."""
    ```
  - ```python
    def validate_arg_value(arg_index: StrOrNumberType, valid_values: Iterable[Any]):
        """Validate that the value of the argument at the given arg_index is in the list of valid_values."""
    ```
  - ```python
    def wait_and_retry_on_failure(wait_seconds=10):
        """Try to call the given function.
    
    If there is an exception thrown by the function, wait for wait_seconds and try again."""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-

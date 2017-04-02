# Project Template for Python

An OS independent project template for Python. It uses `setup.py` for build-management.  
The following commands are build-in:

* `package`: create a *Wheels* package
* `check_code`: code analysis with *Pylint*.
* `check_style_code`: *PEP 8* code style check
* `check_style_doc`: *PEP 257* docstring style check
* `doc_api`: API documentation with Sphinx
* `doc_manual`: generate HTML documentation from Markdown
* `test`: run unit tests
* `coverage`: generate unit test coverage report


## Usage

1. Copy all files and folders.
2. Rename folder `example` and `example.py` to your API name.
3. Add your dependencies to `setup.py`, `requirements.txt` and `requirements-dev.txt`.
4. Change license in `LICENSE` and `setup.py`.
5. Change the project name, API name, version, author, e-mail in `doc/sphinx/index.rst`, `example/__init__.py`, `setup.py`, `setup_commands.py`.
6. Change or remove code examples in `example` and `tests`.

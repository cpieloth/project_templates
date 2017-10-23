# Getting Started

## Command line usage

```bash
# Print help
./example.py --help

# Print help of the sub command 'hello'
./example.py hello --help

# Execute sub command 'hello'
./example.py hello Alice
```


## Dependencies & Virtualenv

* `requirements.txt` lists runtime dependencies
* `requirements-dev.txt` lists dependencies for development

It is recommended to install the dependencies and run the tool in a *virtualenv*.
Virtualenv is a tool to create an "isolated" Python environment.
It helps to keep your base system clean and reduces dependency conflicts.

```bash
cd <project>
 
# create environment with default python version
virtualenv --no-site-packages venv
# create environment with python 3 (Linux)
virtualenv --no-site-packages -p /usr/bin/python3 venv

# activate virtualenv (Linux)
source venv/bin/activate
# activate virtualenv (Windows)
.\venv\Scripts\activate

# install development dependencies
pip3 install -r requirements-dev.txt
 
# run 'hello' command (Linux)
./example.py hello Alice
# run 'hello' command (Windows)
python example.py hello Alice
 
# deactivate and destroy environment
deactivate
rm -rf venv/
```


## Development & Build Management

`setup.py` contains extra commands for development:

```bash
cd <project>

# print extra commands (Linux)
./setup.py --help-commands | grep EXAMPLE
# print extra commands (Windows)
python setup.py --help-commands

package           EXAMPLE: Create a Python Built Distribution package.
check_code        EXAMPLE: Run code analysis with pylint.
check_style       EXAMPLE: Run style checkers.
check_style_code  EXAMPLE: Run style checker for code with pep8.
check_style_doc   EXAMPLE: Run style checker for docstrings with pep257.
documentation     EXAMPLE: Generate HTML documentation with Sphinx.
test              EXAMPLE: Run unit tests.
coverage          EXAMPLE: Generate unit test coverage report.
```

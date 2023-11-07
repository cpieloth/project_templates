# Getting Started    {#getting_started_md}

This guide is written for Ubuntu Linux.


## Preparation & Resolve Dependencies

    $ cd cpp_conan
    $ mkdir build
    $ conan install . --output-folder=build --build=missing
    $ cmake . -B build -DCMAKE_BUILD_TYPE=Release


## Generate & Open Documentation

    $ cd cpp_conan
    $ conan install . --output-folder=build --build=missing -o documentation=True
    $ cmake --build build --target doxygen
    $ xdg-open build/doc/html/index.html


### Compile & Run Example

    $ cd cpp_conan
    $ cmake --build build
    $ build/src/example/example --help


### Linting

The following linter tools are supported:

* *clang-tidy*, must be installed on system
* *cppcheck*, installed via conan with the option `linting=True`

The linter tools are only executed when target is built. By default the linter tools are disabled/skipped and can be enabled using options:

* `SKIP_LINTING_CLANG_TIDY=OFF`
* `SKIP_LINTING_CPPCHECK=OFF`

For example:

    $ cd cpp_conan
    $ mkdir build
    $ conan install . --output-folder=build --build=missing -o liniting=True
    $ cmake . -B build/ -DCMAKE_BUILD_TYPE=Release -DSKIP_LINTING_CLANG_TIDY=OFF -DSKIP_LINTING_CPPCHECK=OFF
    $ cmake --build build

## Deprecated

### Run Unit Tests

    $ cd project_templates/c_cpp/build
    $ make test         # run all unit tests
    $ make test_run_io  # run a single unit test

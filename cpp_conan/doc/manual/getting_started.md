# Getting Started    {#getting_started_md}

This guide is written for Ubuntu Linux.


## Preparation & Resolve Dependencies

    $ cd cpp_conan
    $ mkdir build
    $ conan install . --output-folder=build --build=missing
    $ cmake . -B build -DCMAKE_BUILD_TYPE=Release


## Generate & Open Documentation

    $ cd cpp_conan
    $ cmake --build build --target doxygen
    $ xdg-open build/doc/html/index.html


### Compile & Run Example

    $ cd cpp_conan
    $ cmake --build build
    $ build/src/example/example --help


## Deprecated

### Run Unit Tests

    $ cd project_templates/c_cpp/build
    $ make test         # run all unit tests
    $ make test_run_io  # run a single unit test

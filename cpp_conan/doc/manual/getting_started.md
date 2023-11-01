# Getting Started

## Preparation & Resolve Dependencies

    $ cd cpp_conan
    $ mkdir build
    $ conan install . --output-folder=build --build=missing
    $ cmake . -B build -DCMAKE_BUILD_TYPE=Release


## Generate Documentation

    $ cd cpp_conan
    $ cmake --build build --target doxygen


## Deprecated

### Compile Example

    $ cd project_templates/c_cpp
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make


### Run Unit Tests

    $ cd project_templates/c_cpp/build
    $ make test         # run all unit tests
    $ make test_run_io  # run a single unit test


### Run Example

    $ cd project_templates/c_cpp/build
    $ src/example/example -h
    $ src/example/example -f foo -l bar

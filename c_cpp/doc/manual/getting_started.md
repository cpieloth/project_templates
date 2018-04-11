# Getting Started

## Generate Documentation

    $ cd project_templates/c_cpp
    $ mkdir build
    $ cmake ..
    $ make documentation


## Compile Example

    $ cd project_templates/c_cpp
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make


## Run Unit Tests

    $ cd project_templates/c_cpp/build
    $ make test         # run all unit tests
    $ make test_run_io  # run a single unit test


## Run Example

    $ cd project_templates/c_cpp/build
    $ src/example/example -h
    $ src/example/example -f foo -l bar

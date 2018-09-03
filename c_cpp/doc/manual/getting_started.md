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


## Install Development Requirements

    $ cd project_templates/c_cpp/build
    $ sudo apt-get install python3-pip python3-apt
    $ pip3 install virtualenv
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip3 install -r ansible/requirements.txt
    $ ansible-playbook ansible/playbook_setup_environment.yml -c local -K -e "ansible_python_interpreter=/usr/bin/python3"

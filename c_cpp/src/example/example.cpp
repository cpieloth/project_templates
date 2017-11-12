#ifndef EXAMPLE_EXAMPLE_HPP_
#define EXAMPLE_EXAMPLE_HPP_

extern "C"
{
#include <stdlib.h>
#include <unistd.h>
}

#include <iostream>
#include <string>

#include "example/io.hpp"

using namespace example::io;

typedef struct
{
    std::string firstName;
    bool hasFirstName;
    std::string lastName;
    bool hasLastName;
} args_t;

static void _printHelp(const std::string& exec)
{
    std::cerr << "Usage: " << exec << " -f <first name> -l <last name>" << std::endl;
}

static args_t _parseArgs(int argc, char* argv[])
{
    args_t args;
    args.hasFirstName = false;
    args.hasLastName = false;

    int opt;
    while ((opt = getopt(argc, argv, "hf:l:")) != -1)
    {
        switch (opt)
        {
        case 'h':
            _printHelp(argv[0]);
            exit(EXIT_SUCCESS);
        case 'f':
            args.firstName = optarg;
            args.hasFirstName = true;
            break;
        case 'l':
            args.lastName = optarg;
            args.hasLastName = true;
            break;
        default:
            _printHelp(argv[0]);
            exit(EXIT_FAILURE);
        }
    }

    if (!args.hasFirstName || !args.hasLastName)
    {
        std::cerr << "Missing argument: '-f <first name>' and '-l <last name>' are required." << std::endl;
        exit(EXIT_FAILURE);
    }

    return args;
}

int main(int argc, char* argv[])
{
    args_t args = _parseArgs(argc, argv);
    printWelloWorld(args.firstName, args.lastName);
    return EXIT_SUCCESS;
}

#endif  // EXAMPLE_EXAMPLE_HPP_

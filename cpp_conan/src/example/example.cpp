#include <cstdlib>

#include <iostream>
#include <string>

#include <boost/program_options.hpp>

#include "example/io.hpp"


namespace io = example::io;
namespace po = boost::program_options;


typedef struct
{
    std::string firstName;
    std::string lastName;
} args_t;


static args_t _parseArgs(int argc, char* argv[])
{
    args_t args;

    po::options_description desc("Allowed options");
    desc.add_options()
        ("help", "Print help message")
        ("firstname,f", po::value<std::string>(&args.firstName)->required(), "first name")
        ("lastname,l", po::value<std::string>(&args.lastName)->required(), "last name")
    ;

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    try {
        po::notify(vm);
        if (vm.count("help")) {
            std::cout << desc << "\n";
            exit(EXIT_SUCCESS);
        }
         return args;
    }
    catch(const po::error& ex) {
        if (vm.count("help")) {
            std::cout << desc << "\n";
            exit(EXIT_SUCCESS);
        }

        std::cout << ex.what() << "\n";
        exit(EXIT_FAILURE);
    }
}


int main(int argc, char* argv[])
{
    args_t args = _parseArgs(argc, argv);
    io::printWelloWorld(args.firstName, args.lastName);
    return EXIT_SUCCESS;
}

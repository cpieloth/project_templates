#include <iostream>

#include "example/io.hpp"

using namespace example::io;

std::string example::io::printWelloWorld(const std::string& firstName, const std::string& lastName)
{
    const std::string hello = "Hello " + firstName + " " + lastName + "!";
    std::cout << hello << std::endl;
    return hello;
}

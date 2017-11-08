#include <iostream>

#include "example/io.hpp"

using namespace example::io;

std::string example::io::print_hello_world(std::string name)
{
	const std::string hello = "Hello " + name + "!";
	std::cout << hello << std::endl;
	return hello;
}

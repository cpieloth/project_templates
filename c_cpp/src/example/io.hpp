#ifndef EXAMPLE_IO_HPP_
#define EXAMPLE_IO_HPP_

#include <string>

namespace example
{
namespace io
{

/**
 * Print 'Hello <name>!' to stdout.
 *
 * @param name Name to say hello.
 * @return Printed string.
 */
std::string print_hello_world(std::string name);

}
}

#endif  // EXAMPLE_IO_HPP_

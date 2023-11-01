#pragma once

#include <string>

namespace example
{
namespace io
{

/**
 * Print 'Hello \<first_name> \<last_name>!' to stdout.
 *
 * @param firstName First name of person to greet.
 * @param lastName Last name of person to greet.
 * @return Printed string.
 */
std::string printWelloWorld(const std::string& firstName, const std::string& lastName);

}
}

#ifndef EXAMPLE_IOTEST_HPP_
#define EXAMPLE_IOTEST_HPP_

#include <cxxtest/TestSuite.h>

#include <example/io.hpp>


class IoTestSuite: public CxxTest::TestSuite
{
 public:
    void testPrintWelloWorld(void);
};


void IoTestSuite::testPrintWelloWorld()
{
	TS_ASSERT(example::io::printWelloWorld("Foo", "Bar").compare("Hello Foo Bar!") == 0);
}

#endif  // EXAMPLE_IOTEST_HPP_

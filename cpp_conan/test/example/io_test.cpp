#include <gtest/gtest.h>
#include "example/io.hpp"


TEST(IO, printWelloWorld)
{
    EXPECT_STREQ(example::io::printWelloWorld("Foo", "Bar").c_str(), "Hello Foo Bar!");
}

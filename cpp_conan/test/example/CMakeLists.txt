find_package(GTest REQUIRED)

add_executable(
    io_test
    io_test.cpp
)
target_link_libraries(
    io_test
    ExampleIo
    GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(io_test XML_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/reports)

include(CxxTest)

# IO unit test
list(APPEND test_io_header "${CMAKE_CURRENT_SOURCE_DIR}/IoTest.hpp")
list(APPEND test_io_include_dirs "${PROJECT_SOURCE_DIR}/src")
list(APPEND test_io_libs "ExampleIo")
list(APPEND test_io_deps)

cxxtest_create("io"
               "${test_io_header}"
               "${test_io_include_dirs}"
               "${test_io_libs}"
               "${test_io_deps}"
)
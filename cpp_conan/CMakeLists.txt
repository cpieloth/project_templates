##
# General CMake settings
#
cmake_minimum_required(VERSION 3.27)

project(Example CXX)
set(CMAKE_CXX_STANDARD 17)


##
# Conan
#
include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)


##
# CMake Modules
#
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)


##
# Linting
#
include(clang-tidy)
include(cppcheck)


# Enable testing with CTest
include(CTest)


##
# Directories
#
add_subdirectory(${PROJECT_SOURCE_DIR}/doc)
add_subdirectory(${PROJECT_SOURCE_DIR}/src)
add_subdirectory(${PROJECT_SOURCE_DIR}/test)

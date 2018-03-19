##
# General CMake settings
#
cmake_minimum_required(VERSION 2.8.12)
project(Example)
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

##
# Documentation
#
add_custom_target("documentation")

include(Doxygen)
doxygen_create("doxygen" ${PROJECT_SOURCE_DIR}/doc/Doxyfile)
add_dependencies("documentation" "doxygen")

##
# Compiler Settings
#
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif(NOT CMAKE_BUILD_TYPE)

##
# Directories
#
add_subdirectory(${PROJECT_SOURCE_DIR}/src)

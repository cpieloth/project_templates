##
# Documentation
#
find_package(Doxygen)

if(NOT DOXYGEN_FOUND)
    return()
endif()

# use Doxyfile.in to solve overwrite problems using mixeddoxygen_add_docs() and Doxyfile.
set(DOXYGEN_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)

doxygen_add_docs(
    doxygen
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    CONFIG_FILE ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
)
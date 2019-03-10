##
# Documentation
#
add_custom_target("documentation")

include(Doxygen)
doxygen_create("doxygen" ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile)
add_dependencies("documentation" "doxygen")
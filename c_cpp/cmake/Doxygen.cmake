##
# Module to build doxygen documentation.
#

##
# Add a target with related command to call doxygen for given config file.
# @note: Output directory depends on config file and not CMAKE_BINARY_DIR!
#
# @param target_name  Target name to use for the command.
# @param config_name  Doxygen config file to use.
#
function(doxygen_create target_name config_name)
    find_program(DOXYGEN doxygen)
    if(NOT DOXYGEN)
        message(WARNING "Doxygen documentation is not available. Please install doxygen.")
        return()
    endif()

    # get and use directory of config file as working directory,
    # such that relative paths belongs to config file location
    get_filename_component(working_dir ${config_name} DIRECTORY)
    add_custom_target(${target_name} ${DOXYGEN} ${config_name}
                      WORKING_DIRECTORY ${working_dir}
                      COMMENT "Call doxygen for config file: ${config_name}")
endfunction(doxygen_create)

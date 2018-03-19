##
# Module to build doxygen documentation.
#

##
# Add a target with related command to call doxygen for given config file.
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
    
    add_custom_target(${target_name} ${DOXYGEN} ${config_name}
                      COMMENT "Call doxygen for config file: ${config_name}")
endfunction(doxygen_create)

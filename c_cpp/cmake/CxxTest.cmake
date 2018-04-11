##
# Provide helper functions to create CxxTest unit tests.
#
# @author christof.pieloth
#

find_package(CxxTest REQUIRED)


##
# Create/setup a C++ unit test with CxxTest. The function creates a target for compilation and a target to run the test.
# The targets have the prefix "test_" and "test_run_".
# 
# @param test_name[in]    Name of the test, without any prefix or suffix! Used for target name.
# @param header_files[in] List of required header files. Type is a CMake list, pass it in quotes!.
# @param include_dirs[in] List of required include directories. Type is a CMake list, pass it in quotes!.
# @param libraries[in]    List of libraries to link. Type is a CMake list, pass it in quotes!
# @param dependencies[in] List of dependencies. Type is a CMake list, pass it in quotes!
#
function(cxxtest_create test_name header_files include_dirs libraries dependencies)
    # Target for compilation
    cxxtest_target_name(target_name ${test_name})
    
    CXXTEST_ADD_TEST(${target_name} ${target_name}.cpp ${header_files})
    
    if(include_dirs)
        target_include_directories(${target_name} PUBLIC ${include_dirs})
    endif()
    
    if(libraries)
        target_link_libraries(${target_name} ${libraries})
    endif()

    if(dependencies)
        add_dependencies(${target_name} ${dependencies})
    endif()

    # Target for test execution
    cxxtest_exec_name(exec_name ${test_name})

    set(exec "$<TARGET_FILE:${target_name}>")
    add_custom_target(${exec_name} COMMAND sh -c "${exec_prefix} ${exec}" VERBATIM)
    add_dependencies(${exec_name} ${target_name})
endfunction(cxxtest_create)


##
# Get generated target name for test compilation which will be or is used for cxxtest_create_*.
# For example, can be used for as depenency for other targets.
# The target_name has the format "test_<test_name>".
#
# @param target_name[out] Output variable, name of the used target. Pass it without ${...}.
# @param test_name[in]    Name of the test, without any prefix or suffix! Used for target name.
#
function(cxxtest_target_name target_name test_name)
    set(${target_name} "test_${test_name}" PARENT_SCOPE)
endfunction(cxxtest_target_name)


##
# Get generated target name for test execution which will be or is used for cxxtest_create_*.
# For example, can be used for as depenency for other targets.
# The exec_name has the format "test_run_<test_name>".
#
# @param exec_name[out] Output variable, name of the used target for execution. Pass it without ${...}.
# @param test_name[in]  Name of the test, without any prefix or suffix! Used for target name.
#
function(cxxtest_exec_name exec_name test_name)
    set(${exec_name} "test_run_${test_name}" PARENT_SCOPE)
endfunction(cxxtest_exec_name)
